package main

import "fmt"

func main() {
	x := 4200

	switch {
	case x < 10: 
		fmt.Println("single digit number")
	case x > 9 && x < 100: 
		fmt.Println("two digits")
	case x > 99 && x < 1000: 
		fmt.Println("three digits")
	default: 
		fmt.Println("larger number")
	}
}