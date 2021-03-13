# Describes the setup of a sample go project.

### Steps:
1. define the go.mod
2. define the go_env.properties
3. create a main.go (ideally keeping the convention cmd/<proj name>/main.go)
4. A simple build: `go build -a -o sampleproj cmd/sampleproject/main.go`

#### Using the Dockerfile.build (Builder approach).
5. Building the go builder image `docker build --tag bdastur/gobuilder:1.0 -f Dockerfile.builder  .`

