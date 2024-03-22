package main

import "fmt"

func main(){
	fmt.Println("--------------- 49 ---------------")
	map49 := make(map[string][]string)
	map49["bond_james"] = []string{"shaken, not stirred", "martinis", "fast cars"}
	map49["moneypenny_jenny"] = []string{"intelligence", "literature", "computer science"}
	map49["no_dr"] = []string{"cats", "ice cream", "sunsets"}
	
	fmt.Printf("%#v\n\n", map49)

	for k, v := range map49 {
		fmt.Printf("Key is %v and values are:\n", k)
		for i, v2 := range v {
			fmt.Printf("i: %v\tv: %v\n", i, v2)
		}
	}

	fmt.Println("\n--------------- 50 ---------------")
	fmt.Println("Insert a new record\n")
	map49["fleming_ian"] = []string{"steaks", "cigars", "espionage"}

	for k, v := range map49 {
		fmt.Printf("Key is %v and values are:\n", k)
		for i, v2 := range v {
			fmt.Printf("i: %v\tv: %v\n", i, v2)
		}
	}
	fmt.Println("\n--------------- 51 ---------------")
	fmt.Println("delete a row\n")
	delete(map49, "moneypenny_jenny")
	for k, v := range map49 {
		fmt.Printf("Key is %v and values are:\n", k)
		for i, v2 := range v {
			fmt.Printf("i: %v\tv: %v\n", i, v2)
		}
	}
	

}