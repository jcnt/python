package main

import "fmt"

func main(){

	i:=142

	switch{
	case i>100:
		fmt.Print("big ")
		fallthrough            // this means it will jump to the next block withouth checking 
	case i>0:
		fmt.Print("positive ")
		fallthrough
	default:
		fmt.Println("number")
	}
}