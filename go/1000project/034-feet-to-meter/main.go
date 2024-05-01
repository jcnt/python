package main

import (
	"fmt"
	"os"
	"strconv"
)

func main(){

	if len(os.Args) != 2 {
		fmt.Println("Usage feet-to-meeter [parameter], parameter is number")
		return
	}

	f, err := strconv.ParseFloat(os.Args[1], 64) 

	if err != nil {
		fmt.Printf("ERROR: your parameter was %v and the type is %T\n", os.Args[1], os.Args[1])
		return
	}

	m := f / 3.281
	fmt.Printf("Your value converted to feet is %.2f\n", m)


}