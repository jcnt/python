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
	"strconv"
	"strings"
)

// ---------------------------------------------------------
// EXERCISE: Slice the numbers
//
//   We've a string that contains even and odd numbers.
//
//   1. Convert the string to an []int
//
//   2. Print the slice
//
//   3. Slice it for the even numbers and print it (assign it to a new slice variable)
//
//   4. Slice it for the odd numbers and print it (assign it to a new slice variable)
//
//   5. Slice it for the two numbers at the middle
//
//   6. Slice it for the first two numbers
//
//   7. Slice it for the last two numbers (use the len function)
//
//   8. Slice the evens slice for the last one number
//
//   9. Slice the odds slice for the last two numbers
//
//
// EXPECTED OUTPUT
//   go run main.go
//
//     nums        : [2 4 6 1 3 5]
//     evens       : [2 4 6]
//     odds        : [1 3 5]
//     middle      : [6 1]
//     first 2     : [2 4]
//     last 2      : [3 5]
//     evens last 1: [6]
//     odds last 2 : [3 5]
//
//
// NOTE
//
//  You can also use my prettyslice package for printing the slices.
//
//
// HINT
//
//  Find a function in the strings package for splitting the string into []string
//
// ---------------------------------------------------------

func main() {
	// uncomment the declaration below
	data := "2 4 6 1 3 5"
	d := strings.Split(data, " ")

	fmt.Printf("%T\t%v\n", d, d)
	var i, e, o, m, f, l []int
	for _,v := range d {
		j, _ := strconv.Atoi(v)
		i = append(i, j)

	}
	fmt.Printf("%T\t%v\n", i, i)

	for _,v := range i {
		if v % 2 == 0 {
			e = append(e, v)
		}
	}
	fmt.Printf("%T\t%v\n", e, e)

	e = i[:3]
	fmt.Printf("%T\t%v\n", e, e)

	o = i[3:]
	fmt.Printf("%T\t%v\n", o, o)

	m = i[2:4]
	fmt.Printf("%T\t%v\n", m, m)

	f = i[:2]
	fmt.Printf("%T\t%v\n", f, f)
	
	l = i[len(d)-2:]
	fmt.Printf("%T\t%v\n", l, l)

	e = e[len(e)-1:]
	fmt.Printf("%T\t%v\n", e, e)

	o = o[len(o)-2:]
	fmt.Printf("%T\t%v\n", o, o)
	
}
