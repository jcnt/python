package main

import "fmt"

func main(){

	x := doMath(1, 2, add)
	fmt.Println(x)

	y := doMath(42, 16, subtract)
	fmt.Println(y)


	fmt.Printf("%T\n", add)
	fmt.Printf("%T\n", subtract)
	fmt.Printf("%T\n", doMath)

}

func doMath(a int, b int, f func(int, int) int) int {
	return f(a,b)

}

func add(a int, b int) int {
	return a + b
}

func subtract(a int, b int) int {
	return a - b
}
