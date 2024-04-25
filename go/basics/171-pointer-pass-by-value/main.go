package main

import "fmt"

func intDelta(n *int) {
	*n = 43
}

func main() {
	a := 42
	fmt.Println(a)
	intDelta(&a)
	fmt.Println(a)

	xi := []int{1, 2, 3, 4}
	fmt.Println(xi)
}
