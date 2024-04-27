package main

import (
	"fmt"
	"math/rand"
)

func main() {

	for i := 1; i <= 42; i++ {
		
		x := rand.Intn(5)

    	switch x {
    	case 0:
    		fmt.Printf("%v, x is random number under 5, current value is 0\n", i)
    	case 1:
    		fmt.Printf("%v, x is random number under 5, current value is 1\n", i)
    	case 2:
    		fmt.Printf("%v, x is random number under 5, current value is 2\n", i)
    	case 3:
    		fmt.Printf("%v, x is random number under 5, current value is 3\n", i)
    	case 4:
    		fmt.Printf("%v, x is random number under 5, current value is 4\n", i)
    	}

	}

}