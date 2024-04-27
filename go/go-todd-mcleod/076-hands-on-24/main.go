package main

import ( 
	"fmt" 
	"math/rand" 
)

func init() {
	fmt.Println("This is from the init funciton, Hello!")
}

func main() {
	x := rand.Intn(250)
	fmt.Printf("The name of the variable is x and the value is %v\n", x)

	if x > 0 && x < 101 {
		for i:=1; i<101; i++ {
			if i%10 != 0 {
				continue
			}
			fmt.Printf("sequence through, now %v\n", i)
		}
	} else if x > 100 && x < 201 {
		for i:=101; i<201; i++ {
			if i%10 != 0 {
				continue
			}
			fmt.Printf("sequence through, now %v\n", i)
		}
	} else if x > 201 && x < 251 {
		for i:=201; i<251; i++ {
			if i%10 != 0 {
				continue
			}
			fmt.Printf("sequence through, now %v\n", i)
		}
	}

	switch {
	case x > 0 && x < 101:
		for i:=1; i<101; i++ {
			if i%10 != 0 {
				continue
			}
			fmt.Printf("this time with switch/case, now %v\n", i)
		}
	case x > 100 && x < 201:
		for i:=101; i<201; i++ {
			if i%10 != 0 {
				continue
			}
			fmt.Printf("this time with switch/case, now %v\n", i)
		}
	case x > 201 && x < 251: 
		for i:=201; i<251; i++ {
			if i%10 != 0 {
				continue
			}
			fmt.Printf("this time with switch/case, now %v\n", i)
		}
	}

}