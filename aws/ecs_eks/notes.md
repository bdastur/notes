

## Useful Links

* [Trivy - container image scanner](https://github.com/aquasecurity/trivy)



## ECS Security:

*Image Security*

## How to run trivy for image scanning:

Here we can directly run the trivy container, pointing it to another image.

```
aws/ecs %~> docker run aquasec/trivy image mcp/aws-terraform

```

## How to add a USER directive to the container

```
# Create a custom user with UID 1001 and GID 1001
    RUN groupadd -g 1001 appgroup && \
        useradd -m -u 1001 -g appgroup appuser

```

* With ECS on EC2 you are allowed to run the container in priviledged mode. If you 
  want to block that, set environment variable for ECS container agent 
  `ECS_DISABLE_PRIVILEGED = true`

* AWS ECS Fargate does not allow you to run your containers in privileged mode.

* Nothing should be in your image, which is not required.

## How to create a multistage Dockerfile.

* Using Multistage Dockerfile, you can create smaller more secure images ensuring
  you only package libraries and components you absoluate need in the image, reducing
  the threat vector.

-> In the example below, in stage 1 we build a go binary. We use golang:1.22 as
   the base image.
-> In the second start with start with distroless image and then copy the built 
   binary in this container.

```
# Stage 1: Build the application
FROM golang:1.22 AS builder
WORKDIR /app
COPY /app .
RUN go mod init myapp

 
#RUN CGO_ENABLED=0 GOARCH=arm64 GOOS=darwin go build -a -installsuffix cgo -o myapp .
RUN go build -a -installsuffix cgo -o myapp .
RUN ls -l /
RUN ls -l /app
RUN echo "End"

# Stage 2: Create the distroless image
FROM gcr.io/distroless/static-debian12
RUN ls -l /
COPY  --from=builder /app/myapp myapp
USER nonroot:nonroot
ENTRYPOINT ["./myapp"]
```


## How to run Linting on Dockerfile


----------------------------------------------------------------------------


## How to: Create an ECS cluster.

An example of creating an ECS cluster. This command creates a cluster with
container insigns enabled, capacity providers, tags.


```
aws ecs create-cluster \
    --cluster-name testcluster-1 \
    --settings name=containerInsights,value=enhanced
    --capacity-providers FARGATE_SPOT FARGATE \
    --default-capacity-provider-strategy \
        capacityProvider=FARGATE_SPOT,weight=1,base=1 \
    --tags key=Owner,value=bdastur  key=Environment,value=Production \
    --profile brd3 --region us-east-1
```


## How to: Create a task definition.

NOTE: You will need to create the log group "/ecs/my-web-app" that is defined
in the logConfiguration, it does not automatically create it.

You also need to specify the task-role-arn for logs to stream from the container
to cloudwatch.

```
aws ecs register-task-definition \
    --family simple-web-app \
    --task-role-arn arn:aws:iam::168442441230:role/ecsTaskExecutionRole \
    --execution-role-arn arn:aws:iam::168442441230:role/ecsTaskExecutionRole \
    --requires-compatibilities FARGATE \
    --network-mode awsvpc \
    --cpu 256 \
    --memory 512 \
    --container-definitions '[
        {
            "name": "web-app",
            "image": "nginx:latest",
            "privileged": false,
            "portMappings": [
                {
                    "containerPort": 80,
                    "protocol": "tcp"
                }
            ],
            "essential": true,
            "environment": [
                {
                    "name": "ENV_VARIABLE",
                    "value": "production"
                }
            ],
            "logConfiguration": {
                "logDriver": "awslogs",
                "options": {
                    "awslogs-group": "/ecs/my-web-app",
                    "awslogs-region": "us-east-1",
                    "awslogs-stream-prefix": "ecs"
                }
            }
        }
    ]' \
    --profile brd3 --region us-east-1


```


## How to: create an ECS service.


```
aws ecs create-service \
    --cluster testcluster-1 \
    --service-name simple-web-service \
    --task-definition simple-web-app:1 \
    --desired-count 2 \
    --launch-type FARGATE \
    --network-configuration "awsvpcConfiguration={
        subnets=[subnet-0096155d8f8dd6a9f, subnet-0bdf267741a746125],
        securityGroups=[sg-0164b1714b5e9be4d],
        assignPublicIp=ENABLED
    }" \
    --profile brd3 --region us-east-1
```

## How to update an ECS service

```

aws ecs update-service \
    --cluster testcluster-1 \
    --service simple-web-service \
    --task-definition simple-web-app:2 \
    --desired-count 4 \
    --network-configuration "awsvpcConfiguration={
        subnets=[subnet-0096155d8f8dd6a9f, subnet-0bdf267741a746125],
        securityGroups=[sg-0164b1714b5e9be4d],
        assignPublicIp=ENABLED
    }" \
    --deployment-configuration '{
        "strategy": "ROLLING",
        "maximumPercent": 200,
        "minimumHealthyPercent": 100,
        "deploymentCircuitBreaker": {"enable": true, "rollback": true}
    }' \
    --force-new-deployment \
    --profile brd3 --region us-east-1

```

## How to have loadbalancers for the ECS service.



```
aws ecs update-service \
    --cluster testcluster-1 \
    --service simple-web-service \
    --task-definition simple-web-app:2 \
    --desired-count 4 \
    --network-configuration "awsvpcConfiguration={
        subnets=[subnet-0096155d8f8dd6a9f, subnet-0bdf267741a746125],
        securityGroups=[sg-0164b1714b5e9be4d],
        assignPublicIp=ENABLED
    }" \
    --deployment-configuration '{
        "strategy": "ROLLING",
        "maximumPercent": 200,
        "minimumHealthyPercent": 100,
        "deploymentCircuitBreaker": {"enable": true, "rollback": true}
    }' \
    --load-balancers '[{
        "targetGroupArn": "arn:aws:elasticloadbalancing:us-east-1:168442441230:targetgroup/simple-web-app-targetgroup/b38a00b70c48e579",
        "containerName": "web-app",
        "containerPort": 80
    }]' \
    --force-new-deployment \
    --profile brd3 --region us-east-1

```



