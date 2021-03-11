package utils

import (
    "fmt"
)

func LogName(name string) string {
    msg := fmt.Sprintf("Name is %s", name)

    fmt.Println(msg)
    return msg
}
