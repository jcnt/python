package main

import (
	"fmt"
	"path"
)


func main() {
	var dir, file string

	dir, file = path.Split("css/main.css")

	fmt.Println("file: ", file)
	fmt.Println("dir: ", dir)

	var _, file2 string
	_, file2 = path.Split("new/doc.txt")
	fmt.Println("file2: ", file2)
}
