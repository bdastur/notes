# GOLANG.

## Directory Layout.

NOTE: Always create a new directory inside $GOPATH/src, when starting a Go project.
* https://github.com/alco/gostart


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

*Looping over a list and handling empty list*

```
instance_types = [{{ range .InstanceTypes}}"{{ . }}", {{ else }} "{{ .InstanceType }}" {{ end }}]
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

## Exercise with go mod and scaffold.





## Useful packages:

[Package pretty](https://godoc.org/github.com/kr/pretty)


## Starting up a new go project (go mod)

### Create a project folder.

```
%~> mkdir testproj1
%~> cd testproj1
```

### Initialize go module.
```
%~> go mod init github.com/bdastur/newproj1
go: creating new go.mod: module github.com/bdastur/newproj1
%~> ls
go.mod

```

### Create your scaffold.

/notes/go/newproj1

```
%~> tree
.
├── cmd
│   └── main.go
├── go.mod
├── main.go
└── test

```

### Add missing modules and remove unused modules.

```
 %~> go mod tidy
go: finding module for package github.com/spf13/cobra
go: found github.com/spf13/cobra in github.com/spf13/cobra v1.2.1

%~> go build -o test main.go
```

### Create a Makefile.
```
%~> more Makefile 
build: lint
        go build -o /tmp/newproj1 main.go

lint:
        golangci-lint run --verbose --enable cyclop --enable gocyclo ./...

```

### Running golangci-lint

```
%~> golangci-lint run --verbose --enable cyclop ./...
INFO [config_reader] Config search paths: [./ /Users/behzad.dastur/code/katas/newproj1 /Users/behzad.dastur/code/katas /Users/behzad.dastur/code /Users/behzad.dastur /Users /] 
INFO [lintersdb] Active 11 linters: [cyclop deadcode errcheck gosimple govet ineffassign staticcheck structcheck typecheck unused varcheck] 
INFO [loader] Go packages loading at mode 575 (deps|exports_file|files|imports|types_sizes|compiled_files|name) took 1.593871862s 
INFO [runner/filename_unadjuster] Pre-built 0 adjustments in 480.375µs 
INFO [linters context/goanalysis] analyzers took 0s with no stages 
INFO [runner] processing took 2.673µs with stages: max_same_issues: 452ns, skip_dirs: 267ns, max_from_linter: 205ns, nolint: 203ns, cgo: 149ns, source_code: 132ns, path_prettifier: 127ns, diff: 123ns, identifier_marker: 121ns, uniq_by_line: 119ns, skip_files: 118ns, autogenerated_exclude: 118ns, filename_unadjuster: 118ns, sort_results: 65ns, exclude: 64ns, exclude-rules: 63ns, max_per_file_from_linter: 60ns, path_shortener: 59ns, severity-rules: 56ns, path_prefixer: 54ns 
INFO [runner] linters took 98.019374ms with stages: goanalysis_metalinter: 97.957142ms 
INFO File cache stats: 0 entries of total size 0B 
INFO Memory: 19 samples, avg is 72.4MB, max is 73.3MB 
INFO Execution took 1.70811726s                   

```

