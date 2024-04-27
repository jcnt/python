package main

import ("fmt"; "math/rand")

func main() {
	for i := 0; i < 100; i++ {
		fmt.Printf("Looping through numbers, the currrent is %v\n", i)
	}

	for j := 0; j < 100; j++ {
		x := rand.Intn(10)
    	y := rand.Intn(10)
    	fmt.Println("The two random numbers are: ", x, y)
    
    	switch {
    	case x < 4 && y < 4: 
    		fmt.Println("both less than 4")
    	case x > 6 && y > 6: 
    		fmt.Println("Both larger than 6")
    	case x >= 4 && y <= 6:
    		fmt.Println("x >= 4 and y <= 6")
    	case y != 5: 
    		fmt.Println("y is not 5")
    	default: 
    		fmt.Println("none of the previous ones are correct")
    	}
	}
}