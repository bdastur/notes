#!/usr/bin/env python
# -*- coding: utf-8 -*-

import boto3
import click


@click.group()
def cli():
    pass


@cli.group('volumes')
def volumes():
    """Volume operations"""
    pass


@volumes.command()
@click.option("--az", type=str, default="us-west-2a", help="Availability zone", 
              show_default=True, required=True)
@click.option("--type", type=click.Choice(["io1", "io2", "gp2", "gp3"]), 
              multiple=False, help="Volume type", required=True)
@click.option("--size", type=str, help="Volume size in GiB", required=True)
def create_volume(az, type, size):
    print("Az: %s, type: %s, size: %s" % (az, type, size))
    size = int(size)
    tags = [
        {
            "ResourceType": "volume",
            "Tags": [
                {
                    "Key": "Name",
                    "Value": "TestVolume"
                },
                {
                    "Key": "Owner",
                    "Value": "behzad.dastur"
                }
            ]
        }
    ]
    # test only, hardcoded profile name and region.
    session = boto3.Session(profile_name="dev1", region_name="us-west-2")
    client = session.client("ec2")
    try:
        ret = client.create_volume(AvailabilityZone=az, Encrypted=True, 
                                   Size=size, VolumeType=type, TagSpecifications=tags)
    except botocore.exceptions.ClientError as err:
        print("Failed: Volume creation [%s]" %  err)
        return

    volumeId = ret["VolumeId"]

    print("Volume Create [%s]", volumeId)


def create_snapshot():
    print("Create snapshot")


def main():
    cli.add_command(volumes)
    cli()


if __name__ == '__main__':
    main()
