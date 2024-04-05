package main

import "fmt"

func main() {

	x := func() {
		fmt.Println("This is from an anonymous func")
	}

	y := func(s string) {
		fmt.Println("This is from an anon func with parameter, called: ", s)
	}

	x()
	y("param")

}
