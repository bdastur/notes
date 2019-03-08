build: 
	go build -o bin/main src/github.com/bdastur/main/main.go


BUILD_USER := 2111
BUILD_GROUP := 4111

ARCH := amd64
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


