//
// these are the exmples from the "go tour" website

package main

import (
	"fmt"
	"math/rand"
	"math"
)

var c, python, java bool
const d int = 42
var j, k = 3, 2.0
var s string
const p = 3.14

func add (x, y int) int {
	return x + y
}

func swap (a, b string) (string, string) {
	return b, a
}

func split (sum int) (x, y int) {
	x = sum * 4 / 9
	y = sum - x
	return
}

func main() {
	fmt.Println("My favourite number is", rand.Intn(5))
	fmt.Printf("I have %g problems\n", math.Sqrt(9))
	fmt.Printf("Pi is %g\n", math.Pi)
	fmt.Println(add(42, 13))
	sayHello()
	fmt.Println(swap("Hello", "World"))
	fmt.Println(split(17))
	var i int
	fmt.Println(i, c, python, java, d)
	// short declaration is only available in the function
	m := 3  // - int
	n := "3"  // - string
	//printing out the variable types -> %T
	fmt.Printf("%T \t %T \t %T \t %T \t %T \t %T \t %T \t \n", j, k, c, python, java, m, n)
	fmt.Printf("a string is empty by default like this: %s <---\n", s)
	fmt.Println(p)
}

func sayHello() {
	fmt.Println("hello")
}
