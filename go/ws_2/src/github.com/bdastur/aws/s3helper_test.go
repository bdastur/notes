package aws

import (
	"flag"
	"fmt"
	"testing"
)
/*
 * Example run: go test --role "arn:aws:iam::4xxxx9:role/SSOxxRole" --bucketname us-xxxxate

var ssoRole = flag.String("role", "", "SSO Role in case if you are using it to assume")
var bucketname = flag.String("bucketname", "", "Bucket name to operate on")

func TestS3Basic(t *testing.T) {
	fmt.Println("Testing S3!", *ssoRole)
	if *ssoRole == "" {
		fmt.Println("ssoRole is not set!")
		return
	}

	s3svc := GetS3Client(*ssoRole, "us-west-2", "okta2aws")

	if s3svc == nil {
		t.Errorf("Failed to create a S3 session!")
	}

}

func TestS3PutObject(t *testing.T) {
	fmt.Println("Testing Put Object")
	s3svc := GetS3Client(*ssoRole, "us-west-2", "okta2aws")
	UploadFile(s3svc, *bucketname,
		"TESTFOLDER/testfile.txt",
		"/tmp/upload.txt")

}

func TestS3GetObject(t *testing.T) {
	fmt.Println("Testing Get Object")
}
