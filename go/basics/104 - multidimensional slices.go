package main

import "fmt"

func main(){
	jb := []string{"James", "Bond", "Martini", "Chocolate"}
	jm := []string{"Jenny", "Moneypenny", "Guiness", "Vanilla"}
	fmt.Println(jb)
	fmt.Println(jm)

	people := [][]string{jb, jm}
	fmt.Println(people)
}