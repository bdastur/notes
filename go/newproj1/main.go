package main
import "github.com/bdastur/newproj1/cmd"

import "fmt"
import "os"

func main() {
    fmt.Printf("Go Main! \n")
    if err := cmd.NewProjCommand().Execute(); err != nil {
        os.Exit(1)
    }
}
