package main

import "fmt"

func main() {
	x := 20
	for x > 0 {
		fmt.Println("looping through from 20, now at", x)
		x--
	}
}