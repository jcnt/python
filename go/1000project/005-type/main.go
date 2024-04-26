package main

import "fmt"

func main() {
	speed := 100
	force := 2.5

	b := speed * int(force)
	fmt.Println(b)

	c := float64(speed) * force
	fmt.Println(c)

	// 	speed = float64(speed) * force <- this would fail
	speed = int(float64(speed) * force)
	fmt.Println(speed)
}
