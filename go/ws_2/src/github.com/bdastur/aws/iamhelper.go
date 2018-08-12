package aws

import (
	"github.com/aws/aws-sdk-go/aws"
	"github.com/aws/aws-sdk-go/aws/credentials/stscreds"
	"github.com/aws/aws-sdk-go/aws/session"
	"github.com/aws/aws-sdk-go/service/iam"
)

func GetIAMClient(roleArn string, region string, profile string) *iam.IAM {
	sess := session.Must(session.NewSessionWithOptions(session.Options{
		Config: aws.Config{Region: aws.String(region)}, Profile: profile,
	}))

	creds := stscreds.NewCredentials(sess, roleArn)
	iamsvc := iam.New(sess, &aws.Config{Credentials: creds})

	return iamsvc
}
