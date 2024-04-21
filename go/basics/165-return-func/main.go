package main

import "fmt"

func main(){
	x := retfunc("test string")
	fmt.Println(x())

}

func retfunc(s string) func() string {
	return func() string {
		return s
	}
}