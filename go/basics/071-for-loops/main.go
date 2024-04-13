package main

import "fmt"

func main() {
	for i := 0; i < 5; i++ {
		fmt.Printf("looping through with i, now the value is %v\n", i)
	}

	y := 1

	for y < 10 {
		fmt.Printf("y right now is %v\n", y)
		y++
	}

	for {
		fmt.Printf("second loop is different, value now is %v\n", y)
		if y > 20 {
			break
		}
		y++
	}

	for j:=1; j<20; j++ {
		if j%2 != 0 {
			continue
		}
		fmt.Printf("printing out even numbers: %v\n", j)
	}

	// nested loops
	for a:=1; a<6; a++ {
		for b:=1; b<6; b++{
			fmt.Printf("nested loop, outer is %v, inner is %v\n", a, b)
		}
	}

}