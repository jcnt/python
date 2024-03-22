package main

import (
	"fmt"
	"math/rand"
	// "math/rand"
)

func main() {

//	password := []string{}
	password := ""
	countl := 0 
	countn := 0 
	counts := 0

	letters := []string{"a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G",     "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"}
	numbers := []string{"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"}
	symbols := []string{"!", "#", "$", "%", "&", "(", ")", "*", "+"}
	for i := 0; i < ( 20 + rand.Intn(5)); i++ {
		j := rand.Intn(3)
		switch {
		case j == 0: 
//			password = append(password, letters[rand.Intn(len(letters))])
			password += letters[rand.Intn(len(letters))]
			countl += 1
		case j == 1:
//			password = append(password, numbers[rand.Intn(len(numbers))])
			if countn == 3 {
				password += letters[rand.Intn(len(letters))]
				countl += 1
			} else {
				password += numbers[rand.Intn(len(numbers))]
				countn += 1
			}
		case j == 2:
//			password = append(password, symbols[rand.Intn(len(symbols))])
			if counts == 3 {
				password += letters[rand.Intn(len(letters))]
				countl += 1
			} else {
				password += symbols[rand.Intn(len(symbols))]
				counts += 1
			}

		}
	}
	fmt.Println(password)
	fmt.Printf("lettes: %v, numbers: %v, symbols: %v\n", countl, countn, counts)
}