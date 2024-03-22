package main

import "fmt"

func main() {
	for i := 0; i < 5; i++ {
		fmt.Printf("First loop, iteration %v\n", i)
		for j := 0; j < 5; j++ {
			fmt.Printf("Second (nested) loop, iteration %v\n", j)
		}
	}

	// ranging through a slice
	xi := []int{42, 43, 44, 45, 46, 47}
	for i, v := range xi {
		fmt.Println("Slice Index and Value are: ", i, v)
	}

	// ranging through a map
	m := map[string]int{
		"James": 42,
		"Moneypenny": 	32,
	}
	for k, vv := range m {
		fmt.Println("Map Key and Value are: ", k, vv)
	}

	age := m["James"]
	fmt.Println(age)

	if v, ok := m["Jones"]; ok {
		fmt.Println("it is in the map, value is: ", v)
	} else {
		fmt.Println("it is not in the map, default nul value is: ", v)
	}

}
