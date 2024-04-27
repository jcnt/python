package main

import "fmt"

func main() {

	const (
		monday    = 0
		tuesday   = 1
		wednesday = 2
		thursday  = 3
		friday    = 4
		saturday  = 5
		sunday    = 6
	)

	fmt.Println(monday, tuesday, wednesday, thursday, friday, saturday, sunday)

	const (
		mon = iota
		tue
		wed
		thu
		fri
		sat
		sun
	)

	fmt.Println(mon, tue, wed, thu, fri, sat, sun)

	const (
		_ = iota // you can also set mon to "iota + 1"
		mo
		tu
		we
		th
		fr
		sa
		su
	)

	fmt.Println(mo, tu, we, th, fr, sa, su)

	const (
		EST = -(5 + iota) 	// - (5 + 0) = -5
		_					// - (5 + 1) = -6
		MST
		PST
	)

	fmt.Println(EST, MST, PST)

}
