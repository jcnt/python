package main

import "fmt"

func main() {
	f := incrementor()
	fmt.Println(f())
	fmt.Println(f())
	fmt.Println(f())
	fmt.Println(f())

	g := incrementor()
	fmt.Println(g())
	fmt.Println(g())
	fmt.Println(g())
	fmt.Println(g())
}

func incrementor() func() int {
	x := 0 					// this gets only assigned when f := happens. 
	return func() int {
		x++
		return x
	}
}
