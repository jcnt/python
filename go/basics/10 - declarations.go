package main

import "fmt"

func main() {

	// var for zero value

	var c int
	fmt.Println(c)

	// short declaration

	k := "42"
	fmt.Println(k)

	// multiple inits

	var i, j = 42, "string"
	fmt.Printf("These two are %T and %T and the values are %v and %v\n", i, j, i, j)

	// var when specificy required

	var m float64 = 42.42
	fmt.Println(m)

	// blank identifier 

	var o, p, _ = 46, 47, 48
	fmt.Println(o, p)

}