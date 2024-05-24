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
// EXERCISE: Housing Prices and Averages
//
//  Use the previous exercise to solve this exercise (Housing Prices).
//
//  Your task is to print the averages of the sizes, beds, baths, and prices.
//
//
// EXPECTED OUTPUT
//
//  Location       Size           Beds           Baths          Price
//  ===========================================================================
//  New York       100            2              1              100000
//  New York       150            3              2              200000
//  Paris          200            4              3              400000
//  Istanbul       500            10             5              1000000
//
//  ===========================================================================
//                 237.50         4.75           2.75           425000.00
//
// ---------------------------------------------------------

func main() {
	const (
		header = "Location,Size,Beds,Baths,Price"
		data   = `New York,100,2,1,100000
New York,150,3,2,200000
Paris,200,4,3,400000
Istanbul,500,10,5,1000000
Budapest,200,5,2,100000`

		separator = ","
	)

	d := strings.Split(data, "\n")

	for _, v := range strings.Split(header, separator) {
		fmt.Printf("%-15s", v)
	}
	fmt.Println()
	fmt.Println(strings.Repeat("=", 65))

	for _, v := range d {
		w := strings.Split(v, separator)
		for _, x := range w {
			fmt.Printf("%-15s", x)
		}
		fmt.Println()
	}

	fmt.Println()
	fmt.Println(strings.Repeat("=", 65))

	var as, ab, at, ap float64
	for _,v := range d {
		w := strings.Split(v, separator)
		x,_ := strconv.ParseFloat(w[1], 64)
		as += x
		y,_ := strconv.ParseFloat(w[2], 64)
		ab += y
		z,_ := strconv.ParseFloat(w[3], 64)
		at += z
		u,_ := strconv.ParseFloat(w[4], 64)
		ap += u
	}
	fmt.Printf("%-15s%-15.2f%-15.2f%-15.2f%-15.2f\n", "Average: ", as/float64(len(d)), ab/float64(len(d)), at/float64(len(d)), ap/float64(len(d)) )
}
