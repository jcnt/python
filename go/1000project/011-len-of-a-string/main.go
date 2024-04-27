package main

import (
	"fmt"
	"unicode/utf8"
)

func main() {
	name := "carl"
	fmt.Println(len(name))

	name2 := "Jácint"
	fmt.Println(name2, "has the length of", len(name2))

	name3 := "Jacint"
	fmt.Println(name3, "has the length of", len(name3))

	fmt.Println(name2, "using now utf8 RuneCountInString", utf8.RuneCountInString(name2))
}
