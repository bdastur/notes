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
