# Docker


## Useful links

* [Dockerfile Reference](https://docs.docker.com/engine/reference/builder/)
* [Dockerfile best practices](https://docs.docker.com/develop/develop-images/dockerfile_best-practices/)
* [The twelve factor App](https://12factor.net/codebase)

## Format.

# Comment
INSTRUCTION arguments

## Environment variables.

```

ENV FOO=/bar
ENV my_new_var="A new Var $FOO"

:

RUN echo ${FOO}
RUN echo $my_new_var
RUN env

```

## FROM

```
FROM [--platform=<platform>] <image>[:<tag>] [AS <name>]

```

* An ARG declared before a FROM is outside the build stage, so it can't be used in any
  instruction after the FROM.

* To use the default value of an ARG declared before the first FROM, use an ARG
  without a value inside of a build stage (as below).

```
ARG VERSION="latest"
FROM amazonlinux:$VERSION

ARG VERSION
RUN echo $VERSION > image_version


Build output:
 => [2/6] RUN echo latest > image_version     
```
* From can appear multiple times in a Dockerfile to create multiple images or
  use one build stage as a dependency for another. 
* Each FROM instruction clears any state created by previous instructions.



## RUN.
* The cache for RUN instructions isn't invalidated automatically during the next build.
  The cache for an instruction like `RUN apt-get dist-upgrade -y` will be reused during
  the next build. You can invalidate the cahce by using `--no-cache flag`

Two options:

```
RUN <command>
RUN [ "executable", "param1", "param2"]
```


## CMD

Format:
```
CMD ["executable", "param1", "param2"]  (exec form, this is the preferred form)
CMD ["param1", "param2"] (as default parameters to ENTRYPOINT
CMD command param1 param2  (shell form)
```

There can only be one CMD instruction in a Dockerfile. If you list more than one CMD
then only the last CMD will take effect.

## LABEL

Format:

```
LABEL application="example" OS="AL2"
```

## Expose
* Note: the EXPOSE instruction does not actually publish the port. It functions as a 
  type of documentation between the person who builds the image and the person who
  runs the container, about which ports are intended to be published.


## ENV
* Allows you to set a variable <key> to a <vaule>. This value will be in the environment
for all subsquent instructions in the build stage. The ENV will persist when a 
container is run from the resulting image

* Difference between ENV and ARG is that ARG <value> is only available during the build
  stage and is not persisted in the final image.


