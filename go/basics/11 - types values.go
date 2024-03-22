package main

import "fmt"

func main() {
//	var s string = "hello"
//	var i int = 42
//	var f float64 = 3.14

	s, i, f := "hello", 42, 3.14

	fmt.Printf("s is a %T with a value of %v\n", s, s)
	fmt.Printf("i is a %T with a value of %v\n", i, i)
	fmt.Printf("f is a %T with a value of %v\n", f, f)

	d, b, h := 747, 911, 90210
	fmt.Printf("%v in decimal is %d\n", d, d)
	fmt.Printf("%v in binary is %b\n", b, b)
	fmt.Printf("%v in hexadecimal is %X\n", h, h)
	fmt.Println("\nAll of them: ")
	fmt.Printf("%d\t\t%d\t\t%d\n%b\t%b\t%b\n%X\t\t%X\t\t%X\n", d, b, h, d, b, h, d, b, h)

	var l int8 = 127
	var m uint8 = 255
	fmt.Printf("l has a value of %v and a type of %T\n", l, l)
	fmt.Printf("m has a value of %v and a type of %T\n", m, m)
}