package main

import (
	"fmt"
	"os"
	"strings"
)

func main() {
	msg := os.Args[1]
	l := len(msg)

	s := msg + strings.Repeat("!", l) // adds the number of ! the len of the msg

	fmt.Println(s)

	s = strings.ToUpper(s)
	fmt.Println(s)

	// excercise

	e := strings.Repeat("!", l)
	fmt.Println(e + msg + e)

}
