package main

import "fmt"

func main() {
	x := 42
	fmt.Println(x)
	fmt.Println(&x)

	fmt.Printf("x int \t\tValue: %v \ttype: %T\n", &x, &x)

	s := "james"
	fmt.Printf("s str \t\tValue: %v \ttype: %T\n", &s, &s)

	// y is going to get the same address in memory as x
	y := x
	fmt.Printf("y := x \t\tValue: %v \ttype: %T\n", &y, &y)

	z := &x
	fmt.Printf("z ;= &x \tValue: %v \ttype: %T\n", &z, &z)

	//dereference a pointer
	fmt.Println(*z)
	fmt.Println(*&x)

	*z = 43
	fmt.Println(x)
	fmt.Println(z)

}
