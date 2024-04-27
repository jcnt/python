package main

import "fmt"

func main() {

	x := 66
	y := 77
	z := 66

	if x < 50 {
		fmt.Println("Smaller")
	} else {
		fmt.Println("Bigger")
	}

	if x < z && y > z {
		fmt.Println("Z in between")
	} else if x < z && y < z {
		fmt.Println("Z bigger than both")
	} else if x > z && y > z {
		fmt.Println("Z smaller than both")
	} else {
		fmt.Println("something else")
	}




}