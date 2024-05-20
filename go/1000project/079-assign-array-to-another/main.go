package main

import "fmt"

func main(){

	prev := [3]string{"Kafka's Revenge", "Stay Golden", "Everythingship"}

	fmt.Printf("Last year: \n%#v\n", prev)

	books := prev

	for i := range books {
		books[i] += " 2nd edition"
	}
	
	fmt.Printf("This year: \n%#v\n", books)

	var books2 [4]string
	fmt.Println(books2)

	for i, b := range prev {
		books2[i] += b + " 2nd ed."
	}
	fmt.Println(books2)
}