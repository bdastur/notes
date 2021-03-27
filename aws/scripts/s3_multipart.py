#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import boto3
import botocore

"""
A very simple example of using boto3 client APIs for multipart upload.
Some key things to consider when performing the multipart upload.
1. ALways make sure to either complete or abort the upload in case of failure
   The uploaded chunks do not get deleted automatically and they start
   accumulating and costing a lot.
2. Set a lifecycle policy on the bucket to clean out chunks after x no of days
3. The minimum size of a single chunk is 5MB except the last chunk, any licenses
   than that and you will get a boto exception of EntityTooSmall.
"""


def multipart_upload(s3client,
                     bucket_name,
                     filename,
                     key):
    """
    Upload a large file using multipart upload.

    Three distinct steps:
    1. Initiate a multipart upload. Get the upload id which will be used in
       subsequent steps.
    2. Start uploading chunks (pass the upload id to let it know ID
       of the initiated upload), also keep track of the parts . You will use that
       to complete the upload.
    3. Complete the upload. (pass the list of parts (a dict of eTag and part no)
        )
    """
    # Initiate multipart upload.
    try:
        response = s3client.create_multipart_upload(
            Bucket=bucket_name,
            Key=key,
            ACL='private',
            StorageClass='STANDARD')
    except botocore.exceptions.ClientError as err:
        print "Exception occured initiating multipart upload: %s" % err
        sys.exit()

    upload_id = response['UploadId']

    parts = []
    part_no = 1

    # Upload individual Chunks.
    with open(filename, "rb") as fhandle:
        # 5MB is the minimum size of each part you upload.
        chunk_size = 5 * 1024 * 1024
        while True:
            chunk = fhandle.read(chunk_size)
            if len(chunk) == 0:
                print "Done!"
                break

            # upload chunks
            try:
                response = s3client.upload_part(Bucket=bucket_name,
                                                Body=chunk,
                                                Key=key,
                                                PartNumber=part_no,
                                                UploadId=upload_id)
            except botocore.exceptions.ParamValidationError as err:
                print "Upload part failed [%s]" % err
                s3client.abort_multipart_upload(Bucket=bucket_name,
                                                Key="test.iso",
                                                UploadId=upload_id)
                sys.exit()
            except botocore.errorfactory.NoSuchUpload as err:
                print "No such upload"
                s3client.abort_multipart_upload(Bucket=bucket_name,
                                                Key="test.iso",
                                                UploadId=upload_id)
                sys.exit()

            parts.append({'ETag': response['ETag'], 'PartNumber': part_no})
            part_no += 1

    print "Total Chunks uploaded: ", len(parts)
    # Complete the upload.
    response = s3client.complete_multipart_upload(Bucket=bucket_name,
                                                  Key="test.iso",
                                                  MultipartUpload={
                                                      'Parts': parts
                                                  },
                                                  UploadId=upload_id)




def main():
    profile_name = "default"
    try:
        session = boto3.Session(profile_name=profile_name,
                                region_name="eu-central-1")
        s3client = session.client('s3')
    except botocore.exceptions.ProfileNotFound:
        print "Profile %s not found" % profile_name
        sys.exit()

    multipart_upload(s3client, 'simple-testbucket101',
                     'test.iso', 'test.iso')





if __name__ == '__main__':
    main()
