package measure

import (
	"fmt"
	"math"
)

type Geometry interface {
	area() float64
}

type Rect struct {
	Width  float64
	Height float64
}

type Circle struct {
	Radius float64
}

func (r Rect) area() float64 {
	return r.Width * r.Height
}

func (c Circle) area() float64 {
	return 2 * c.Radius * math.Pi
}

func Measure(g Geometry) {
	fmt.Println("measure")
	fmt.Println(g.area())
}
