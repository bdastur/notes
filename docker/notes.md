# Notes on Docker.


## Useful links:

* [docker docs storage driver](https://docs.docker.com/storage/storagedriver/select-storage-driver/)
* [storage driver deep dive](https://integratedcode.us/2016/08/30/storage-drivers-in-docker-a-deep-dive/)
* [CIS Docker Benchmark tool](https://github.com/aquasecurity/docker-bench)
* [ CIS Docker Benchmark](https://drive.google.com/drive/u/0/folders/1k6KXjkyWUOUGJFb-CG08B_qAl8CsEx_m)

* [Distroless](https://github.com/GoogleContainerTools/distroless)
* [Multistage docker builds](https://blog.alexellis.io/mutli-stage-docker-builds/)
* [Docker ARG, ENV and .env Guide](https://vsupalov.com/docker-arg-env-variable-guide/)


## Follow up reading:

### Docker Content trust.

The Docker images used in a production environment should come from a trusted party.
The DOCKER_CONTENT_TRUST=1 environment variable will force the Docker engine to
guarantee that the pulled image is the correct image. Also, it's recommended to
avoid using --disable-content-trust flag in docker pull commands. In this way,
containers will be running trusted images and the production environment
will not be at risk.

It's recommended to avoid copying sensitive information into the Docker image.
The file containing customer information is mounted as a volume that will be
available to the app when the container is launched. In this way, such information
will not be stored in the Docker image and it will not be exposed to unauthorized parties.

It's recommended that docker.service user and group ownership are correctly set to root.
The stat command is checking both user and group parameters. In this way, the
script will ensure that only root can have access to this file that contains
sensitive parameters of docker daemon.

It's recommended that /etc/docker user and group ownership are correctly set to root.
The stat command is checking both user and group parameters. In this way, the
script will ensure that only root can have access to this folder that contains
configuration parameters of docker daemon.

Passwords should not be stored in plain text in the source code repository.
Docker Secrets has been used in order to securely store the provided password.
Docker Secrets will populate the password into the path /run/secrets/ inside
the MySQL Exporter container.This prevents an unauthorized user from having
access to the credentials.


When deploying a local Docker registry using a storage backend in AWS S3 bucket,
it's recommended to use encryption at rest and HTTPS as transport protocol
instead of HTTP. In this way, the information stored in the Docker registry will be
protected.

```
docker service create \
    --name scw-local-registry \
    --publish published=5000,target=5000 \
    -e "REGISTRY_STORAGE=s3" \
    -e "REGISTRY_STORAGE_S3_REGION=eu-west-1" \
    -e "REGISTRY_STORAGE_S3_BUCKET=scw_internal_registry_bucket" \
    -e "REGISTRY_STORAGE_S3_ENCRYPT=false" \
    -e "REGISTRY_STORAGE_S3_V4AUTH=true" \
    registry:2
```


