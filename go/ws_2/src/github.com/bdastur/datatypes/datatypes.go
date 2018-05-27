package datatypes

import (
	"fmt"
)

func VariableDeclaration() {
	fmt.Println("----------------------------------------------")
	fmt.Println("Variable Declaration!")

	/*
	 * A var statement declares a list of variables. A var statement
	 * can be at a function or package level.
	 */
	var ui8Var1, ui8Var2 uint8

	ui8Var1 = 42
	ui8Var2 = 23
	fmt.Println("ui8Var1, ui8Var2", ui8Var1, ui8Var2)

	/*
	 * A var declaration can include initializers, on per variable.
	 */
	var ui32Var3 = 4344
	var i, j int = 23, 43
	fmt.Println("ui32Var3, i, j", ui32Var3, i, j)

	/*
	 * Short variable declarations.
	 */
	ui32Var4 := 3443
	fmt.Println("ui32Var4: ", ui32Var4)

	fmt.Println("----------------------------------------------")
}

func IntegerDatatype() {
	fmt.Println("This is IntegerDatatype")
	/*
	 * Go provides both signed and unsigned integer arithmetic.
	 * Signed integers 8, 16, 32 and 64 bits. (int8, int16, int32, int64.)
	 *  unsigned: uint8, uint16, uint32, unit64.
	 * unit and int are types that are natural or most efficient size for
	 * signed and unsigned integers for a particular platform.
	 */

	var ui8Var1 uint8
	var i8Var2 int8 = 43
	var i32Var3 int32 = 8944

	ui8Var1 = uint8(i8Var2)
	ui8Var1 = uint8(i32Var3)
	fmt.Println("ui8Var1: ", ui8Var1)

}
