#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import unittest
import boto3
import botocore


class SQS(unittest.TestCase):
    def setUp(self):
        env = os.environ.get('PROFILE_NAME', 'default')
        if env == "default":
            print "Using Default profile"
        else:
            print "Using %s profile" % env

        try:
            session = boto3.Session(profile_name=env,
                                    region_name="us-east-1")
        except botocore.exceptions.ProfileNotFound:
            print "Profile %s not found!" % env
            self.sqsclient = None
            return

        self.sqsclient = session.client('sqs')
        self.queue_name = "brd-queue"

    def test_create_standard_queue(self):
        print "basic"
        attributes = {
            'DelaySeconds': '5',
            'MaximumMessageSize': '1024',
            'MessageRetentionPeriod': '60'
        }

        # Create a standard queue.
        response = self.sqsclient.create_queue(
            QueueName=self.queue_name,
            Attributes=attributes
        )
        print "response: ", response

        # Get Queue URL.
        response = self.sqsclient.get_queue_url(
            QueueName=self.queue_name
        )
        print "response: ", response['QueueUrl']
        queue_url = response['QueueUrl']

        # Delete queue.
        response = self.sqsclient.delete_queue(
            QueueUrl=queue_url
        )

    def test_send_message(self):
        # Create a standard queue.
        queue_name = "brd-testqueue-1"
        response = self.sqsclient.create_queue(
            QueueName=queue_name
        )
        print "Response: ", response

        queue_url = response['QueueUrl']
        # Send message.
        response = self.sqsclient.send_message(
            QueueUrl=queue_url,
            MessageBody='This is a test message',
            DelaySeconds=1
        )
        print "response for send msg: ", response
        
