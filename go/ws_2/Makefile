####################################
# Sample makefile for go ws_1 
###################################

hello: src/github.com/bdastur/hello/hello.go
	go install github.com/bdastur/hello

examples: src/github.com/bdastur/examples/*.go
	go install github.com/bdastur/examples

sserver: src/github.com/bdastur/simpleserver/*.go
	go install github.com/bdastur/simpleserver

ex_1:  src/commands/ex_1.go
	go build -o bin/ex_1 src/commands/ex_1.go

ex_2: src/commands/ex_2.go
	go build -o bin/ex_2 src/commands/ex_2.go

structs: src/github.com/bdastur/structs/*.go
	go install github.com/bdastur/structs

.PHONY: test_ex1
test_ex1:
	go test ./test/ex_1
