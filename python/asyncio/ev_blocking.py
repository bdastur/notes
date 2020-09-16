#!/usr/bin/env python
# -*- coding: utf-8 -*-



import asyncio
import concurrent.futures
import time
import boto3


def get_instances():
    print("Get instances...")
    session = boto3.Session(profile_name="dev1", region_name="us-west-2")
    ec2_client = session.client("ec2")
    data = ec2_client.describe_instances()
    print("Get instances done")
    return data

def get_volumes():
    print("Get Volumes..")
    session = boto3.Session(profile_name="dev1", region_name="us-west-2")
    ec2_client = session.client("ec2")
    data = ec2_client.describe_volumes()
    print("Get volumes done")
    return data

def blocking_task(id, delay):
    print("Blocking task-", id)
    time.sleep(delay)
    print("Blockingg task-%s Done" % id)


async def non_blocking(executor, id_suffix):
    loop = asyncio.get_running_loop()
    print("Non Blocking operation")

    print("Callin blockin..")
    loop.run_in_executor(executor, blocking_task, "1-%s" % id_suffix ,3)
    print("Calling blocking")
    loop.run_in_executor(executor, blocking_task, "2-%s" % id_suffix, 4)
    print("Here done!")

    if executor:
        executor.shutdown()

async def non_blocking_aws(executor, func):
    print("Non blocking aws: ", func)
    loop = asyncio.get_running_loop()
    data = loop.run_in_executor(executor, func)
    print(data)


async def main():
    # Using the default loop's executor.
    await non_blocking(None, "local")

    # Using a custom threadpool executor
    executor = concurrent.futures.ThreadPoolExecutor(max_workers=3)
    await non_blocking(executor, "thread")

    # Using custom process pool executor
    executor = concurrent.futures.ProcessPoolExecutor(max_workers=3)
    await non_blocking(executor, "process")

    # call get instances.
    await non_blocking_aws(None, get_instances)

    await non_blocking_aws(None, get_volumes)



if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    print("Main EV Loop Complete")


