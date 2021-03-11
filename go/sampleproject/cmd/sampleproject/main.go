package main

import (
    "fmt"
    log_utils "github.com/bdastur/sampleproject/internal/utils"
)


func main() {
    fmt.Println("Sample Project - Main")
    msg := log_utils.LogName("Behzad")
    fmt.Println("MSG: %s", msg)
}
