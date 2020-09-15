#!/usr/bin/env python
# -*- coding: utf-8 -*-



import asyncio
import concurrent.futures
import time
import boto3


def get_instances():
    print("Get instances...")
    session = boto3.Session(profile_name="workdayscylladev1", region_name="us-west-2")
    ec2_client = session.client("ec2")
    data = ec2_client.describe_instances()
    #print(data)
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


# async def main(loop, executor):
#     print("In async main")
#     data = await loop.run_in_executor(executor, get_instances())
#     print("Got instances")
#     print("Data: ", data)

async def main():
    # Using the default loop's executor.
    await non_blocking(None, "local")

    # Using a custom threadpool executor
    executor = concurrent.futures.ThreadPoolExecutor(max_workers=3)
    await non_blocking(executor, "thread")

    # Using custom process pool executor
    executor = concurrent.futures.ProcessPoolExecutor(max_workers=3)
    await non_blocking(executor, "process")


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    #executor = concurrent.futures.ThreadPoolExecutor(max_workers=4)
    #loop.run_until_complete(main(loop, executor))
    loop.run_until_complete(main())
    #asyncio.run(non_blocking(None))
    print("Here in __main__")


