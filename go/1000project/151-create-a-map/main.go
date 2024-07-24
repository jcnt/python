package main

import "fmt"

func main(){

	dict := map[string]string{}

	dict["up"] = "fel"
	dict["down"] = "le"

	key := "good"
	value := dict[key]

	fmt.Printf("%q means %#v\n", key, value)

	fmt.Printf("Number of keys is %d\n", len(dict))
}