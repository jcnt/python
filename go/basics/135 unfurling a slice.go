package main

import "fmt"

func main() {

	xi := []int{1, 2, 3, 4, 5, 6, 7, 8, 9}
	x := sum(xi...)
	fmt.Println("Printing from func main, the sum is \t", x)
}

func sum(ii ...int) int {
	fmt.Println("Printing ii from sum func\t\t", ii)
	fmt.Printf("Printing the type of ii inside sum\t %T\n", ii)

	n := 0
	for _, v := range ii {
		n += v
	}
	return n
}
