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
// EXERCISE: Observe the length and capacity
//
//  Follow the instructions inside the code below to
//  gain more intuition about the length and capacity of a slice.
//
// ---------------------------------------------------------

func main() {
	// --- #1 ---
	// 1. create a new slice named: games

	var games1 []string

	// 2. print the length and capacity of the games slice

	fmt.Printf("The length of the slice is %d and the capacity is %d\n", len(games1), cap(games1))

	// 3. comment out the games slice
	//    then declare it as an empty slice

	games2 := []string{}

	// 4. print the length and capacity of the games slice

	fmt.Printf("The length of the slice is %d and the capacity is %d\n", len(games2), cap(games2))

	// 5. append the elements: "pacman", "mario", "tetris", "doom"

	games2 = append(games2, "pacman", "mario", "tetris", "doom")

	// 6. print the length and capacity of the games slice

	fmt.Printf("The length of the slice is %d and the capacity is %d\n", len(games2), cap(games2))

	// 7. comment out everything
	//
	// 8. declare the games slice again using a slice literal
	//    (use the same elements from step 5)

	games3 := []string{"pacman", "mario", "tetris", "doom"}

	// --- #2 ---
	fmt.Println("\nSection 2")
	// 1. use a loop from 0 to 4 to slice the games slice, element by element.

	for i := range games3 {
		f := i
		t := i + 1
		fmt.Printf("%q\n", games3[f:t])

		// 2. print its length and capacity along the way (in the loop).

		// for ... {
		// 	fmt.Printf("games[:%d]'s len: %d cap: %d\n", ...)
		fmt.Printf("Length is %d and capacity is %d\n", len(games3), cap(games3))
		// }
	}

	// --- #3 ---
	// 1. slice the games slice up to zero element
	//    (save the result to a new slice named: "zero")

	zero := games3[0:0]

	// 2. print the games and the new slice's len and cap

	fmt.Println("\nSection 3")

	fmt.Printf("games3 length is %d and capacity is %d\n", len(games3), cap(games3))
	fmt.Printf("zero length is %d and capacity is %d\n", len(zero), cap(zero))

	// 3. append a new element to the new slice

	zero = append(zero, "angrybirds")

	// 4. print the new slice's lens and caps

	fmt.Printf("zero length is %d and capacity is %d\n", len(zero), cap(zero))

	// 5. repeat the last two steps 5 times (use a loop)

	fillup := []string{"pinball", "driver", "fifa", "gta", "luigi"}

	for _, v := range fillup {
		zero = append(zero, v)
		fmt.Println("adding", v)
		fmt.Printf("zero length is %d and capacity is %d\n", len(zero), cap(zero))
	}

	// 6. notice the growth of the capacity after the 5th append
	//
	// Use this slice's elements to append to the new slice:
	fill2 := []string{"ultima", "dagger", "pong", "coldspot", "zetra"}

	// zero := ...
	// fmt.Printf("games's     len: %d cap: %d\n", ...)
	// fmt.Printf("zero's      len: %d cap: %d\n", ...)

	for _, v := range fill2 {
		zero = append(zero, v)
		fmt.Println("adding", v)
		fmt.Printf("zero length is %d and capacity is %d\n", len(zero), cap(zero))
	}

	// --- #4 ---
	fmt.Println("\nSection 4")
	// using a range loop, slice the zero slice element by element,
	// and print its length and capacity along the way.
	//
	// observe that, the range loop only loops for the length, not the cap.
	fmt.Println()

	for i, v := range zero {
		fmt.Printf("%d: %s\tlength is %d and cap is %d\n", i, v, len(zero), cap(zero))
	}


	// --- #5 ---
	fmt.Println("\nSection 5")
	// 1. do the 3rd step above again but this time, start by slicing
	//    the zero slice up to its capacity (use the cap function).
	//
	// 2. print the elements of the zero slice in the loop.
	fmt.Println()

	for i := range zero {
	   fmt.Printf("zero[:%d]'s  len: %d cap: %d - %q\n", i, len(zero[:i]), cap(zero[:i]), zero[:i])
	}

	// --- #6 ---
	fmt.Println("\nSection 5")
	// 1. change the one of the elements of the zero slice

	zero[1] = "Aladdin"
	//
	// 2. change the same element of the games slice

	games3[1] = "Aladdin"
	
	// 3. print the games and the zero slices

	fmt.Println(zero)
	fmt.Println(games3)
	//
	// 4. observe that they don't have the same backing array
	fmt.Println()
	// ...
	fmt.Printf("zero  : %q\n", zero)
	fmt.Printf("games : %q\n", games3)

	// --- #7 ---
	// try to slice the games slice beyond its capacity
}
