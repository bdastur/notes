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

## Passing Arguments and Options.
You can use the packages 'os' and 'flag' to provide a decent command line interface.

Example:
```
package main

import (
    "flag"
    "fmt"
    "os"
)

func read_argument(args []string) {

    // Get options (flags)
    wordPtr := flag.String("word", "default-word", "A random string")
    numPtr := flag.Int("count", 10, "A random number")
    boolPtr := flag.Bool("dry-run", true, "Boolean flag true/false")

    flag.Parse()

    fmt.Println("WordPtr: ", *wordPtr)
    fmt.Println("numPtr: ", *numPtr)
    fmt.Println("Bool ptr: ", *boolPtr)
    fmt.Println("Arguments: ", flag.Args())

}

func main() {
    fmt.Println("Test Basic!")

    read_argument(os.Args)

```

Output:
```
$ ./bin/examples -h
Test Basic!
Arguments: [./bin/examples -h] 
Arguments:  [./bin/examples -h]
Usage of ./bin/examples:
  -count int
        A random number (default 10)
  -dry-run
        Boolean flag true/false (default true)
  -word string
        A random string (default "default-word")


$ ./bin/examples --word=testword --count=43 --dry-run=false somecommand
Test Basic!
Arguments: [./bin/examples --word=testword --count=43 --dry-run=false somecommand] 
Arguments:  [./bin/examples --word=testword --count=43 --dry-run=false somecommand]
WordPtr:  testword
numPtr:  43
Bool ptr:  false
Arguments:  [somecommand]

```

## A simple http server.
ws_2/github.com/bdastur/simpleserver

To test:
```
curl localhost:8080/test -d '{"id": 43, "name": "Bharat"}'
```


## Go templates.

*Conditional check*

```
{{ if eq .ClusterType "dev" }}
    security_groups = ["${data.aws_security_group.sg_worker.id}",
        "${data.aws_security_group.sg_sshIngress.id}",
        "${data.aws_security_group.sg_workerDev.id}"]
{{ else }}
    security_groups = ["${data.aws_security_group.sg_worker.id}",
        "${data.aws_security_group.sg_sts.id}",
        "${data.aws_security_group.sg_misc_egress.id}",
{{ end }}
```

*Looping*
```
{{ range .AZs }}
    variable is {{ . }}
}
{{ end }} 
```

*Looping over a list of structs*
```
 {{range .Volumes.SecondaryVolumes}}
    {
        name = "{{ .Device}}"
        volume_type = "{{ .DiskType}}"
        volume_size = "{{ .DiskSize}}"
   },
{{end}}
```


*Looping and getting an index.*
```
{{ $count := 0 }}
{{ range .AZs }}
variable "{{ . }}-{{ $count }}" {
    description = "Availability zone -1"
    type = "string"
    default = "test"
}
{{ end }}


```
