package main

import "fmt"

func main(){
	x := func(s string){
		fmt.Println("Anonymous func with a single parameter:", s)
		for i := 1; i<10; i++ {
			fmt.Println("This is a for loop inside the anon func where i is", i)
		}
	} 

	x("parameter")

	
}
