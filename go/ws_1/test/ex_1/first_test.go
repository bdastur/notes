package main

import (
    "testing"
    "fmt"
    "mathutils"
)

func TestBasic(t *testing.T) {
    fmt.Println("Test Basic!")
    sum := mathutils.Addition(4, 5)
    fmt.Println("Sum: ", sum)
}

