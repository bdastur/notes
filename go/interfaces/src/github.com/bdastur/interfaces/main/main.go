package main

import (
	"fmt"

	"github.com/bdastur/interfaces/internal/measure"
)

func main() {
	fmt.Println("vim-go")
	r := measure.Rect{Width: 4, Height: 4}
	measure.Measure(r)

	c := measure.Circle{Radius: 34}
	measure.Measure(c)
}
