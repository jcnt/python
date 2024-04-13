package main

import "fmt"

func main() {

	foo()
	bar("Todd")
	s := aloha("Todd")
	fmt.Println(s)

}

func foo() {
	fmt.Println("I'm from foo")
}

func bar(s string) {
	fmt.Println("I'm from bar and my name is", s)

}

func aloha(s string) string {
	return fmt.Sprint("I'm from Aloha and they call me Mr.", s)
}