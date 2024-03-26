package main

import "fmt"

func main() {

	x := sum(1, 2, 3, 4, 5, 6, 7, 8, 9)
	fmt.Println("The sum is", x)

}

func sum(ii ...int) int {
	fmt.Println(ii)
	fmt.Printf("%T\n", ii)

	m := 0 
	for _, v := range ii {
		m += v
	}

	return m

}