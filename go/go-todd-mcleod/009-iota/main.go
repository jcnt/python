package main

import "fmt"

const (
	c0 = iota // c0 == 0
	c1 = iota // c1 == 1
	c2 = iota // c2 == 2
)

const (
	_ = iota // c0 == 0
	a
	b
	c
	d
	e
	f
)

const (
	_      = iota
	KB int = 1 << (10 * iota)
	MB
	GB
	TB
	PB
	EB
)

func main() {
	fmt.Printf("%d \t %b\n", 1, 1)
	fmt.Printf("%d \t %b\n", 1<<a, 1<<a)
	fmt.Printf("%d \t %b\n", 1<<b, 1<<b)
	fmt.Printf("%d \t %b\n", 1<<c, 1<<c)
	fmt.Printf("%d \t %b\n", 1<<d, 1<<d)
	fmt.Printf("%d \t %b\n", 1<<e, 1<<e)
	fmt.Printf("%d \t %b\n", 1<<f, 1<<f)
	fmt.Printf("Type\tbase2\t\t\t\t\t\t\t\tbase10\n")
	fmt.Printf("byte:\t%b\t\t\t\t\t\t\t\t%d\n", 1, 1)
	fmt.Printf("KB:\t%b\t\t\t\t\t\t\t%d\n", KB, KB)
	fmt.Printf("MB:\t%b\t\t\t\t\t\t%d\n", MB, MB)
	fmt.Printf("GB:\t%b\t\t\t\t\t%d\n", GB, GB)
	fmt.Printf("TB:\t%b\t\t\t%d\n", TB, TB)
	fmt.Printf("PB:\t%b\t\t%d\n", PB, PB)
	fmt.Printf("EB:\t%b\t%d\n", EB, EB)
}
