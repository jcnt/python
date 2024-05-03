package main

import (
	"fmt"
	"os"
)

func main() {

	city := os.Args[1]

	switch city {
	default:
		fmt.Println("Where?")
	case "Paris", "Lyon":
		fmt.Println("France")
	case "Tokyo":
		fmt.Println("Japan")
	}
}
