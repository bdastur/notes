# GOLANG.

## Directory Layout.

```
GOPATH=$(HOME)/CODE/ws_1

$ $HOME/CODE/ws_1
src/
   command/main.go
   foo/bar/x.go


pkg/
   linux_amd64/
       foo/bar.a

bin/
  testbinary

```



## Writing and running the simplest test.

```
$GOPATH/src/commands/first_test.go

package main

import (
    "testing"
    "fmt"
)

func TestBasic(t *testing.T) {
    fmt.Println("Test Basic!")
}


```

To run this test:

```
go test ./src/commands/ -v
=== RUN   TestBasic
Test Basic!
--- PASS: TestBasic (0.00s)
PASS
ok  	commands	0.007s

```

## Creating a Library.
Example in ws_2 folder.

```
$ cd ws_2
$ export GOPATH=$(pwd)
$ mkdir src/github.com/bdastur/stringutil

```
Create a new stringutil.go file under that.

Check that the package compiles
```
go build github.com/bdastur/stringutil
```

Execute go install to build the shared library.

```
go install github.com/bdastur/stringutil
```

The shared library will be created under

```
pkg/darwin_amd64/github.com/bdastur/stringutil.a 
```

Updated hello.go to use the stringutil library.

