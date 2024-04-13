package main

import "fmt"

func main() {
	xi := []int{42, 43, 44, 45, 46, 47}
	for i, v := range xi {
		fmt.Println("ranging over a slice", i, v)
	}

	m := map[string]int{
		"James":	42, 
		"Jones": 	32,
	}
	for k, v := range m {
		fmt.Println("ranging over a map", k, v)
	}
}