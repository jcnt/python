package main

import (
	"fmt"
	"os"
	"strconv"
)

func main() {

	if len(os.Args) != 2 {
		fmt.Println("Give me a year number")
		return
	}

	arg := os.Args[1]

	y, err := strconv.Atoi(arg)
	if err != nil {
		fmt.Printf("%q is nut a valid year.\n", arg)
		return
	}

	if y%4 == 0 && (y%100 != 0 || y%400 == 0) {
		fmt.Printf("%d is a leap year\n", y)
	} else {
		fmt.Printf("%d is not a leap year\n", y)
	}

}
