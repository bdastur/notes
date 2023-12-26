#!/usr/bin/env python
# -*- coding: utf-8 -*-


import boto3
import botocore
import random
import string
import sys


def getBotoClient(region, profile, service):
    try:
        session = boto3.Session(region_name=region, profile_name=profile)
        client = session.client(service)
    except botocore.exceptions.ProfileNotFound as err:
        return None, err

    return client, None


def sendMessage(region, profile, queueUrl, **msgOptions):
    try:
        messageBody = msgOptions["messageBody"]
        messageAttributes = msgOptions["attributes"]
    except KeyError as err:
        print("Invalid msg options [%s]" % err)
        return

    client, errMsg = getBotoClient(region, profile, "sqs")
    if client is None:
        print("Failed to get boto client [%s]" % errMsg)
        return

    ret = client.send_message(QueueUrl=queueUrl,
                              MessageBody=messageBody,
                              MessageAttributes=messageAttributes)
    print(ret)

def sendMessageTest():
    region = "us-east-1"
    profile = "dev"
    queueUrl = "https://sqs.us-east-1.amazonaws.com/111111111111/testqueue1"

    msgCount = 1
    for count in range(msgCount):
        print(count)
        msg = "".join(random.choices(string.ascii_uppercase + string.digits, k=40))
        print(msg)
        id = str(random.randint(1000, 999999))

        msgOptions = {
            "messageBody": "This is a test message One",
            "attributes": {
                "type": {
                    "StringValue": msg,
                    "DataType": "String"
                },
                "user": {
                    "StringValue": "bdastur",
                    "DataType": "String"
                },
                "Id": {
                    "StringValue": id,
                    "DataType": "Number"
                }
            }
        }
        sendMessage(region, profile, queueUrl, **msgOptions)

def receiveMessage(region, profile, queueUrl):
    client, errMsg = getBotoClient(region, profile, "sqs")
    if client is None:
        print("Failed to get boto client [%s]" % errMsg)
        return
    visibilityTimeout = 10 # 10 seconds.
    maxMessages = 1 # MaxNumberofMessages to return.
    waitTimeSeconds = 10 # Long polling wait time.

    print("Receiving Msg [visibility timeout: %d], [max msgs: %d], [wait time: %d]" % (visibilityTimeout, maxMessages, waitTimeSeconds))
    ret = client.receive_message(QueueUrl=queueUrl,
                                 AttributeNames=["ALL"],
                                 MaxNumberOfMessages=maxMessages,
                                 VisibilityTimeout=visibilityTimeout,
                                 WaitTimeSeconds=waitTimeSeconds)
    return ret


def receiveMessageTest():
    region = "us-east-1"
    profile = "dev"
    queueUrl = "https://sqs.us-east-1.amazonaws.com/111111111111/testqueue1"

    ret = receiveMessage(region, profile, queueUrl)
    print("Recv msg: ", ret)
    

def main():

    if len(sys.argv) != 2:
        print("Usage ./sqs_test.py [send|recv]")
        sys.exit(0)

    operation = sys.argv[1]
    print("Operation: ", operation)

    if operation == "send":
        # Send message.
        sendMessageTest()
    else:
        receiveMessageTest()


if __name__ == '__main__':
    main()



