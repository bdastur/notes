#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime
import boto3
import click
import os
import pickle
import pprint
import sys


def generate_summary(instances):
    """
    Generate summary object
    """
    summary = {}
    summary['by_region'] = {}
    summary['last_7_days'] = {}
    summary['by_tags'] = {}


    idx = 0
    for instance in instances:

        # Categorize by region
        ##################################################
        region = instance['region']
        if summary['by_region'].get(region, None) is None:
            summary['by_region'][region] = []
        summary['by_region'][region].append(idx)

        # Last 7 days
        ##################################################
        today  = datetime.datetime.now()
        today_str = today.strftime('%Y-%m-%d')

        time_delta = datetime.timedelta(days=7)
        check_launch_date =  today - time_delta
        check_launch_date_str = check_launch_date.strftime('%Y-%m-%d')

        launch_time = instance['LaunchTime']
        launch_time = launch_time.replace(tzinfo=None)
        if launch_time > check_launch_date:
            instance_type = instance['InstanceType']
            if summary['last_7_days'].get(instance_type, None) is None:
                summary['last_7_days'][instance_type] = []

            summary['last_7_days'][instance_type].append(idx)

        # By tags
        ####################################################
        tags = instance['Tags']
        for tag in tags:
            key = tag['Key']
            value = tag['Value']
            key = key.strip()
            value = value.strip()
            if summary['by_tags'].get(key, None) is None:
                summary['by_tags'][key] = {}

            if summary['by_tags'][key].get(value, None) is None:
                summary['by_tags'][key][value] = []

            summary['by_tags'][key][value].append(idx)

        idx += 1

    # pp = pprint.PrettyPrinter()
    # pp.pprint(summary)
    return summary

def filter_instances_launch_date(instances, from_date, to_date):
    filteredInstances = []
    fromDate = datetime.datetime.strptime(from_date, '%Y-%m-%dT%H:%M:%S+00:00')
    toDate = datetime.datetime.strptime(to_date, '%Y-%m-%dT%H:%M:%S+00:00')

    for instance in instances:
        launchDate = instance['LaunchTime']
        if instance['BlockDeviceMappings']:
            launchDate = instance['BlockDeviceMappings'][0]['Ebs']['AttachTime']

        launchDate_str = launchDate.strftime("%Y-%m-%dT%H:%M:%S+00:00")
        launchDate = launchDate.replace(tzinfo=None)
        if launchDate > fromDate and launchDate <= toDate:
            filteredInstances.append(instance)
            # print("Instance launched at %s, between (%s - %s) " % \
            #       (launchDate_str, from_date, to_date))

    print("Instance launched between (%s - %s) %d" % \
        (from_date, to_date, len(filteredInstances)))
    return filteredInstances


def get_ec2_instances(**kwargs):
    all_instances = []
    profile_name = kwargs.get('profile_name', 'dev')
    region = kwargs.get('region', 'us-east-1')
    session = boto3.Session(profile_name=profile_name, region_name=region)
    client = session.client('ec2')

    nextToken = None
    done = False
    while not done:
        if not nextToken:
            data = client.describe_instances(MaxResults=1000)
        else:
            data = client.describe_instances(MaxResults=1000, NextToken=nextToken)

        for reservation in data['Reservations']:
            instances = reservation['Instances']
            all_instances.extend(instances)
        sys.stdout.write(".")
        sys.stdout.flush()

        try:
            nextToken = data['NextToken']
        except KeyError:
            done = True
            continue

    print("[%s] Total Instances: [%d]", region, len(all_instances))
    for instance in all_instances:
        instance['region'] = region

    return all_instances


def generate_csv_file_from_instances_info(instances, name):

    fpath = os.path.join("/Users/behzaddastur/scratch", name)
    fhandle = open(fpath, "w")
    row_heading = ["status", "instance id", "AZ", "instance type", "launch date",
                   "attach date", "state", "Termination time", "c_deployment", "c_role"]
    rowHeadingString = ",".join(row_heading) + "\n"
    fhandle.write(rowHeadingString)

    for instance in instances:
        row = []
        launchDate = instance['LaunchTime'].strftime('%Y-%m-%d')

        if instance['BlockDeviceMappings']:
            attachDate = instance['BlockDeviceMappings'][0]['Ebs']['AttachTime'].strftime('%Y-%m-%d')
        else:
            attachDate = launchDate

        if attachDate == launchDate:
            row.append("NEW INSTANCE")
        else:
            row.append("Restarted")


        row.append(instance['InstanceId'])
        row.append(instance['Placement']['AvailabilityZone'])
        row.append(instance['InstanceType'])
        row.append(launchDate)
        row.append(attachDate)
        row.append(instance['State']['Name'])
        if not instance['StateTransitionReason']:
            row.append("NA")
        else:
            row.append(instance['StateTransitionReason'])

        for tag in instance['Tags']:
            key = tag['Key']
            value = tag['Value']
            if key == "c_deployment":
                #row.append(value)
                row.insert(8, value)
            if key == "c_role":
                #row.append(value)
                row.insert(9, value)

        rowString = ",".join(row) + "\n"
        fhandle.write(rowString)

    fhandle.close()


def collect_all_instances_data():
    regions = ["us-east-1", "us-west-2", "ap-southeast-1",
               "ap-southeast-2", "eu-central-1", "eu-west-1"]

    allInstances = []
    for region in regions:
        options = {
            "profile_name": "dev",
            "region": region
        }
        instances = get_ec2_instances(**options)
        allInstances.extend(instances)

    return allInstances


def main():
    rawDataFile = "/Users/behzaddastur/scratch/raw_data.pickle"

    try:
        fhandle = open(rawDataFile, "rb")
        allInstances = pickle.load(fhandle)
        fhandle.close()
    except FileNotFoundError:
        allInstances = collect_all_instances_data()
        fhandle = open(rawDataFile, "wb")
        pickle.dump(allInstances, fhandle, pickle.HIGHEST_PROTOCOL)
        fhandle.close()

    # Find instances by region.

    # Generate report (All Instances - no filter)
    generate_csv_file_from_instances_info(allInstances, "all_instances.csv")

    #filter_instances_launch_date(allInstances, "2021-03-01", "2021-03-30")
    #filter_instances_launch_date(allInstances, "2021-04-01", "2021-04-30")
    #filter_instances_launch_date(allInstances, "2021-05-01", "2021-05-14")

    filteredInstances = filter_instances_launch_date(allInstances,
                                 '2021-05-19T00:01:01+00:00',
                                 '2021-05-20T00:01:00+00:00')
    print("Filtered instances: ", filteredInstances)
    summary = generate_summary(allInstances)


if __name__ == "__main__":
    main()
