package main

import "fmt"

func main(){

	blue := [5]int{6, 9, 3, 2, 1}
	red := [5]int{6, 9, 3, 2, 1}

	fmt.Println("blue, red, Are they equal?")

	if blue == red {
		fmt.Println("✅")
	} else {
		fmt.Println("nope")
	}

	type bookcase [5]int 
	green := bookcase{6, 9, 3, 2, 1}

	if blue == green {
		fmt.Println("✅")
	} else {
		fmt.Println("nope")
	}

	type cabinet [5]int
	yellow := cabinet{6, 9, 3, 2, 1}
	
	if cabinet(green) == yellow {
		fmt.Println("✅")
	} else {
		fmt.Println("nope")
	}

	fmt.Printf("blue: %#v\n", blue)
	fmt.Printf("red: %#v\n", red)
	fmt.Printf("green: %#v\n", green)
	fmt.Printf("yellow: %#v\n", yellow)

}