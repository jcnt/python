package main

import (
	"bytes"
	"fmt"
)

func main() {
	b := bytes.NewBufferString("Hello ")
	fmt.Println(b.String())
	b.WriteString("Gophers!")
	fmt.Println(b.String())
	b.Reset()
	b.WriteString("This is a completely new string")
	fmt.Println(b.String())

	b.Write([]byte("Happy Happy"))
	fmt.Println(b.String())
}
