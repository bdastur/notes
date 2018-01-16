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

[Example of secrets in ENV](https://github.com/bdastur/notes/tree/master/kubernetes/simple-web-app/dc_withsecrets_asenv.yaml)


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


## Kubernetes and RBAC 'Role-based Access Control'
[kubernetes.io: RBAC](https://kubernetes.io/docs/admin/authorization/rbac/)

The document details creating Roles, service accounts and role bindings.
We are going to do the following:
1. Create a new Cluster Role.
2. Create a new service account.
3. Create a new Cluster role binding.

This will enable us to use our service role to perform operations for which we 
have given permissions based on the Role.
e
### Create a new Cluster Role:
A cluster role can be used to grant permissions similar to a Role, additionally
it can be used to grant access to cluster scoped resources like nodes, pods etc.

Here is an example of a template to create a Cluster Role with Read-only access
to all resources.

[Cluster Role template](https://github.com/bdastur/notes/tree/master/kubernetes/cluster_role.yaml)

```
$ oc create -f cluster_role.yaml

```

### Create a service account.

Example template for creating a service account:
[Service account template](https://github.com/bdastur/notes/tree/master/kubernetes/service_account.yaml)

```
$ oc create -f service_account.yaml
```

### Create a Cluster Role binding:t

Example of creating a cluster role binding for our Cluster Role and use our
service account as a subject.

[Cluster Role binding template](https://github.com/bdastur/notes/tree/master/kubernetes/cluster_role_binding.yaml)

```
$ oc create -f cluster_role_binding.yaml
```

### How to login with our service account:

#### Describe our service account:

```
$ oc get serviceaccount readonly-user -o yaml
apiVersion: v1
imagePullSecrets:
- name: readonly-user-dockercfg-w091v
kind: ServiceAccount
metadata:
  creationTimestamp: 2017-12-27T16:12:02Z
  name: readonly-user
  namespace: default
  resourceVersion: "48418189"
  selfLink: /api/v1/namespaces/default/serviceaccounts/readonly-user
  uid: ac57b2f5-eb20-11e7-b02d-0a79a3b169d0
secrets:
- name: readonly-user-dockercfg-w091v
- name: readonly-user-token-cw7n7
```

#### Describe the token:

```
(awsenv)MFD57:web-app behzad_dastur$ oc describe secret readonly-user-token-cw7n7
Name:       readonly-user-token-cw7n7
Namespace:  default
Labels:     <none>
Annotations:    kubernetes.io/service-account.name=readonly-user
        kubernetes.io/service-account.uid=ac57b2f5-eb20-11e7-b02d-0a79a3b169d0

Type:   kubernetes.io/service-account-token

Data
====
ca.crt:     712 bytes
namespace:  7 bytes
token:      eyJhbGciOiJ....._JkFWKmUxdUTWvqbc8kCLmKp3w43WSzdv3dY_BL_OGUf8RO5--Xx0T

``` 

### Login with the token:

```
$ oc login --token=eyJhbGciOiJ...8kCLmKp3w43WSzdv3dY_BL_OGUf8RO5--Xx0T
Logged into "https://acme-kube-dev.us-east-1.acme.dev.aws.acmecorp.net:443" as "system:serviceaccount:default:readonly-user" using the token provided.

```


### Node selectors.
https://docs.openshift.com/container-platform/3.4/admin_guide/managing_projects.html#setting-the-project-wide-node-selector

```
# Get labels for nodes.
oc get nodes --show-labels

# Edit the namespace to add node selector.
oc edit namespace <namespacename>

openshift.io/node-selector: tier=guaranteed

```





