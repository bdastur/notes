# useful links:
* [Example qeustions](https://www.itexams.com/exam/KCNA?)
* [Linux Foundation - dashboard](https://trainingportal.linuxfoundation.org/learn/dashboard)
* [Kubernetes Docs](https://kubernetes.io)


* Cloud native means leveraging cloud for:
 * Resiliency
 * Manageability
 * Observability

Cloud native applications and process are built from the ground up to take full 
advantage of the cloud.

----------------------------------------------------------------------
Setting up a Kubernetes cluster
* Add hostname in the hosts file. to allow servers to talk to each other using hostnames.
* Install containerd on all hosts.

---
kernels modules: overlay, br_netfilter
>sudo modprobe overlay
>sudo modprobe br_netfilter

This will install the Kernel modules.

---
sysctl settings.
Add following settings in /etc/sysctl.d/99-kubernetes-cri.conf
>net.bridge.bridge-nf-call-iptables = 1
>net.ipv4.ip_forward = 1
>net.bridge.bridge-nf-call-ip6tables = 1

run this command for the settings to take effect.
sudo sysctl --system
---

install containerd package.
> sudo apt-get update && sudo apt-get install -y containerd
> mkdir -p /etc/containerd
> sudo containerd config default | sudo tee /etc/containerd/config.toml

sudo systemctl restart containerd
---
Disable swap
Check /etc/fstab to ensure nothing is going to turn swap on.

---
sudo apt-get update && sudo apt-get install apt-transport-https curl -y

---
Add GPG key for kubernetes package repository

---
install kubernetes packages.
sudo apt-get install -y kubelet-1.23. kubeadm=1.23 kubectl

To ensure packags are not automatically update:
sudo apt-mark hold kubelet kubeadm kubectl
---
Initialize cluster (only on controller)

kubeadm init --pod-network-cidr 192.168.0.0 --kubernetes-version 1.23.0

When finished, it provides a command to run:
kubeadm join <ip> --token <> --discovery-token-ca-cert-hash <sha>

----
On workers.
mkdir -p $HOME/.kube
sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
chmown $(id -u):$(id: -g) $HOME/.kube/config

---
on controller
setup kubernetes networking.

kubectl apply -f /path to  calico.yaml

-----
Join worker nodes.

on controller:
kubeadm token create --print-join-command
 - it generates the kubeadm join command, copy that and run it in worker nodes.


----------------------------------------------------------------------

## Kubernetes Fundamentals

### Kubernetes Resources.
* Resources are objects of a certain type in Kubernetes API.
* Objects/Resources have a resource type

* Resource type determines the kubernetes functionality controlled by that object.


To list all resource types in a cluster:

```
kubectl api-resources
```


Documentation for a resource

```
kubectl explain
```

## Resources for pod management.
* ReplicaSet - a given number of replica pods is running at any given time.
* Deployment - similar to ReplicaSet. It has additional functionality - declarative
               way. But it does more.


"Deployment" is a higher-level object that manages the creation and updates of 
ReplicaSets, allowing for advanced features like rolling updates and rollbacks, 
while a "ReplicaSet" is a lower-level object focused solely on ensuring a specified
number of identical pods are always running, essentially acting as a replication mechanism

You typically use a deployment to manage your replicaset, rather than creating them
directly.

* You can create a deployment with a yaml file or imperatively using the command below:

```
kubectl create deploy <name> --image=<image> --replicas=<replicas>
```

## Statefulset.
* Built to manage stateful applications.
* Pods mainitan order and a sticky identity (Same pod name, network host names),
  even if they are re-created on a different node.
* Requires you to create a headless service alongside the statefulset.

## DaemonSet
* Runs replicaset on each node in the cluster.


## Job
* Run a containarized task to completion.

## CronJob
* Runs a job repeatedly according to a schedule


## Container Orchestration:
* Automate the tasks that are required to manage container workload. 
* Avoid manul tasks like running and restarting containers.


## Container Runtime.
* Software responsible for running containers.
* Kubelet communicates with the container runtime.

* Container runtime interface (CRI) - standard protocol between the kublet and
  container runtime.
* Examples of Container Runtime.
  - CRI-O - docker alternative, providing CRI compatability for runc and Kata
    containers.
  - containerd: CNCF project, - emphasises simplicity, robustness and portability.


## Kubernetes Security.
* Security philosopy is based on the 4Cs model - CLoud, Clusters, Containers & Code.

### Authentication.
- Verifying the indentity of a Kubernetes API client, proving who they say they are.
* Methods:
* client certificates : client provides an X509 client cert. kubectl uses this method.
* Bearer tokens - client passes a bearer token in an HTTP request header.
* OpenID connect tokens - OAuth2 integration with external identity providers. uses
  JSON Web Token (JWT) signed by the provider. JWTs include signed identity data about
  the user
* Authentication proxy - A trusted proxy validates authentication data provided via HTTP.
* Anonymous - No authentication occurs.
* There are others in documentation ..


## Authorization.
* Whether a user/client has permission to perform a specific operation.

* Node - specific use case, grants permissions needed by kubelet to work with resources 
  on a specific Node.
* Attribute-Based Access Control (ABAC) - define permissions through the use of policies
  that use attribtues to refer to users, resources etc.
* Role-Based access control (RBAC) - Assign granular permissions to roles. Then assign
  those roles to users.
* Webhook - Kubernetes API server will reach out to a HTTP service to determine if
  permission is allowed. You can use this to implement a fully custom authorization
  scheme.

OPA Gatekeeper:
* Open Policy Agent Gatekeeper - create and enforce policies that control what 
  can and cannot be done in your Kubernetes environment.

* Role based access control.


# Kubernetes Networking.

### Cluster network.
* Kubernetes ues virtual network to allow pods to communicate within the cluster.
* Each pod has its own ip address unique to the cluster.
* Pods can communicate transparently, even if they are on different Nodes.

### Cluster DNS.
* Allows containers to discover services within cluster using hostnames.
* Kubernetes containers are automatically configured to use the cluster dns.

### Network policy
* A kubernetes object that allows you to control what network traffic is allowed 
  within the cluster network.
* Each n/w policy selects which pods it applies to.
* The policy provides rules that define what incoming/out going traffic is allowed.
* Pods are non-isolated by default - all traffic is allowed.

# Exploring Services
* Expose an application running on a set of replica pods as a network service.
* Selects a set of pod and expose them as a single network entity.

## Service Types.
* ClusterIP - Expose the service on an IP address internally within the cluster network.
* NodePort - Expose the service externally using a node port listening on each node.
* Loadbalancer - Expose the service externally using a cloud provider load balancer.
* ExternalName - Creates a DNS record pointing to an external location outside the cluster
  network. This make it easy for Pods to access an external URL or IP address.

## Headless service.
* A service with no cluster ip address.
* Can be used to interface with service discovery mechanisms wihout actually proxying
  traffic.

## Services without selectors.
* It wont select backend pods and the service will not automatically create endpoints.
* You will manually create endpoints.
* Might be used to give additional control.

## Service Discovery
* ClusterDNS
* Environment Variables  - Kubernetes automatically adds environment variables to
  each container that provide information about services.

## Ingress.
* A kubernetes object that manages external access to applications within the
  cluster.
* Can offer additional functionality like load balancing or SSL termination.
* Ingress work along side services.

client --> |ingress| --> |service| --> |pods|

# Service Mesh
* Something that manages communication between application components, often adding
additional functionality like logging, tracing or encryption.
* A service mesh is different from a Kubernetes Service resource.

* Application components communicate with each other through a service mesh of
proxies (sidecards) deployed alongside each component.

||pod|sidecar|+-----+|side-car|pod||

* Sidecard proxies add additional functionality provided by the service mesh.

* Examples of service mesh:
 - Linkerd - part of CNCF - provides metrics, mTLS, more.
 - Consul connect - Built on Hashicrop consul. Connection authorization and mTLS
   encryption
  - Traefik Mesh: Opensource, build for ease of use. Traffic control and observability.
  - Istio: Open-source platform-independent. Policies, traffic mgmt, metrics
  - Kuma: Open source, works with Kubernetes and VMs. Routing, observability and security.
  - F5 NGINX Service mesh: data plane uses NGINX plus. Traffic handling, blue/green
    deployments, zero-trust mTLS.

## Service Mesh Interface (SMI)
* A standard interface for service meshes in Kubernetes.
* Configure any SMI-supporting service mesh using custom Kubernetes resources via the
  Kubernetes API.

# Kubernetes Storage.

## Volumes.
* Provides external storage to your Kubernetes containers to store application data.

* Persistent Volumes: 
Treat storage resources as dynamically, consumable, similar to how Kubernetes 
treats resources like memory and CPU.
* It defines a storage resource.

* A persistent volume claim binds to a PersistentVolume and allows you to mount
the storage resource inside a Pod.

* Reclaim policies:
* What happens to the storage resource when PersistentVolumeClaims are deleted?
* Retain - Reclaim manually.
* Recycle - Automatic reclamation via a simple data scrub.
* Delete - Underlying storage resource is deleted.

## Rook.
* A storage orchestration tool that integrates with Kubernetes.
* Automate torage management with self-managing, self-scaling, self-healing storage
  services.
 
## ConfigMaps and Secrets
* Store configuration data like configs, config files, secure credentials and pass
  it to containers.
* Use secrets for sensitive data like passwords
* Make configuration data unchangeable with immutable: true
* By default secret data is NOT encrypted, just base64-encoded.


# CloudNative Architecture Fundamentals.
* Seeks to design systems that support the goal of cloud native technology.
* CloudNative Arch is the tools, techniques and design strategies to facilitiate

Examples of CLoudnative Arch:
* Loosely coupled microservices
* DevOps practices
* Operational automation
* Serverless
* Orchestration


# Autoscaling.
* Vertical and Horizontal.
* Vertical - more compute power, adding additional CPU/memoyr to nodes

* Horizontal - adding more instances, pods. Adding more nodes to cluster.

## Kubernetes Autoscaling Tools.
* Horizontal Pod Autoscaler.
Monitors resource usage of existing replicas, and creates/destroys replicas when
needed.

* Cluster Autoscaler.
Adds and removes Nodes from the cluster based upon real-time usage.


# Serverless
* AWS Lambda
* Azure Functions
* Google Cloud Functions.

# Cloud Native Community and Governance.
* CNCF: CLoud Native Computing Foundation.

# CloudNative Organizational Personas.
* Generalized roles that interact with cloud native technology in different ways.

* SRE - responsible for maintaining appln reliability and performance.
        Create and maintain SLOs, SLAs and SLIs.

# Open standards.
* A technology specification open to public adoption.
* Allow technologies that support open standard, can work together more easily.

* Open Container Initiative (OCI):
* Organization that creates open standards for container formats and runtimes.
* Image-spec - OCI open standard for container image format.
* Runtime-spec - OCI open standard for container runtimes.
* Reference implementation for the OCI runtime-spec is runc.

* Examples of Open standards:
 - HTML
 - XML
 - OCI runtime-spec and image-spc
 - Kubernetes Service Mesh Interface (SMI)

# Cloud native observability.

## Telemetry and observability

## Telemetry:
* Refers to collecting data such as metrics and log data about a system.
* closely relates to observability. 

## Observability:
* Ability to understand and measure the state of a system based upon data generated
by that system.

## Container logs in kubernetes.
* Kubernetes maintains logs for each container.
* Standard output and error streasm go into the container log.

```
kubectl logs <pod name> -c <container name>
```


## Distributed system tracing.
* Tracks requests across a complex application consisting of multiple components
  and services.
* Each request or interaction is tagged with a unique identifier.
* Helps you understand what is going on as requests make their way through the
  entire system.


* Trace:
Data about a request as it moves through the system; a set of related events
across multiple components.

* Span:
A part of a trace, represenging the request moving through one segment of the
system.

# Monitoring with Prometheus

## Prometheus metric type

* counter: A single number that can only increae or reset to zero.
* gauge - A single number that can go up or down.
* Histograms - counts observations that fit into configurable buckets.
* summary - similar to a histogram, but uses dynamic quantiles over a sliding
  time window.

# Cost management.

* FinOps - refers to the practice of using observability to support automation
  and data-driven decisions to limt cloud costs.

## Examples of cost management.
* Collecting data in Prometheus - show there is enough capacity and scale down 
  as a result.
* Gather metrics about compute resource usage - choose more efficient cloud resources
  for applications.
* Using cluster autoscaler to temporarily scale the cluster up to run a large batch
  processing job.


# Cloud native application delivery.

What is application deliver?
* The processes and techniques used to ship new code to customers. Also known as deployment.

Challenges:
* change brings instability.

## Understanding GitOps
* Using Git to manage your application infrastructure.
* Git is the source of truth for declarative infrastructure/applications.
* 

# GitOps Tools

* Flux:
- syncs manifests stored in a Git repo with your cluster.
- built on top of GitOps toolkit.

* Argo CD:
- uses GitOps to do continous delivery in kubernetes
- includes a gui

# Continuous integration and continuous delivery.















































