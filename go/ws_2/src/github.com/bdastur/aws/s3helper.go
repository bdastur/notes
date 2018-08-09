package aws

import (
	"fmt"

	"github.com/aws/aws-sdk-go/aws"
	"github.com/aws/aws-sdk-go/aws/credentials/stscreds"
	"github.com/aws/aws-sdk-go/aws/session"
	"github.com/aws/aws-sdk-go/service/s3"
)

func ListBuckets() {
	fmt.Println("List buckets")
	// Specify profile for config and region for requests
	sess := session.Must(session.NewSessionWithOptions(session.Options{
		Config:  aws.Config{Region: aws.String("us-west-2")},
		Profile: "okta2aws",
	}))
	creds := stscreds.NewCredentials(sess,
		"arn:aws:iam::461168169469:role/SSOAdmin1Role")

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
		fmt.Printf("Result: %s", aws.StringValue(result.LocationConstraint))

	}

}
