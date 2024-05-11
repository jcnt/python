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
	"math/rand"
	"os"
	"strconv"
	"time"
)

// ---------------------------------------------------------
// EXERCISE: Double Guesses
//
//  Let the player guess two numbers instead of one.
//
// HINT:
//  Generate random numbers using the greatest number
//  among the guessed numbers.
//
// EXAMPLES
//  go run main.go 5 6
//  Player wins if the random number is either 5 or 6.
// ---------------------------------------------------------

func main() {

	rand.Seed(time.Now().UnixNano())

	if len(os.Args) != 3 {
		fmt.Println("run main.go with a number!")
		return
	}

	u1, err := strconv.Atoi(os.Args[1])

	if err != nil {
		fmt.Printf("%q is not a number", os.Args[1])
		return
	}

	u2, err := strconv.Atoi(os.Args[2])
	if err != nil {
		fmt.Printf("%q is not a number", os.Args[1])
		return
	}

	u := u1
	
	if u2 > u1 {
		u = u2
	}

	fmt.Println(u)

	for i := 0; i <= u; i++ {

		n := rand.Intn(u + 1)

		if u == n {
			switch rand.Intn(3) {
			case 0:
				fmt.Println("You won!")
			case 1:
				fmt.Println("You're awesome!")
			case 2:
				fmt.Println("You're brilliant!")
			}
			return
		}

	}

	switch l := rand.Intn(2); {
	case l == 0:
		fmt.Println("You lose!")
	case l == 1:
		fmt.Println("You did NOT win!")
	}

}
