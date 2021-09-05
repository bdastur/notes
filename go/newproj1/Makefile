ARCH := amd64
OS := $(shell uname -s | tr A-Z a-z)
GOOS := $(OS)
PKG := $(shell echo $$PKG)

BUILD_IMAGE ?= bdastur/gobuildagent:0.1

build: lint
	go mod tidy
	go build -o /tmp/newproj1 main.go

lint:
	golangci-lint run --verbose --enable cyclop --enable gocyclo ./...


docker-build:
	@docker run -ti \
				--rm \
				-u $(BUILD_USER):$(BUILD_GROUP) \
				-v "$$(pwd)/.go:/go" \
				-v "$$(pwd):/go/src/$(PKG)" \
				-v "$$(pwd)/bin/$(ARCH):/go/bin" \
				-v "$$(pwd)/bin/$(ARCH):/go/bin/$$(go env GOOS)_$(ARCH)" \
				-v "$$(pwd)/.go/std/$(ARCH):/usr/local/go/pkg/linux_$(ARCH)_static" \
				-w /go/src/$(PKG)\
	            -e "GOPATH=/go"\
				-e "GOARCH=$(ARCH)" \
				-e "GOOS=$(OS)" \
				--entrypoint /usr/local/go/bin/go \
				$(BUILD_IMAGE) \
				build -o ./mainbin main.go

build-dirs:
	@mkdir -p bin/$(ARCH)
	@mkdir -p .go/src/$(PKG) .go/internal .go/bin .go/std/$(ARCH)

print-params:
	@echo "======================================="
	@echo "Go make - build/lint/cyclomatic complexity"
	@echo "PKG: $(PKG)"
	@echo "Build User: $(BUILD_USER):$(BUILD_GROUP)"
	@echo "GO OS: $(GOOS)"
	@echo "======================================="
