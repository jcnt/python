package main

import "fmt"

func main() {
	n := []int{1, 2, 3, 4, 5, 6, 7, 8, 9}

	fmt.Println(foo(n))

	fmt.Println(bar(n...))
}

func foo(n []int) int {
	s := 0
	for _, v := range n {
		s += v
	}
	return s
}

func bar(m ...int) int {
	s := 0
	for _, v := range m {
		s += v
	}
	return s
}