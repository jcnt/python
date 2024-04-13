package main

import (
	"fmt"
	"log"
	"os"
)

func main() {
	xb, err := readFile("151 poem.txt")
	if err != nil {
		log.Fatalf("error in main readfile %s", err)
	}
	fmt.Println(xb)
	fmt.Println(string(xb))
}

func readFile(filename string) ([]byte, error) {
	xb, err := os.ReadFile(filename)
	if err != nil {
		return nil, fmt.Errorf("there was an error with readfile: %s", err)
	}
	return xb, nil
}
