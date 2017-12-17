# Kubernetes and Openshift Notes:

## Simple Web application workflow.
Walkthrough of creating a simple web application.


### Code for simple application:

[simple-web-app](https://github.com/bdastur/notes/tree/master/kubernetes/simple-web-app)

### Building and Pushing the image to registry:
```
export REGISTRY=`registry.abc.xyz.com`

docker build --tag=$REGISTRY/alpine:0.1 .
docker push $REGISTRY/alpine:0.1

```

### Openshift/Kubernetes templates:

[simple deployment config](https://github.com/bdastur/notes/tree/master/kubernetes/simple-web-app/deploymentconfig.yaml)

[Example of liveness and readiness probe](https://github.com/bdastur/notes/tree/master/kubernetes/simple-web-app/dc_livenessprobe.yaml)

[Example of mouting secerts](https://github.com/bdastur/notes/tree/master/kubernetes/simple-web-app/dc_withsecrets.yaml)


### Create a new Openshift project/namespace for a new app.
We will first create a new namespace/project with openshift client CLI.


```
$ oc new-project pyapp --description="A simple web application" --display-name="pyapp"

$ oc project pyapp
Already on project "pyapp" on server "https://abc.xyz.aws.acme.net:443".
```


### Create a new deployment config.
A simple deployment configuration looks like this.
```
---
  kind: "Template"
  apiVersion: "v1"
  metadata:
    name: "pyapp"
  objects:
    -
      kind: "DeploymentConfig"
      apiVersion: "v1"
      metadata:
        name: "pyapp"
        labels:
          template: "pyapp"
          name: "pyapp"
      spec:
        strategy:
          type: "Recreate"
        triggers:
          -
            type: "ConfigChange"
        replicas: 1
        selector:
          name: "pyapp"
        template:
          metadata:
            labels:
              name: "pyapp"
          spec:
            containers:
              -
                name: "pyapp-container"
                image: "${image_url}"
                ports:
                  - containerPort: 5001
                resources:
                  requests:
                    memory: "2048Mi"
                    cpu: "250m"
                  limits:
                    memory: "2048Mi"
                    cpu: "250m"
                env:
            volumes:
  parameters:
    -
      name: "image_url"
      value: "registry.abc.acme.com/alpine:0.1"

```

To create a new deployment config.
```

$ oc create -f deploymentconfig.yaml

```

To edit deployment config:
```
$ oc process -f deploymentconfig.yaml | oc apply -f -

```

To get all resources:
```
$ oc get all
```


### Liveness and Readiness probes:

[Kubernetes.io: liveness-readiness-probes](https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-probes/)

```
# Liveness probe.
livenessProbe:
  exec:
    command:
      - cat
      - /tmp/healthy
  initialDelaySeconds: 25
  periodSeconds: 10 
  successThreshold: 1
  failureThreshold: 3

# Readiness probe.
readinessProbe:
  exec:
    command:
      - cat
      - /tmp/ready
  initialDelaySeconds: 25
  periodSeconds: 10
  failureThreshold: 1

```

### Creating Secrets:

[Kubernets.io: secrets](https://kubernetes.io/docs/concepts/configuration/secret/)

```
$ export MY_SECRET="testing"

$ oc create secret generic my-secret --from-literal=mysecret=$MY_SECRET
secret "my-secret" created
```

#### Decoding a secret:
```
$ oc get secrets my-secret -o yaml
apiVersion: v1
data:
  mysecret: dGVzdGluZw==
kind: Secret
metadata:
  creationTimestamp: 2017-12-16T14:52:07Z
  name: my-secret
  namespace: pyapp
  resourceVersion: "31531077"
  selfLink: /api/v1/namespaces/pyapp/secrets/my-secret
  uid: b002bb79-e270-11e7-bce0-126bbe2a1452
type: Opaque

$ echo dGVzdGluZw== | base64 --decode
testing
```


