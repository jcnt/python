package main

import "fmt"

func main(){
	f := foo(5)
	s, b := bar("bar")
	fmt.Println(f)
	fmt.Println(s)
	fmt.Println(b)
}

func foo(n int) int {
	r := n*3
	return r
}

func bar(s string) (int, string) {
	r := len(s)
	return r, s
}