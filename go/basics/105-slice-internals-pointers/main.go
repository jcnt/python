package main

import "fmt"

func main(){
	a := []int{0, 1, 2, 3, 4, 5, 6}
	b := a
	fmt.Println("a slice", a)
	fmt.Println("b slice", b)

	a[0] = 7
	// printing out and BOTH changed!!
	fmt.Println("\na[0] = 7")
	fmt.Println("a slice", a)
	fmt.Println("b slice", b)

	fmt.Println("\nlets create c with make")
	c := make([]int, 7)
	copy(c, a)
	fmt.Println("a slice", a)
	fmt.Println("b slice", b)
	fmt.Println("c slice", c)
	fmt.Println("\na[0] = 0")
	a[0] = 0
	fmt.Println("a slice", a)
	fmt.Println("b slice", b)
	fmt.Println("c slice", c)


}