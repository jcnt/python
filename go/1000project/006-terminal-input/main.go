package main

import (
	"fmt"
	"os"
)

func main() {
	fmt.Printf("%#v\n", os.Args)
	fmt.Println("first argument: ", os.Args[1])

	for i := 0; i < len(os.Args); i++ {
		fmt.Println("Argument number", i, "is: ", os.Args[i])
	}
}
