package main

import (
	"fmt"
)

func main(){
	c := multi5(3) 
	fmt.Println(c)
}

func multi5(r int) int {
	return r * 5
}