package main

import "fmt"

func main() {
	fmt.Println("Here's an array")
	fmt.Println("------------------------")
	array := [...]string{"Almond Biscotti Café", "Banana Pudding ", "Balsamic Strawberry (GF)", "Bittersweet Chocolate (GF)", "Blueberry Pancake (GF)", "Bourbon Turtle (GF)", "Browned Butter Cookie Dough", "Chocolate Covered Black Cherry (GF)", "Chocolate Fudge Brownie", "Chocolate Peanut Butter (GF)", "Coffee (GF)", "Cookies & Cream", "Fresh Basil (GF)", "Garden Mint Chip (GF)", "Lavender Lemon Honey (GF)", "Lemon Bar", "Madagascar Vanilla (GF)", "Matcha (GF)", "Midnight Chocolate Sorbet (GF, V)", "Non-Dairy Chocolate Peanut Butter (GF, V)", "Non-Dairy Coconut Matcha (GF, V)", "Non-Dairy Sunbutter Cinnamon (GF, V)", "Orange Cream (GF) ", "Peanut Butter Cookie Dough", "Raspberry Sorbet (GF, V)", "Salty Caramel (GF)", "Slate Slate Different", "Strawberry Lemonade Sorbet (GF, V)", "Vanilla Caramel Blondie", "Vietnamese Cinnamon (GF)", "Wolverine Tracks (GF)"}
	fmt.Println(len(array))
	fmt.Println(array)
	fmt.Printf("%T\n", array)

	// same thing with slice: 
	fmt.Println("\nNow a slice")
	fmt.Println("------------------------")
	slice := []string{"Almond Biscotti Café", "Banana Pudding ", "Balsamic Strawberry (GF)", "Bittersweet Chocolate (GF)", "Blueberry Pancake (GF)", "Bourbon Turtle (GF)", "Browned Butter Cookie Dough", "Chocolate Covered Black Cherry (GF)"}
	fmt.Println(slice)
	fmt.Println(len(slice))
	fmt.Printf("%T\n", slice)
	for i, v := range slice {
		fmt.Printf("%v is index \t %v is value\n", i, v)
	}

	fmt.Println("\nLooping through odd numbers")
	fmt.Println("------------------------")
	for i, v := range slice {
		if i % 2 == 0 {
			fmt.Printf("odd indexes only, %v is value\n", v)
		}
	}
	//single item only: 
	fmt.Println("\nSingle item only")
	fmt.Println("------------------------")
	for i := range slice {
		if i % 5 == 0 {
			fmt.Println(slice[i])
		}
	}

	// using for for the index with len()
	fmt.Println("\nusing len()")
	fmt.Println("------------------------")
	for i := 0; i < len(slice); i++ {
		fmt.Println(slice[i])
	}

	fmt.Println("-------------------------")
	xi := []int{42, 43, 44, 45}
	fmt.Println(xi)
	fmt.Println("let's append now")
	xi = append(xi, 46, 47, 48)
	fmt.Println(xi)
	fmt.Println("-------------------------")
	fmt.Println("slicing a slice")
	fmt.Printf("xi - %v\n", xi[:4])
	fmt.Printf("xi - %v\n", xi[2:])
	fmt.Printf("xi - %v\n", xi[:])
	fmt.Println("-------------------------")
	fmt.Println("now delete from a slice")
	xi = append(xi[:4], xi[5:]...)
	fmt.Println(xi)


}
