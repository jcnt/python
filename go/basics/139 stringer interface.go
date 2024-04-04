package main

import (
	"fmt"
	"log"
	"strconv"
)

type book struct {
	title string
}

func (b book) String() string {
	return fmt.Sprint("The title of the book is ", b.title)
}

type count int

func (c count) String() string {
	return fmt.Sprint("This is the number ", strconv.Itoa(int(c)))
}

func logInfo(s fmt.Stringer) {
	log.Println("LOG FROM 139", s.String())
}

func main() {
	b := book{
		title: "West With The Night",
	}

	var n count = 42

	fmt.Println(b)
	fmt.Println(n)

	log.Println(b)
	log.Println(n)

	logInfo(b)
	logInfo(n)
}
