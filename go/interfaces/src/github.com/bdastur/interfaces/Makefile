build: 
	go build -o bin/main src/github.com/bdastur/main/main.go


BUILD_USER := 2111
BUILD_GROUP := 4111

ARCH := amd64
OS := $(shell uname -s | tr A-Z a-z)
PKG := github.com/bdastur

BUILD_IMAGE ?= gobuildagent:0.1



deps:
	# dep ensure && dep prune
	@echo "fetching deps: $@"
	@docker run                                                             \
		-ti                                                                 \
		--rm                                                                \
		-u $(BUILD_USER):$(BUILD_GROUP)                                       \
		-v "$$(pwd)/.go:/go"                                                \
		-v "$$(pwd):/go/src/$(PKG)"                                         \
		-v "$$(pwd)/bin/$(ARCH):/go/bin"                                    \
		-v "$$(pwd)/bin/$(ARCH):/go/bin/$$(go env GOOS)_$(ARCH)"            \
		-v "$$(pwd)/.go/std/$(ARCH):/usr/local/go/pkg/linux_$(ARCH)_static" \
		-e GLIDE_HOME=/go/src/$(PKG)/.glide"                               \
		-e GOPATH=/go"                                                     \
		-w /go/src/$(PKG)                                                   \
		--entrypoint /projects/bin/dep                                     \
		gobuildagent:0.1                                                      \
		ensure


vet:
	@echo "Run 'go vet' to report on suspicious constructs..."
	@docker run                                                             \
	    -t                                                                  \
	    --rm                                                                \
	    -u $(BUILD_USER):$(BUILD_GROUP)                                       \
	    -v "$$(pwd)/.go:/go"                                                \
	    -v "$$(pwd):/go/src/$(PKG)"                                         \
	    -v "$$(pwd)/bin/$(ARCH):/go/bin"                                    \
	    -v "$$(pwd)/bin/$(ARCH):/go/bin/$$(go env GOOS)_$(ARCH)"            \
	    -v "$$(pwd)/.go/std/$(ARCH):/usr/local/go/pkg/linux_$(ARCH)_static" \
	    --entrypoint go                                                     \
		-e "GOPATH=/go"                                                     \
	    -w /go/src/$(PKG)                                                   \
	    $(BUILD_IMAGE)                                                      \
			vet ./...

SRC_DIRS := main # directories which hold app source (not vendored)

cyclo: vet
	@echo "running code checking tools..."
	@echo "Check for cyclomatic complexity > 10..."
	@docker run                                                             \
	    -t                                                                  \
	    --rm                                                                \
	    -u $(BUILD_USER):$(BUILD_GROUP)                                       \
	    -v "$$(pwd)/.go:/go"                                                \
	    -v "$$(pwd):/go/src/$(PKG)"                                         \
	    -v "$$(pwd)/bin/$(ARCH):/go/bin"                                    \
	    -v "$$(pwd)/bin/$(ARCH):/go/bin/$$(go env GOOS)_$(ARCH)"            \
	    -v "$$(pwd)/.go/std/$(ARCH):/usr/local/go/pkg/linux_$(ARCH)_static" \
		-e "GOPATH=/go"                                                     \
        --entrypoint /projects/bin/gocyclo                                  \
		-w /go/src/$(PKG)                                                   \
	    $(BUILD_IMAGE)                                                      \
		-over 10 $(SRC_DIRS)



build:
	@echo "Building go code"
	@docker run   															\
		-t              												    \
		--rm                                                               \
		-u $(BUILD_USER):$(BUILD_GROUP)									    \
		-v "$$(pwd)/.go:/go"                                                \
        -v "$$(pwd):/go/src/$(PKG)"                                         \
        -v "$$(pwd)/bin/$(ARCH):/go/bin"                                    \
        -v "$$(pwd)/bin/$(ARCH):/go/bin/$$(go env GOOS)_$(ARCH)"            \
        -v "$$(pwd)/.go/std/$(ARCH):/usr/local/go/pkg/linux_$(ARCH)_static" \
        -w /go/src/$(PKG)                                                   \
        -e "GOPATH=/go"                                                     \
		-e "GOARCH=$(ARCH)"                                                 \
		-e "GOOS=$(OS)"                                                     \
        --entrypoint /usr/local/go/bin/go                                   \
        $(BUILD_IMAGE)                                                      \
        build -o ./mainbin main/main.go

