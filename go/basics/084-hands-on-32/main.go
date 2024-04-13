package main

import "fmt"

func main() {
	i := 20
	for {
		if i < 1 {
			break
		}
		fmt.Println("For loop with break", i)
		i--
	}
}