package aws

import (
	"fmt"
	"testing"
)

/*
 * Example run: go test --role "arn:aws:iam::4xxxx9:role/SSOxxRole" --bucketname us-xxxxate
 */

//var ssoRole = flag.String("role", "", "SSO Role in case if you are using it to assume")
//var bucketname = flag.String("bucketname", "", "Bucket name to operate on")

func TestIAMClientGet(t *testing.T) {
	fmt.Println("Testing IAM Client!", *ssoRole)
	if *ssoRole == "" {
		fmt.Println("ssoRole is not set!")
		return
	}

	iamsvc := GetIAMClient(*ssoRole, "us-west-2", "okta2aws")
	if iamsvc == nil {
		t.Errorf("Failed to create a IAM session")
	}
}

func TestIAMListRoles(t *testing.T) {
	iamsvc := GetIAMClient(*ssoRole, "us-west-2", "okta2aws")

	roles := GetIAMRoles(iamsvc)
	if roles == nil {
		t.Errorf("Could not get IAM Roles")
	}

}
