package aws

import (
	"bytes"
	"fmt"
	"io"
	"io/ioutil"
	"strings"

	"github.com/aws/aws-sdk-go/aws"
	"github.com/aws/aws-sdk-go/aws/credentials/stscreds"
	"github.com/aws/aws-sdk-go/aws/session"
	"github.com/aws/aws-sdk-go/service/s3"
)

const (
	ERR_OK               = 0
	ERR_INVALID_PARAMS   = 1
	ERR_OPERATION_FAILED = 2
)

func GetS3Client(roleArn string, region string, profile string) *s3.S3 {
	sess := session.Must(session.NewSessionWithOptions(session.Options{
		Config: aws.Config{Region: aws.String(region)}, Profile: profile,
	}))

	creds := stscreds.NewCredentials(sess, roleArn)
	s3svc := s3.New(sess, &aws.Config{Credentials: creds})

	return s3svc
}

func UploadFile(s3svc *s3.S3,
	bucketname string,
	key string,
	filepath string) int {

	// upload object.
	data, err := ioutil.ReadFile(filepath)
	if err != nil {
		fmt.Println("Failed to read ", filepath)
		return ERR_OPERATION_FAILED
	}

	input := &s3.PutObjectInput{
		Body:                 aws.ReadSeekCloser(strings.NewReader(string(data))),
		Bucket:               aws.String(bucketname),
		Key:                  aws.String(key),
		ServerSideEncryption: aws.String("AES256"),
	}

	result, err := s3svc.PutObject(input)
	if err != nil {
		fmt.Println(err.Error())
		return ERR_OPERATION_FAILED
	} else {
		fmt.Println("Upload complete!", result)
		return ERR_OK
	}
}

func DownloadFile(s3svc *s3.S3, bucketname string, key string) {
	fmt.Printf("Download File %s", key)

	input := &s3.GetObjectInput{
		Bucket: aws.String(bucketname),
		Key:    aws.String(key),
	}

	result, err := s3svc.GetObject(input)
	if err != nil {
		fmt.Println("Error: ", err)
		return
	}

	fmt.Println("Result: ", result)
	buf := bytes.NewBuffer(nil)
	bufresult, err := io.Copy(buf, result.Body)
	if err != nil {
		fmt.Println("Failed operation ", err)
		return
	}
	fmt.Println("Result: ", bufresult)

}

func DeleteFile(s3svc *s3.S3, bucketname string, key string) error {

	params := &s3.DeleteObjectInput{
		Bucket: aws.String(bucketname),
		Key:    aws.String(key),
	}

	result, err := s3svc.DeleteObject(params)
	if err != nil {
		fmt.Println("Failed to delete ", key, " ERR: ", err)
		return err
	}
	fmt.Println("Result: ", result)
	return err
}

func ListBuckets(roleArn string, bucketname string) {
	fmt.Println("List buckets")
	// Specify profile for config and region for requests
	sess := session.Must(session.NewSessionWithOptions(session.Options{
		Config:  aws.Config{Region: aws.String("us-west-2")},
		Profile: "okta2aws",
	}))
	creds := stscreds.NewCredentials(sess, roleArn)

	s3svc := s3.New(sess, &aws.Config{Credentials: creds})
	result, err := s3svc.ListBuckets(nil)
	if err != nil {
		fmt.Println("Failed to list s3 buckets.", err)
	}

	for _, b := range result.Buckets {
		fmt.Printf("Bucket %s created on %s \n ",
			aws.StringValue(b.Name),
			aws.TimeValue(b.CreationDate))

		bucketname := aws.String(*b.Name)

		// Get Bucket location.
		input := &s3.GetBucketLocationInput{
			Bucket: bucketname,
		}
		result, err := s3svc.GetBucketLocation(input)
		if err != nil {
			fmt.Println(err.Error())
		}
		fmt.Printf("Result: %s \n", aws.StringValue(result.LocationConstraint))

		// Get Bucket policy
		policyinput := &s3.GetBucketPolicyInput{
			Bucket: bucketname,
		}

		policyresult, err := s3svc.GetBucketPolicy(policyinput)
		if err != nil {
			fmt.Println(err.Error())
		} else {
			fmt.Printf("Policy result: %s", policyresult)
		}
	}

	// upload object.
	input := &s3.PutObjectInput{
		Body:                 aws.ReadSeekCloser(strings.NewReader("/tmp/upload.txt")),
		Bucket:               aws.String(bucketname),
		Key:                  aws.String("TESTFOLDER/testupload.txt"),
		ServerSideEncryption: aws.String("AES256"),
	}

	putresult, err := s3svc.PutObject(input)
	if err != nil {
		fmt.Println(err.Error())
	} else {
		fmt.Println("Upload complete!", putresult)

	}

}
