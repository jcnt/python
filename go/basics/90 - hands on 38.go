package main

import (
	"fmt"
	"math/rand"
)

func main() {
	c := 0
	for i := 0; i < 100; i++ {
		// statement; statement idiom:
		if x := rand.Intn(5); x == 3 {
			c++
			fmt.Printf("x is 3 now\t iteration is %v\t total is %v \n", i, c)
		}
	}

	// booleans
	fmt.Println(true && true)
	fmt.Println(true && false)
	fmt.Println(true || true)
	fmt.Println(true || false)
	fmt.Println(!true)
}
