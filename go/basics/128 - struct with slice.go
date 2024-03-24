package main

import "fmt"


type person struct {
	first string
	last string
	icecream []string
}

func main() {

	p1 := person {
		first : "James", 
		last : "Bond", 
		icecream : []string{"vanilla", "chocolate", "banana"},
	}

	p2 := person {
		first : "Jenny", 
		last : "Moneypenny", 
		icecream : []string{"strawberry", "raspberry", "apple"},
	}


	fmt.Println(p1)
	fmt.Println(p2)

	fmt.Println(p1.icecream)
	fmt.Println(p2.icecream)

	for _, v := range p1.icecream {
		fmt.Println(p1.first, "favourite ice cream is", v)
	}

	for _, v := range p2.icecream {
		fmt.Println(p2.first, "favourite ice cream is", v)
	}

	m := map[string]person {
		p1.last: p1, 
		p2.last: p2, 
	}

	fmt.Println(m)

	for k, v := range m {
		fmt.Println(k, v)
	}
}