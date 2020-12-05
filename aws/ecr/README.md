Build the image:
```
docker build --tag ecrtest:0.1 .
```

Get ECR Login Password:
```
aws ecr get-login-password  \
  --region us-west-2 --profile dev1 | docker login --username AWS --password-stdin 1xxxxxxx9.dkr.ecr.us-west-2.amazonaws.com

```

Create a ECR Repository:
```
aws ecr create-repository \
  --repository-name test-repo --image-scanning-configuration scanOnPush=true
```

Tag the image:
```
docker tag ecrtest:0.1 1xxxxxxx9.dkr.ecr.us-west-2.amazonaws.com/test-repo:0.1
```

Push image:
```
docker push 1xxxxxxx9.dkr.ecr.us-west-2.amazonaws.com/test-repo:0.1 
```

