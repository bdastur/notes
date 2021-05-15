#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime
import boto3
import os
import pprint


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
        print(".", end="")
        
        try:
            nextToken = data['NextToken']
        except KeyError:
            done = True
            continue

    print(len(all_instances))
    return all_instances

def filter_instances_launch_date(instances, from_date):
    filteredInstances = []
    fromDate = datetime.datetime.strptime(from_date, '%Y-%m-%d')
    for instance in instances:
        launchDate = instance['LaunchTime']
        launchDate = launchDate.replace(tzinfo=None)
        print("Launch date: ", instance['LaunchTime'])
        if launchDate > fromDate:
            filteredInstances.append(instance)
    
    print("Instance with LD > %s : %d", fromDate, len(filteredInstances))


def generate_csv_file_from_instances_info(instances, name):
    
    fpath = os.path.join("/Users/behzaddastur/scratch", name)
    fhandle = open(fpath, "w")
    row_heading = ["instance id", "AZ", "instance type", "launch date",
                   "state", "c_deployment"]
    rowHeadingString = ",".join(row_heading) + "\n"
    fhandle.write(rowHeadingString)

    for instance in instances:
        row = []
        launchDate = instance['LaunchTime'].strftime('%Y-%m-%d')

        row.append(instance['InstanceId'])
        row.append(instance['Placement']['AvailabilityZone'])
        row.append(instance['InstanceType'])
        row.append(launchDate)
        row.append(instance['State']['Name'])
        for tag in instance['Tags']:
            key = tag['Key']
            value = tag['Value']
            if key == "c_deployment":
                row.append(value)
        
        rowString = ",".join(row) + "\n" 
        fhandle.write(rowString)

    fhandle.close()




def main():
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

    
    generate_csv_file_from_instances_info(allInstances, "all_instances.csv")

    #filter_instances_launch_date(all_instances, "2021-05-01")



if __name__ == "__main__":
    main() 
