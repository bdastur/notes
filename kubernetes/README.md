# Kubernetes and Openshift Notes:

## Simple Web application workflow.
Walkthrough of creating a simple web application.


### Code for simple application:

[simple-web-app](/Users/behzad_dastur/CODE/notes_dec3/notes/kubernetes/simple-web-app)

### Building and Pushing the image to registry:
```
export REGISTRY=`registry.abc.xyz.com`

docker build --tag=$REGISTRY/alpine:0.1 .
docker push $REGISTRY/alpine:0.1

```

### Openshift/Kubernetes templates:
