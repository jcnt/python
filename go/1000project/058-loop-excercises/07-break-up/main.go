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
// EXERCISE: Break Up
//
//  1. Extend the "Only Evens" exercise
//  2. This time, use an infinite loop.
//  3. Break the loop when it reaches to the `max`.
//
// RESTRICTIONS
//  You should use the `break` statement once.
//
// HINT
//  Do not forget incrementing the `i` before the `continue`
//  statement and at the end of the loop.
//
// EXPECTED OUTPUT
//    go run main.go 1 10
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

	i := n

	for  {
		if i > x {
			break
		} else if i % 2 != 0 {
			i++
			continue
		}

		fmt.Printf("%d", i)
		if i < x {
			fmt.Print(" + ")
		}

		sum += i
		i++


	}
	fmt.Printf(" = %d\n", sum)
}
