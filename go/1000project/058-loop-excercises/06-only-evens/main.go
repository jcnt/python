// Copyright © 2018 Inanc Gumus
// Learn Go Programming Course
// License: https://creativecommons.org/licenses/by-nc-sa/4.0/
//
// For more tutorials  : https://learngoprogramming.com
// In-person training  : https://www.linkedin.com/in/inancgumus/
// Follow me on twitter: https://twitter.com/inancgumus

package main

import (
	"fmt"
	"os"
	"strconv"
)

// ---------------------------------------------------------
// EXERCISE: Only Evens
//
//  1. Extend the "Sum up to N" exercise
//  2. Sum only the even numbers
//
// RESTRICTIONS
//  Skip odd numbers using the `continue` statement
//
// EXPECTED OUTPUT
//  Let's suppose that the user runs it like this:
//
//    go run main.go 1 10
//
//  Then it should print:
//
//    2 + 4 + 6 + 8 + 10 = 30
// ---------------------------------------------------------

func main() {

	if len(os.Args) != 3 {
		fmt.Println("Please provide min and max")
		return
	}

	min, max := os.Args[1], os.Args[2]
	var sum int

	if min >= max {
		fmt.Println("min should be smaller than max!")
		return
	}

	n, err := strconv.Atoi(min)
	if err != nil {
		fmt.Println("min should be a number!")
		return
	}

	x, err := strconv.Atoi(max)
	if err != nil {
		fmt.Println("max should be a number!")
		return
	}

	for i := n; i <= x; i++ {
		if i % 2 != 0 {
			continue
		}

		sum += i
		fmt.Printf("%d", i)
		if i < x {
			fmt.Print(" + ")
		}


	}
	fmt.Printf(" = %d\n", sum)
}
