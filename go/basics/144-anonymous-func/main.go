package main

import "fmt"

func main() {
	foo()

	func(){
		fmt.Println("Anonymus func ran")
	}()

	func(s string){
		fmt.Println("this is an anonymus func showing my name", s)
	}("Jacint")

}

func foo(){
	fmt.Println("Foo ran")
}