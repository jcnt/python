package main

import "fmt"

func main() {
	var s string
	s = "How are you?"
	fmt.Println(s)

	s = "<html>\n\t<body>\"Hello\"</body>\n</html>"
	fmt.Println(s)

	s=`
<html>
	<body>"Hello"</body>
</html>
	
	`
	fmt.Println(s)

	fmt.Println("C:\\dir\\myfile.txt")
	fmt.Println(`C:\dir\myfile.txt`)

}
