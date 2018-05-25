package main

import (
	"flag"
	"fmt"
	"os"
)

func build_cli(args []string) {
	// Using Printf function
	//fmt.Printf("os arguments: %s %s", args, "\n")
	fmt.Println("Arguments: ", args)

	/*
	 * Note: When using flags. The falgs should always be provided
	 * first before any arguments.
	 * Example $ ./bin/examples -dry-run=true <arg1> <arg2>
	 */
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

	build_cli(os.Args)

}
