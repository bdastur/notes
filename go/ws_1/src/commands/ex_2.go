package main

import (
	"fmt"
	"simpleutils"
	"time"
)

func fib(x int) int {
	if x < 2 {
		return x
	}
	return fib(x-1) + fib(x-2)
}

/*
 * Using go routines.
 * In this case invoking spinner to indicate progress bar while finding
 * fibonacci number.
 */
func main() {
	fmt.Println("Ex2\n")
	// A go statement causes this function to be called in a newly
	// created goroutine.
	go simpleutils.Spinner(100 * time.Millisecond)
	const n = 40
	fibN := fib(n)
	fmt.Printf("\nFibonacci of %d is %d\n", n, fibN)
}
