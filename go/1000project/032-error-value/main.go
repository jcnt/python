package main

import (
	"fmt"
	"os"
	"strconv"
)

func main(){
	n, err := strconv.Atoi(os.Args[1])
	fmt.Println("converted number:", n)
	fmt.Println("returned error value:", err)

}