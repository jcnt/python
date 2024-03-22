package main
import "fmt"
import "time"

func main() {
    fmt.Println("Hello, Go. 🤩")

//    const name = "Kim"
//	const age = 22
//
//	fmt.Printf("%s is %d years old.\n", name, age)
//
//    fmt.Println(`
//    test print
//    of 
//    multiple
//    lines
//    `)

    adams := 42
    fmt.Printf("42 as binary, %b \n", adams)
    fmt.Printf("42 as hexadecimal, %x \n", adams)

    a, b, c, d, e, f := 0, 1, 2, 3, 4, 15

    fmt.Printf("%v \t %b \t %x \n", a, a, a)
    fmt.Printf("%v \t %b \t %x \n", b, b, b)
    fmt.Printf("%v \t %b \t %x \n", c, c, c)
    fmt.Printf("%v \t %b \t %x \n", d, d, d)
    fmt.Printf("%v \t %b \t %x \n", e, e, e)
    fmt.Printf("%v \t %b \t %x \n", f, f, f)
    
    fmt.Println("The time is", time.Now())

}

