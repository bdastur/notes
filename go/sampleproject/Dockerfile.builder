# Note: this is the builder pattern described in this blog:
# (https://blog.alexellis.io/mutli-stage-docker-builds/).
# There is a better way to do this by using a multi-stage Dockerfile, which
# is also present in this directory.

FROM golang:1

ENV MAIN_GO_FILE=cmd/sampleproject/main.go

WORKDIR /workspace

COPY go.* /workspace/

# Download any external go modules.
RUN go mod download

COPY cmd/ cmd
COPY internal/ internal

# Build.
RUN  GOOS=darwin go build -a -o sampleproj $MAIN_GO_FILE
