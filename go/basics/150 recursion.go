package main

import "fmt"

func main() {
	fmt.Println(factorial(4))
	fmt.Println(factloop(4))
}

func factorial(n int) int {
	fmt.Println("This is n", n)
	if n == 0 {
		return 1
	}
	return n * factorial(n-1)
}

func factloop(n int) int {
	total := 1
	for n > 0 {
		fmt.Println("loop, n currently is ", n)
		total *= n
		n--
	}
	return total
}