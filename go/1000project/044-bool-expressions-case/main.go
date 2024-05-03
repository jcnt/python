package main

import "fmt"

func main() {

	i := 0

	switch {
	case i > 0:
		fmt.Println("Positive")
	case i < 0:
		fmt.Println("Negative")
	default:
		fmt.Println("Zero")
	}
}
