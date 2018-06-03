package datatypes

import (
	"fmt"
)

func CompositeTypes() {
	fmt.Println("Composite types!")
	/*
	 * Declaring an int array
	 */
	var iarr1 [5]int

	/*
	 * Looping over an array using range.
	 */
	for i, v := range iarr1 {
		fmt.Printf("%d %d \n", i, v)
	}
	fmt.Printf("-------------------\n")

	/*
	 * Looping over an array the old fashioned way.
	 */
	for i := 0; i < len(iarr1); i += 1 {
		fmt.Printf("%d %d \n", i, iarr1[i])
	}

	/*
	 * array of strings.
	 */

	var sarr2 [3]string
	for i, v := range sarr2 {
		sarr2[i] = "abc"
		fmt.Printf("%d %s, %s\n", i, v, sarr2[i])
	}
}
