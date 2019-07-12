#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import datetime
import boto3
import botocore


class CloudTrailHelper(object):
    def __init__(self, account_id, role, region):
        # Use okta2aws role.
        session = boto3.Session(profile_name="okta2aws")
        sts_client = session.client('sts')
        try:
            role_arn = "arn:aws:iam::" + account_id + ":role/" + role
            assumed_role_creds = sts_client.assume_role(RoleArn=role_arn, RoleSessionName="test")
        except botocore.exceptions.ClientError as err:
            print("Failed to get caller identity ", err)
            return

        # Create new session:
        sess = boto3.Session(aws_access_key_id=assumed_role_creds['Credentials']['AccessKeyId'],
                             aws_secret_access_key=assumed_role_creds['Credentials']['SecretAccessKey'],
                             aws_session_token=assumed_role_creds['Credentials']['SessionToken'])
        self.cl_client = sess.client('cloudtrail')

    def parse_events(self, events_obj, events):
        for event in events:
            event_name = event['EventName']
            if events_obj.get(event_name, None) is None:
                events_obj[event_name] = {}
                events_obj[event_name]['Count'] = 0
                events_obj[event_name]['EventDetails'] = []

            events_obj[event_name]['Count'] += 1
            event_detail = {}
            event_detail['UserName'] = event['Username']
            event_detail['EventTime'] = event['EventTime']
            events_obj[event_name]['EventDetails'].append(event_detail)

    def lookup_events(self, start_time, end_time, event_source="iam.amazonaws.com"):
        next_token = None
        events_obj = {}
        lookup_attributes = [{'AttributeKey': 'EventSource', 'AttributeValue': event_source}]
        while True:
            if next_token is None:
                output = self.cl_client.lookup_events(
                        StartTime=start_time,
                        EndTime=end_time,
                        MaxResults=50,
                        LookupAttributes=lookup_attributes)
            else:
                output = self.cl_client.lookup_events(
                        StartTime=start_time,
                        EndTime=end_time,
                        MaxResults=50,
                        LookupAttributes=lookup_attributes,
                        NextToken=next_token)
            self.parse_events(events_obj, output['Events'])

            if 'NextToken' in output:
                print("Next token: ", output['NextToken'])
                next_token = output['NextToken']
            else:
                break

        for event in events_obj:
            print("Event: ", event, "   Count: ", events_obj[event]['Count'])



def main():
    # Parse Arguments.
    if len(sys.argv) <= 3:
        print("Not enough arguments")
        print("Usage: ./cloudtrail_test.py <account-id> <role to assume> <region>")
        print("Example: ./cloudtrail_test.py 11111111111 AdminRole us-west-2")
        return

    account_id = sys.argv[1]
    role = sys.argv[2]
    region = sys.argv[3]
    cloudtrail_helper = CloudTrailHelper(account_id, role, region)

    # Lookup events
    start_time = datetime.datetime(2019, 7, 8, 10, 9)
    end_time = datetime.datetime(2019, 7, 8, 10, 16)
    event_source = "iam.amazonaws.com"

    cloudtrail_helper.lookup_events(start_time, end_time, event_source=event_source)



if __name__ == "__main__":
    main()
