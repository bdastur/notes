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
		"arn:aws:iam::4xxxx9:role/SoeRolee")

	s3svc := s3.New(sess, &aws.Config{Credentials: creds})
	result, err := s3svc.ListBuckets(nil)
	if err != nil {
		fmt.Println("Failed to list s3 buckets.", err)
	}

	for _, b := range result.Buckets {
		fmt.Printf("* %s created on %s \n ",
			aws.StringValue(b.Name),
			aws.TimeValue(b.CreationDate))
	}

}
