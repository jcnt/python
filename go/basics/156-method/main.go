package main

import "fmt"

type person struct {
	first string
	age   int
}

func (p person) speak() {
	fmt.Println("I am", p.first, "and I am", p.age, "years old.")
}

func main() {
	p1 := person{
		first: "Karcsi",
		age:   42,
	}

	p2 := person{
		first: "Bela",
		age:   45,
	}

	p1.speak()
	p2.speak()

}
