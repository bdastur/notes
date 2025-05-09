# Kubernetes and Openshift, gcloud Notes:

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

### Useful reading:

* [Almighty-pause-container](https://www.ianlewis.org/en/almighty-pause-container)
* [What are Kubernetes Pods](https://www.ianlewis.org/en/what-are-kubernetes-pods-anyway)
* [Deep Dive into Kubeernetes controllers](https://engineering.bitnami.com/articles/a-deep-dive-into-kubernetes-controllers.html)
* [Custom controllers with Python](https://blog.openshift.com/writing-custom-controller-python/)


### Useful tools and projects:
* [Python client library for Kubernetes](https://github.com/kelproject/pykube)
* [Kubernetes webhook autoscaler](https://github.com/wbuchwalter/kubernetes-webhook-autoscaler)
* [Bulk port fowarding of kubernetes services for local development](https://github.com/txn2/kubefwd)
* [A tool for exploring each layer for docker image](https://github.com/wagoodman/dive)
* [Kubernetes operator to automate helm, daemonset, SS & Deployment updates](https://github.com/keel-hq/keel)
* [Multi pod logging for kubernetes](https://github.com/wercker/stern)
* [Multi pod logging for kubernetes - but this one is a simple bash script](https://github.com/johanhaleby/kubetail)
* [Python framework to write Kubernetes Operators](https://github.com/zalando-incubator/kopf)
* [Kubernetes network policy recepies](https://github.com/ahmetb/kubernetes-network-policy-recipes)
* [Troubleshooting networking](https://github.com/nicolaka/netshoot)
* [Web visualization of a cluster](https://github.com/vmware/octant)
* [Kubernetes failure stories](https://k8s.af/)
* [Kubernetes troubleshooting workflow](https://learnk8s.io/troubleshooting-deployments)
* [Kube cost tool](https://github.com/kubecost/cost-model)
* [kube grafiti](https://github.com/HotelsDotCom/kube-graffiti)
* [Dockerfile linter](https://github.com/hadolint/hadolint)
* [Monitor Kubernetes, record history of events and resources](https://github.com/salesforce/sloop)
* [CD.Foundation Projects (Jenkins, Tekton,..)](https://cd.foundation/projects/)
* [Tekton K8s CI/CD](https://github.com/tektoncd)
* [Kubernetes desktop client - visualization](https://docs.infra.app/)
* [Opensource cloud native registry for docker images and helm charts](https://github.com/goharbor/harbor)
* [Kubectl Krew - plugin manager](https://krew.sigs.k8s.io/)
* [Kubernetes essential tools - 2021](https://itnext.io/kubernetes-essential-tools-2021-def12e84c572)
* [Mizu - kubernetes traffic viewer tool](https://up9.com/traffic-viewer-kubernetes)
* [Kubernetes prompt for bash and zsh](https://github.com/jonmosco/kube-ps1)
* [cloud native runtime security tool](https://github.com/falcosecurity/falco)
* [How to structure a kubernetes project](https://www.techopsexamples.com/p/how-to-structure-your-kubernetes-project)

* https://github.com/karmab/samplecontroller
* https://blog.openshift.com/writing-custom-controller-python/
* https://github.com/bazelbuild/rules_k8s
* https://github.com/kubernetes-client/python

### Talks and Other links:
* [Container networking from scratch](https://www.youtube.com/watch?v=6v_BDHIgOY8)
* [Kubecon2018 schedule talks](https://events.linuxfoundation.org/events/kubecon-cloudnativecon-north-america-2018/schedule/)


### Openshift/Kubernetes templates:

* [simple deployment config](https://github.com/bdastur/notes/tree/master/kubernetes/simple-web-app/deploymentconfig.yaml)
* [Example of liveness and readiness probe](https://github.com/bdastur/notes/tree/master/kubernetes/simple-web-app/dc_livenessprobe.yaml)
* [Example of mouting secerts](https://github.com/bdastur/notes/tree/master/kubernetes/simple-web-app/dc_withsecrets.yaml)
* [Example of secrets in ENV](https://github.com/bdastur/notes/tree/master/kubernetes/simple-web-app/dc_withsecrets_asenv.yaml)


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

$ kubectl create -f deploymentconfig.yaml

```

To edit deployment config:
```
$ kubectl process -f deploymentconfig.yaml | kubectl apply -f -

```

To get all resources:
```
$ kubectl get all
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

$ kubectl create secret generic my-secret --from-literal=mysecret=$MY_SECRET
secret "my-secret" created
```

#### Decoding a secret:
```
$ kubectl get secrets my-secret -o yaml
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
[Bitnami blog RBAC](https://docs.bitnami.com/kubernetes/how-to/configure-rbac-in-your-kubernetes-cluster/)
[Using RBAC Authorization](https://kubernetes.io/docs/reference/access-authn-authz/rbac/#role-binding-examples)

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
$ kubectl create -f cluster_role.yaml

```

### Create a service account.

Example template for creating a service account:
[Service account template](https://github.com/bdastur/notes/tree/master/kubernetes/service_account.yaml)

```
$ kubectl create -f service_account.yaml
```

### Create a Cluster Role binding:

Example of creating a cluster role binding for our Cluster Role and use our
service account as a subject.

[Cluster Role binding template](https://github.com/bdastur/notes/tree/master/kubernetes/cluster_role_binding.yaml)

```
$ kubectl create -f cluster_role_binding.yaml
```

### How to login with our service account:

#### Describe our service account:

```
$ kubectl get serviceaccount readonly-user -o yaml
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
(awsenv)MFD57:web-app behzad_dastur$ kubectl describe secret readonly-user-token-cw7n7
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
[oc document - node selectors](https://docs.openshift.com/container-platform/3.4/admin_guide/managing_projects.html#setting-the-project-wide-node-selector)

```
# Get labels for nodes.
kubectl get nodes --show-labels

# Edit the namespace to add node selector.
kubectl edit namespace <namespacename>

openshift.io/node-selector: tier=guaranteed

```

Updating Node Labels:
[oc document - node labels](https://docs.openshift.com/container-platform/3.4/admin_guide/manage_nodes.html#updating-labels-on-nodes)

```
$ kubectl label node ip-10-110-23-12.compute.internal product-line=esg --overwrite

```



### Resource reqeusts and Scheduling.

**Links**:
https://kubernetes.io/docs/concepts/configuration/manage-compute-resources-container/

http://blog.kubernetes.io/2017/03/advanced-scheduling-in-kubernetes.html

#### Creating a resource quota

```
 more test_quota.yaml
apiVersion: v1
kind: ResourceQuota
metadata:
  name: compute-resources
spec:
  hard:
    pods: "4"
    requests.cpu: "1"
    requests.memory: 1Gi
    limits.cpu: "2"
    limits.memory: 2Gi

```

```
oc project web-app
oc create -f test_quota.yaml

$ oc describe quota compute-resources
Name:       compute-resources
Namespace:  web-app
Resource    Used    Hard
--------    ----    ----
limits.cpu  0   2
limits.memory   0   2Gi
pods        0   4
requests.cpu    0   1
requests.memory 0   1Gi

```

### Using Service accounts:

You can include service account credentials in your deployment configuration.

```
---
  kind: "Template"
  apiVersion: "v1"
  metadata:
    name: "acu-usage"
  objects:
    -
      kind: "DeploymentConfig"
      apiVersion: "v1"
:
      spec:
        strategy:
          type: "Recreate"
        triggers:
:
      serviceAccount: kube-utils-user
      serviceAccountName: kube-utils-user

```

You can then reference the service account credentials in the container. The
credentials/token are stored in /var/run/secrets/kubernetes.io/serviceaccount.


### Namespaces.

Creating a namespace:
```
$ kubectl create -f ./templates/namespace.json
namespace "development" created


$ kubectl get namespaces
NAME          STATUS    AGE
default       Active    2h
development   Active    17s
kube-public   Active    2h
kube-system   Active    2h
```

Deleting a namespace:
```
$ kubectl delete namespace development
namespace "development" deleted

```

Switching to a new namespce:

First add the new context into our ~/.kube/config file:

```
- context:
    cluster: gke_test-project-kube-mar18_us-east1-b_testcluster-1
    user: gke_test-project-kube-mar18_us-east1-b_testcluster-1
  name: gke_test-project-kube-mar18_us-east1-b_testcluster-1-brd-test-1

```

Now switch to the new namespace:

```
 $ kubectl config use-context gke_test-project-kube-mar18_us-east1-b_testcluster-1-brd-test-1
```


### Static Pods
https://kubernetes.io/docs/tasks/administer-cluster/static-pod/

* static pods are managed directly by kubelet daemon.
* They do not have any replication controller, and kubelet daemon watches it
  and restarts if it crashes.
* There is no health check.
* Static pods are always bound to one kubelet daemon and always run on the same node.

#### Creating a static pod:

Create a deployment file . Eg below:
let's say in /etc/kubernetes/manifests
```
apiVersion: v1
kind: Pod
metadata:
  namespace: kube-system
  name: static-web
  labels:
    role: myrole
    kubernetes.io/cluster-service: "true"

spec:
  hostNetwork: false
  containers:
    - name: web
      image: nginx:latest
      resources:
        limits:
          memory: 4Gi
        requests:
          memory: 4Gi
      ports:
        - name: web
          containerPort: 80
          hostPort: 9080
          protocol: TCP

```

When running kubelet, specify the --pod-manifest-path as below:
```
kubelet --pod-manifest-path=/etc/kubernetes/mainfests

```
There is not need to restart kubelet if you update or add a new pod definition


## Daemonsets:
https://v1-7.docs.kubernetes.io/docs/concepts/workloads/controllers/daemonset/

A sample template for a Daemonset (V1.7.8)

```
apiVersion: extensions/v1beta1
kind: DaemonSet
metadata:
  namespace: kube-system
  name: web-daemon
  labels:
    role: myrole
    kubernetes.io/cluster-service: "true"

spec:
  template:
    metadata:
      labels:
        name: web-daemon
    spec:
      containers:
        - name: web
          image: nginx:latest
          resources:
            limits:
              memory: 2Gi
            requests:
              memory: 2Gi
          ports:
            - name: web
              containerPort: 80
              hostPort: 9083
              protocol: TCP

```

Creating the daemonset is the same as creating a pod.

```
$ kubectl create -f  webdaemon.yaml
```

Listing daemonsets:
```
$ kubectl get daemonset
NAME         DESIRED   CURRENT   READY     UP-TO-DATE   AVAILABLE   NODE SELECTOR   AGE
web-daemon   23        23        20        23           20          <none>          13m

```

Deleting a daemonset:
```
$ kubectl delete daemonset web-daemon
```


## Service mesh:
To simply put, it is a dedicated infrastructure layer that handles
service-to-service communication between pods/services running kubernetes.

### Istio:
https://istio.io/docs/setup/kubernetes/quick-start/
https://github.com/dcberg/istio-workshop

With Istio, this infrastructure layer is created by deploying a lightweight proxy
alongside each application service. The application itself does not need to be
aware of the proxy.

The monitoring, management and security of communication can be handled outside of
the application logic.

Installing Istio:
```
$ curl -L https://git.io/getLatestIstio | sh -
$ export PATH="$PATH:/Users/behzad.dastur/clusters/testenv/istio/istio-0.8.0/bin"
$
$ istioctl -h

```

Installing Istio on kubernetes:

```
kubectl create clusterrolebinding cluster-admin-binding  \
   --clusterrole=cluster-admin \
   --user=$(gcloud config get-value core/account)

```

```
kubectl apply -f istio-0.8.0/install/kubernetes/istio-demo.yaml
```

Installing with Helm via helm template.
If you do not have tiller running on the cluster, you can create a deployment template from helm charts as below.

```
cd istio-0.8.0
helm template install/kubernetes/helm/istio --name istio --namespace istio-system > myistiotemplate.yaml

```

Install components via the manifest:
```
kubectl create namespace istio-system
kubectl create -f myistiotemplate.yaml
```

Istio manual side-car injection:

```
kubectl apply -f <(istioctl kube-inject -f istio-workshop/guestbook/helloworld-deployment.yaml)
```

### Kubernetes client:
https://github.com/kubernetes-client/python/blob/master/kubernetes/README.md
https://github.com/kubernetes/website/pull/6836/files


### How to start an interactive bash pod within Kubernetes cluster.
https://gc-taylor.com/blog/2016/10/31/fire-up-an-interactive-bash-pod-within-a-kubernetes-cluster

```
$ kubectl run test-shell --rm -i --tty --image bdastur/simplepy:latest -- bash
If you don't see a command prompt, try pressing enter.
bash-4.4# 

```

## Gcloud

### SDK Installation:

```
$ wget https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-cloud-sdk-193.0.0-darwin-x86_64.tar.gz
$ gunzip google-cloud-sdk-193.0.0-darwin-x86_64.tar.gz
$ tar -xvf google-cloud-sdk-193.0.0-darwin-x86_64.tar
$ cd google-cloud-sdk
$ ./install.sh
$
$ source ~/.bash_profile
$ glcoud --help

```

### List projects.

```
$ gcloud projects list

```


### Set into a project

```
gcloud config set project test-project-kube-mar18

```
### List cloud sdk properties.

```
$ gcloud config list

```

### List credentialed accounts.

```
$ gcloud auth list

```

### Setup a Kubernetes cluster.

To check which Kubernetes versions are default and available in a given zone
```
$ gcloud container get-server-config --zone us-east1-b

```

Create a kubernetes cluster called testcluster-1
```
gcloud container clusters create testcluster-1 \
  --cluster-version=1.9.4-gke.1 \
  --disk-size=50 \
  --labels=tier=regular \
  --max-nodes-per-pool=100 \
  --node-labels=tier=regular \
  --node-version=1.9.4-gke.1 \
  --num-nodes=3 \
  --tags=tag1
```

To resize existing cluster
```
 gcloud container clusters resize testcluster-1 --size=4
```

To refresh add credentials to a kube cluster:

```
 gcloud container clusters get-credentials testcluster-1 --zone us-east1-b
```

Prerequisits for using RBAC in GKE.
First grant your user the ability to create roles in Kubernetes.

```
$ kubectl create clusterrolebinding cluster-admin-binding --clusterrole cluster-admin --user behzad.dastur@gmail.com
clusterrolebinding.rbac.authorization.k8s.io "cluster-admin-binding" created

$ kubectl get clusterrolebinding cluster-admin-binding -o yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  creationTimestamp: 2018-06-19T01:07:07Z
  name: cluster-admin-binding
  resourceVersion: "3070"
  selfLink: /apis/rbac.authorization.k8s.io/v1/clusterrolebindings/cluster-admin-binding
  uid: 160ae2aa-735d-11e8-8545-42010a8e013d
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: ClusterRole
  name: cluster-admin
subjects:
- apiGroup: rbac.authorization.k8s.io
  kind: User
  name: behzad.dastur@gmail.com

```


## Helm:

### Useful links:
* [Helm Documentation home](https://docs.helm.sh/)
* [Getting started with a chart template](https://docs.helm.sh/chart_template_guide/#getting-started-with-a-chart-template)
* [Helm tutorials](https://jfrog.com/blog/10-helm-tutorials-to-start-your-kubernetes-journey/)


## Minikube:

### starting minikube:
```
#!/bin/bash

echo "Starting minikube"
MEMORY="1024"
CPU="1"
KUBE_VERSION="v1.10.0"
VMDRIVER="virtualbox"

minikube start --memory=$MEMORY --cpus=$CPU --kubernetes-version=$KUBE_VERSION \
    --extra-config=controller-manager.cluster-signing-cert-file="/var/lib/localkube/certs/ca.crt" \
    --extra-config=controller-manager.cluster-signing-key-file="/var/lib/localkube/certs/ca.key" \
    --vm-driver=`$VMDRIVER`
```

## Setting up kubernetes prompt

* Copy the [kube-ps1.sh ](https://github.com/jonmosco/kube-ps1) script to a
  location on your mac.
* Add the following to your `.bashrc` or `.zshrc` file

(in this case I have saved the kube-ps1.sh as `/tools/kube_ps1.sh`
```
export KUBECONFIG="$HOME/.kube/prodconfig"
source ~/tools/kube_ps1.sh
export PROMPT='$(kube_ps1)'$PROMPT
```

Now you should see the kubernetes context and namespace in your prompt
```
(⎈ |oresimpl:default)√[behzad.dastur] ~/.scylla %~> 
```

You can turn this on and off using `kubeon/kubeoff`



## CKA:
Key components:

Master nodes:
etcd
Controller Manager (10252)
Kube Scheduler (10251)
Kube apiserver (443)


Worker nodes:
docker, containerd or rocket
kube-proxy
kubelet


### etcd:


## Krew:
###  Installing on mac

```
#!/bin/sh
# Installing Krew

(
  set -x; cd "$(mktemp -d)" &&
  OS="$(uname | tr '[:upper:]' '[:lower:]')" &&
  ARCH="$(uname -m | sed -e 's/x86_64/amd64/' -e 's/\(arm\)\(64\)\?.*/\1\2/' -e 's/aarch64$/arm64/')" &&
  KREW="krew-${OS}_${ARCH}" &&
  curl -fsSLO "https://github.com/kubernetes-sigs/krew/releases/latest/download/${KREW}.tar.gz" &&
  tar zxvf "${KREW}.tar.gz" &&
  ./"${KREW}" install krew
)

```

### After that update our environment PATH to add $HOME/.krew/bin

### Install a plugin

```
kubectl krew install access-matrix
```

Using the plugin:

 | Caveats:
 | \
 |  | Usage:
 |  |   kubectl access-matrix
 |  |   kubectl access-matrix for pods
 | /
/







