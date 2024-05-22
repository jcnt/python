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
// EXERCISE: Refactor to Array Literals
//
//  1. Use the 02-get-set-arrays exercise
//
//  2. Refactor the array assignments to array literals
//
//    1. You would need to change the array declarations to array literals
//
//    2. Then, you would need to move the right-hand side of the assignments,
//       into the array literals.
//
// EXPECTED OUTPUT
//   The output should be the same as the 02-get-set-arrays exercise.
// ---------------------------------------------------------

func main() {

	names := [3]string{"James", "John", "Jack"}
	distances := [5]int{20, 25, 10}
	alives := [4]bool{true, true, false, false}

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
