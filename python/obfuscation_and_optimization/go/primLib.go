package main

import (
        "C"
)

//export getPrime
func getPrime(primeLimit C.int) C.int {
        var limit = int(primeLimit)
        var primes [100000]int
        var found int = 0
        var number int = 2
        var composite bool
        for found <limit {
                composite = false
                for i:=0; i<= found; i++ {
                        if primes[i] != 0 && number%primes[i] == 0 {
                                composite =true
                                break
                        }
                }
                if !composite {
                        primes[found] = number
                        found += 1
                }
                number += 1
        }
        return C.int(primes[found-1])
}

func main() {
        
}

