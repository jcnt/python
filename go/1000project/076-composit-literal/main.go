package main

import "fmt"

func main(){

	book := [4]string{"Kafka's Revenge", "Stay Gold"}
	fmt.Println(book)
	fmt.Printf("%q\n", book)

	book2 := [...]string{"Kafka's Revenge", "Stay Gold"}
	fmt.Println(book2)
	fmt.Printf("%q\n", book2)
}