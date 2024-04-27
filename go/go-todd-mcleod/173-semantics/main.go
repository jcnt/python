package main

import "fmt"

func add(n int) int {
	return n + 1
}

func addPoint(v *int){
	*v += 1
}

func main() {
	//value semantics
	x := 1
	fmt.Println(add(x))
	fmt.Println(x)

	//pointer semantics
	y := 2
	fmt.Println(y)
	addPoint(&y)
	fmt.Println(y)


}
