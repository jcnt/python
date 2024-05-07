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
// EXERCISE: Sum up to N
//
//  1. Get two numbers from the command-line: min and max
//  2. Convert them to integers (using Atoi)
//  3. By using a loop, sum the numbers between min and max
//
// RESTRICTIONS
//  1. Be sure to handle the errors. So, if a user doesn't
//     pass enough arguments or she passes non-numerics,
//     then warn the user and exit from the program.
//
//  2. Also, check that, min < max.
//
// HINT
//  For converting the numbers, you can use `strconv.Atoi`.
//
// EXPECTED OUTPUT
//  Let's suppose that the user runs it like this:
//
//    go run main.go 1 10
//
//  Then it should print:
//
//    1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 = 55
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
		sum += i
		fmt.Printf("%d", i)
		if i < x {
			fmt.Print(" + ")
		}

	}
	fmt.Printf(" = %d\n", sum)
}