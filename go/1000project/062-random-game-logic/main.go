package main

import (
	"fmt"
	"math/rand"
	"os"
	"strconv"
	"time"
)

func main() {

	rand.Seed(time.Now().UnixNano())

	if len(os.Args) != 3 {
		fmt.Println("please pick a number")
		return
	}

	guess, err := strconv.Atoi(os.Args[1])

	if err != nil {
		fmt.Printf("%q is not a number\n", os.Args[1])
		return
	}

	guess2, err := strconv.Atoi(os.Args[2])

	if err != nil {
		fmt.Printf("%q is not a number\n", os.Args[1])
		return
	}

	for turn := 0; turn < 5; turn++ {

		n := rand.Intn(guess + 1)

		if n == guess || n == guess2 {
			fmt.Println("🎉 You win!!!")
			if turn == 0 {
				fmt.Println("Wooooo, you won on the first turn!")
			}
			return
		}
	}
	fmt.Println("💀 You lost, try again...")
}
