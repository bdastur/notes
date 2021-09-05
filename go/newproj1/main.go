package main
import "github.com/bdastur/newproj1/cmd"
import "github.com/bdastur/newproj1/internal/utils"

import "fmt"
import "os"

func main() {
    fmt.Printf("Go Main! \n")
    utils.LogMessage()
    if err := cmd.NewProjCommand().Execute(); err != nil {
        os.Exit(1)
    }
}
