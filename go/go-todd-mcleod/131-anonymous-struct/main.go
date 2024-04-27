package main

import "fmt"

func main() {

	p1 := struct{
		first string
		friends map[string]int
		drinks []string
	}{

		first: "James",
		friends: map[string]int{
			"Jenny": 27, 
			"Q": 87, 
			"Ian": 47,
		},
		drinks: []string{
			"Martini",
			"Water",
		},
	}

	fmt.Println(p1)

	for k, v := range p1.friends {
		fmt.Printf("James' friend is %v with age %v\n", k, v)
	}

	for _, v := range p1.drinks {
		fmt.Printf("Bond's favorite drink is %v\n", v)
	}

	

}