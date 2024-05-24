package main

type ph [5]string

var zero = ph{
	"███",
	"█ █",
	"█ █",
	"█ █",
	"███",
}

var one = ph{
	"██ ",
	" █ ",
	" █ ",
	" █ ",
	"███",
}

var two = ph{
	"███",
	"  █",
	"███",
	"█  ",
	"███",
}

var three = ph{
	"███",
	"  █",
	"███",
	"  █",
	"███",
}

var four = ph{
	"█ █",
	"█ █",
	"███",
	"  █",
	"  █",
}

var five = ph{
	"███",
	"█  ",
	"███",
	"  █",
	"███",
}

var six = ph{
	"███",
	"█  ",
	"███",
	"█ █",
	"███",
}

var seven = ph{
	"███",
	"  █",
	"  █",
	"  █",
	"  █",
}

var eight = ph{
	"███",
	"█ █",
	"███",
	"█ █",
	"███",
}

var nine = ph{
	"███",
	"█ █",
	"███",
	"  █",
	"███",
}

var sep = ph{
	"   ",
	" ░ ",
	"   ",
	" ░ ",
	"   ",
}

var digits = [...]ph{zero, one, two, three, four, five, six, seven, eight, nine}
