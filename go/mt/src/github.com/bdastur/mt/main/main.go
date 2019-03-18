package main

import (
	"fmt"
	"math/rand"
	"strconv"
	"time"
)

func main() {
	a := 5
	b := 5
	threadCount := 30

	rand.Seed(time.Now().UTC().UnixNano())

	fmt.Println("Main Go!")

	result := make(chan string, 1)

	for i := 0; i < threadCount; i++ {
		go calculateProduct(a, b, i, result)
	}

	for i := 0; i < threadCount; i++ {
		val := <-result
		fmt.Printf("[%d] Prod val: [%s] \n", i, val)
	}

	go calculateSum(a, b, 1, result)
	val := <-result

	fmt.Println("Prod result: ", val)
	fmt.Println("Sum result: ", val)

	fmt.Println("This is in main")
	//fmt.Scanln()
	fmt.Println("Done")
	fmt.Printf("a = %d, b = %d \n", a, b)
}

func calculateProduct(a int, b int, idx int, result chan<- string) {
	fmt.Printf("Calculate Product - go routine [%d]\n", idx)
	sleepDuration := time.Duration(rand.Intn(10)) * time.Second

	time.Sleep(sleepDuration)
	resval := "idx: " + strconv.Itoa(idx) + " prod: " + strconv.Itoa(a*b*idx)
	result <- resval
}

func calculateSum(a int, b int, idx int, result chan<- string) {
	fmt.Println("Calculate Sum - go routine")
	sleepDuration := time.Duration(rand.Intn(5)) * time.Second
	time.Sleep(sleepDuration)

	resval := "idx: " + strconv.Itoa(idx) + " sum: " + strconv.Itoa(a+b+idx)
	result <- resval
}
