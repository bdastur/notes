package aws

import (
	"fmt"

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

func GetIAMRoles(iamsvc *iam.IAM) *iam.ListRolesOutput {
	input := &iam.ListRolesInput{}

	result, err := iamsvc.ListRoles(input)
	if err != nil {
		fmt.Println("Failed to list Roles.", err)
		return nil
	}

	markerstring := result.Marker

	for {
		if *result.IsTruncated != true {
			break
		}

		newinput := &iam.ListRolesInput{
			Marker: markerstring,
		}
		result, err = iamsvc.ListRoles(newinput)
		if err != nil {
			fmt.Println("Failed to return role")
		}
		markerstring = result.Marker
	}

	return result

}

func GetAccountSummary(iamsvc *iam.IAM) {
	// Get account summary
	accountsummaryinput := &iam.GetAccountSummaryInput{}
	summary, err := iamsvc.GetAccountSummary(accountsummaryinput)
	if err != nil {
		fmt.Println("Failed to get account summary!")
	}
	fmt.Println("Account summary: ", summary)
}
