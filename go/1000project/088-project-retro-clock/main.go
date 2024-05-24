package main

import (
	"fmt"
	"os"
	"os/exec"
	"runtime"
	"time"
)

func main(){
	type ph [5]string

	zero := ph{
		"███",
		"█ █",
		"█ █",
		"█ █",
		"███",
	}

	one := ph{
		"██ ",
		" █ ",
		" █ ",
		" █ ",
		"███",
	}

	two := ph{
		"███",
		"  █",
		"███",
		"█  ",
		"███",
	}

	three := ph{
		"███",
		"  █",
		"███",
		"  █",
		"███",
	}

	four := ph{
		"█ █",
		"█ █",
		"███",
		"  █",
		"  █",
	}

	five := ph{
		"███",
		"█  ",
		"███",
		"  █",
		"███",
	}

	six := ph{
		"███",
		"█  ",
		"███",
		"█ █",
		"███",
	}

	seven := ph{
		"███",
		"  █",
		"  █",
		"  █",
		"  █",
	}

	eight := ph{
		"███",
		"█ █",
		"███",
		"█ █",
		"███",
	}

	nine := ph{
		"███",
		"█ █",
		"███",
		"  █",
		"███",
	}

	sep := ph{
		"   ",
		" ░ ",
		"   ",
		" ░ ",
		"   ",
	}

	digits := [...]ph{zero, one, two, three, four, five, six, seven, eight, nine}

	for {

		ClearScreen()
    	now := time.Now()
    	h, m, s := now.Hour(), now.Minute(), now.Second()
    
    	clock := [...]ph{
    		digits[h/10], digits[h%10],
    		sep,
    		digits[m/10], digits[m%10],
    		sep,
    		digits[s/10], digits[s%10],
    	}
    
    	for line := range clock[0] {
    		for index, digit := range clock {
    			next := clock[index][line]
				if digit == sep && s%2 == 0{
					next = "   "
				}
    			fmt.Print(next, "  ")
    		}
    		fmt.Println()
    	}
    	fmt.Println()
		time.Sleep(time.Second)
	}
	
}

func ClearScreen(){
	if runtime.GOOS == "windows" {
		cmd := exec.Command("cmd", "/c", "cls")
		cmd.Stdout = os.Stdout
		cmd.Run()
	} else {
		cmd := exec.Command("clear")
		cmd.Stdout = os.Stdout
		cmd.Run()
	}
}