package main

import "fmt"

func main() {
	// deferred functions run LIFO, foo will run first after non-deferred func
	defer bar()
	defer foo()
	nofoo()
	
}

func foo(){
	fmt.Println("this is foo")
}

func bar(){
	fmt.Println("this is bar")
}

func nofoo(){
	fmt.Println("this is nofoo")
}