# AWS Identity and Access Management

## Useful Links:

* [AWS Reinvent: Become an IAM Policy Master](https://www.youtube.com/watch?v=YQsK4MtsELU)
* [AWS Reinvent: Getting started with AWS identity](https://www.youtube.com/watch?v=Zvz-qYYhvMk)
* [IAM JSON policy reference](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies.html)
* [Actions, Resources & Condition keys for AWS Services](https://docs.aws.amazon.com/service-authorization/latest/reference/reference_policies_actions-resources-contextkeys.html)
* [Access policy types](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html#access_policy-types)


## Policy Types:

*Identity-based policies*
* Managed and inline policies that can be attached to IAM entities
  (users, groups, roles)

*Resource-based policies*
* Inline policies attached to resources, like S3, KMS, etc.
* Requires a Principal. Principal can be in the same or different account.

*Permission boundaries*
* A managed policy used as a permissions boundary for an IAM entity (user or role).
* This policy defines the maximum permissions that the identity-based policies can
  grant to an entity, but does not grant permissions.
* Resource-based policies that specify the user or role as the principal
  are not limited by the permissions boundary.
* An explicit deny in any of these policies overrides the allow.

*Organizations SCPs*
* AWS Organizations service control policy (SCP) define the maximum permissions
  for the account members of an organization or organizational unit.
* SCPs limit permissions  that identity-based policies or resource-based
  policies grant to entities within the account, but do not grant permissions.

*Access control lists*
* ACLS control which principals in other accounts can access the resource to
  which the ACL is attched.
* ACLs are similar to resource-based policies.
* ACLS are cross-account permission policies that grant permissions to specified
  principal.
* ACLs cannot grant permissions to entities within the same account.

*Session policies*
* Pass advanced session policies when you use the AWS CLI or API to assume a
  role or a federated user.
* Session policies limit the permissions that the role or user's identity-basedd
  policies grant to the session.
* Session policies limit permissions for a created session, but do  not grant
  permissions.


### How to generate IAM credentials report.
```
#!/bin/bash
aws iam generate-credential-report  --profile core-services-prod
aws iam get-credential-report \
    --query Content --output text \
    --profile core-services-dev | base64 -D

```

