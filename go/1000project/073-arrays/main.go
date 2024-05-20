package main

import "fmt"

func main(){
	var books [4]string

	fmt.Printf("type of books: %T\n", books)
	fmt.Println("books:", books)
	fmt.Printf("books: %q\n", books)
	fmt.Printf("books: %#v\n", books) // %#v prints the type and value!o

	books[0] = "Kafka's Revenge"
	fmt.Printf("books: %q\n", books)
	fmt.Printf("books: %q\n", books[0])

	books[1] = "Stay Golden"
	books[2] = "Everythingship"
	books[3] = books[0] + " 2nd edition"

	fmt.Printf("books: %q\n", books)

	var (
		wBooks [1]string
		sBooks [3]string
	)

	wBooks[0] = books[0]

	for i := 0; i<len(sBooks); i++ {
		sBooks[i] = books[i+1]
	}

	fmt.Printf("wBooks: %q\n", wBooks)
	fmt.Printf("sBooks: %q\n", sBooks)

	// for range
	for i := range sBooks {
		sBooks[i] = books[i+1]
	}
	fmt.Printf("wBooks: %q\n", wBooks)
	fmt.Printf("sBooks: %q\n", sBooks)

	var published [len(books)]bool

	published[0] = true
	published[len(books)-1] = true

	fmt.Println("\nPublished books: ")
	for i, ok := range published {
		if ok {
			fmt.Printf("+ %s\n", books[i])
		}
	}


}

