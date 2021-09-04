build: lint
	go build -o /tmp/newproj1 main.go

lint:
	golangci-lint run --verbose --enable cyclop --enable gocyclo ./...
