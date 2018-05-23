package main

import (
	"flag"
	"fmt"
	"os"
)

func read_argument(args []string) {
	// Using Printf function
	fmt.Printf("Arguments: %s %s", args, "\n")

	// Using Println
	fmt.Println("Arguments: ", args)

	// Get options (flags)
	wordPtr := flag.String("word", "default-word", "A random string")
	numPtr := flag.Int("count", 10, "A random number")
	boolPtr := flag.Bool("dry-run", true, "Boolean flag true/false")

	flag.Parse()

	fmt.Println("WordPtr: ", *wordPtr)
	fmt.Println("numPtr: ", *numPtr)
	fmt.Println("Bool ptr: ", *boolPtr)
	fmt.Println("Arguments: ", flag.Args())

}

func main() {
	fmt.Println("Test Basic!")

	read_argument(os.Args)

}
