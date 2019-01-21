# Notes on Jenkins.
----

## Useful links:
[Jenkins plugins](https://plugins.jenkins.io/ansible)
[Official Jenkins Docker repo](https://github.com/jenkinsci/docker)


## Allowing your CI container to start other docker agents/containers.
* If you want your CI container, to be able to start containers, then a simple way is
  to expose /var/run/docker.sock to your CI container using -v flag.
  ``` --volume /var/run/docker.sock:/var/run/docker.sock```.
  You will also need to install the docker cli in your CI container.

* Now your CI container will be ablee to start containers. Except that instead of
  starting child containers, it will start sibling containers.

