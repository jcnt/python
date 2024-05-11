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
// EXERCISE: Random Messages
//
//  Display a few different won and lost messages "randomly".
//
// HINTS
//  1. You can use a switch statement to do that.
//  2. Set its condition to the random number generator.
//  3. I would use a short switch.
//
// EXAMPLES
//  The Player wins: then randomly print one of these:
//
//  go run main.go 5
//    YOU WON
//  go run main.go 5
//    YOU'RE AWESOME
//
//  The Player loses: then randomly print one of these:
//
//  go run main.go 5
//    LOSER!
//  go run main.go 5
//    YOU LOST. TRY AGAIN?
// ---------------------------------------------------------

func main() {

	rand.Seed(time.Now().UnixNano())

	if len(os.Args) != 2 {
		fmt.Println("run main.go with a number!")
		return
	}

	u, err := strconv.Atoi(os.Args[1])

	if err != nil {
		fmt.Printf("%q is not a number", os.Args[1])
		return
	}

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
