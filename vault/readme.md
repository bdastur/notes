# Hashicorp Vaults
Notes on Hashicorp vault.

## Steps to configure AWS Backend:

Hashicorp’s Vault can generate secrets dynamically with AWS backend.
Which means the API keys get generated when needed and can be revoked
when done, without a user having to request them,  worrying about saving
them and all the other issues with maintain secrets.

Here are the steps to use AWS Backend to generate secrets.
Since I only tested it with CLI I am only documenting CLI method, but I will update the notes later for API access.


1. Mounting the AWS Backend:
Vault supports multiple backends, one of them is an AWS backend.
First step is to mount the AWS backend.
```
# vault mount aws
```

To list all the backends mounted:

```
# vault mounts
Path        Type       Accessor            Plugin  Default TTL  Max TTL  Force No Cache  Replication Behavior  Description
aws/        aws        aws_430c7150        n/a     system       system   false           replicated
cubbyhole/  cubbyhole  cubbyhole_d4ed2c7d  n/a     n/a          n/a      false           local                 per-token private secret storage
secret/     kv         kv_3a09af8f         n/a     system       system   false           replicated            key/value secret storage
sys/        system     system_b7d54821     n/a     n/a          n/a      false           replicated            system endpoints used for control, policy and debugging

```
2. Create an IAM User
We need API Keys that can be used by Vault to generate API keys on fly.
For that we need to create an IAM user. The user should have permissions to
create users and create inline policies.

Here is the policy that you can attach to this user.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "AllowIAMUserOperationswithPrefix",
            "Action": [
                "iam:Createuser",
                "iam:CreateAccessKey",
                "iam:DeleteAccessKey",
                "iam:DetachUserPolicy",
                "iam:DeleteUser"
            ],
            "Effect": "Allow",
            "Resource": [
                "arn:aws:iam::333333333333:user/vault-root-*"
            ]
        },
        {
            "Sid": "AllowPutUserpolicy",
            "Action": [
                "iam:PutUserPolicy",
                "iam:DeleteUserPolicy"
            ],
            "Effect": "Allow",
            "Resource": [
                "*"
            ]
        },
    ]
}
```

3. Write the secrets to Vault.

```
# vault write aws/config/root access_key=AKKKKKKKKKKKKKR4 \ secret_key=xnxjxjxjxjxjxjxjxjxjxjxjxjxjxp+
Success! Data written to: aws/config/root
```

Note that these keys cannot be retrieved from Vault. You cannot read them back.
```
# vault read aws/config/root
Error reading aws/config/root: Error making API request.

URL: GET http://127.0.0.1:8200/v1/aws/config/root
Code: 405. Errors:

* 1 error occurred:

* unsupported operation
```


4. You can create different policies for what calls Roles (which are different
   than IAM Roles). The policy is what gets applied to the IAM user that
    vault creates, which lets the user perform various AWS operations.

Here I have a file called policy.json:
```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "Stmt1426528957000",
      "Effect": "Allow",
      "Action": [
        "ec2:*"
      ],
      "Resource": [
        "*"
      ]
    }
  ]
}
```

5. Create a aws/roles/<name> to create specific roles (Again, these are not
   AWS Roles but vault specific reference)

Here we are creating a vault role called deploy.
```
# vault write aws/roles/deploy policy=@policy.json
Success! Data written to: aws/roles/deploy
```


6. Finally we come to the step of creating credentials.
   Use the vault read aws/creds/<name>

This action creates a iam user vault-* in aws.

```
# vault read aws/creds/deploy
Key             Value
---             -----
lease_id        aws/creds/deploy/929e67b9-8f53-a729-4d44-7076833028e0
lease_duration  768h0m0s
lease_renewable true
access_key      AXXXXXXXXXXXXXXXXXXA
secret_key      FxjxjxjxjxjxjxjxjxjxjxjxjxjxJN
security_token  <nil>
```

7. To revoke credentials (this indirectly removes the vault-* iam user from aws)

```
# vault revoke aws/creds/deploy/929e67b9-8f53-a729-4d44-7076833028e0
Success! Revoked the secret with ID 'aws/creds/deploy/929e67b9-8f53-a729-4d44-7076833028e0', if it existed.
```
