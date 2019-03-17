package main

import (
	"fmt"
	"math/rand"
	"time"
)

func main() {
	a := 1
	b := 2

	fmt.Println("Main Go!")

	result := make(chan int, 2)

	go calculate(a, b, result)
	b = <-result

	a = b * b
	fmt.Println("This is in main")
	//fmt.Scanln()
	fmt.Println("Done")
	fmt.Printf("a = %d, b = %d \n", a, b)
}

func calculate(a int, b int, result chan<- int) {
	fmt.Println("Calculate - go routine")
	sleepDuration := time.Duration(rand.Intn(10))
	fmt.Println("Sleep Duration: ", sleepDuration)

	time.Sleep(time.Duration(rand.Intn(10)) * time.Second)
	result <- (a * b)
}
