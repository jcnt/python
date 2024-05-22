// Copyright © 2018 Inanc Gumus
// Learn Go Programming Course
// License: https://creativecommons.org/licenses/by-nc-sa/4.0/
//
// For more tutorials  : https://learngoprogramming.com
// In-person training  : https://www.linkedin.com/in/inancgumus/
// Follow me on twitter: https://twitter.com/inancgumus

package main

import "fmt"

// ---------------------------------------------------------
// EXERCISE: Refactor to Ellipsis
//
//  1. Use the 03-array-literal exercise
//
//  2. Refactor the length of the array literals to ellipsis
//
//    This means: Use the ellipsis instead of defining the array's length
//                manually.
//
// EXPECTED OUTPUT
//   The output should be the same as the 03-array-literal exercise.
// ---------------------------------------------------------

func main() {

	names := [...]string{"James", "John", "Jack"}
	distances := [...]int{20, 25, 10}
	alives := [...]bool{true, true, false, false}

	for i, v := range names {
		fmt.Printf("names[%d]: %s\n", i, v)
	}

	for i, v := range distances {
		fmt.Printf("distances[%d]: %d\n", i, v)
	}

	for i, v := range alives {
		fmt.Printf("alives[%d]: %t\n", i, v)
	}

}
