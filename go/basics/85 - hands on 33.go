package main

import "fmt"

func main() {
	for i:=0; i<30; i++ {
		if i % 2 == 0 {
			continue
		}
		fmt.Println("ranging through odd numbers", i)
	}
}
