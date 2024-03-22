package main

import "fmt"

func main() {
	// 42:
	// using composite literal create an array
	fmt.Println("\n--------------- 42 ---------------")
	newx := [5]int{}
	//assign values to each position
	for i := 0; i < 5; i++ {
		newx[i] = i
	}
	for i, v := range newx {
		fmt.Printf("index is %v\tvalue is %v\ttype is %T\n", i, v, v)
	}

	// 43:
	/*
		Using a COMPOSITE LITERAL:
		● create a SLICE of TYPE int
		● assign these 10 VALUES
		42, 43, 44, 45, 46, 47, 48, 49, 50, 51
		● Range over the slice and print the values out.
			○ print out the VALUE and the TYPE
	*/
	fmt.Println("\n--------------- 43 ---------------")
	fthree := []int{}
	fthree = append(fthree, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51)
	for _, v := range fthree {
		fmt.Printf("Value is %v\tType is %T\n", v, v)
	}

	// 44:
	/* Using the code from the previous example, use SLICING to create the following new slices which are then printed:
	● [4243444546]
	● [4748495051]
	● [4445464748]
	● [4344454647]
	*/
	fmt.Println("\n--------------- 44 ---------------")
	ffour := fthree
	fmt.Printf("ffour: %v\n", ffour[:5])
	fmt.Printf("ffour: %v\n", ffour[5:])
	fmt.Printf("ffour: %v\n", ffour[2:7])
	fmt.Printf("ffour: %v\n", ffour[1:6])

	fmt.Println("\n--------------- 45 ---------------")
	ffive := []int{42, 43, 44, 45, 46, 47, 48, 49, 50, 51}
	fmt.Println(ffive)
	ffive = append(ffive, 52)
	fmt.Println(ffive)
	ffive = append(ffive, 53, 54, 55)
	fmt.Println(ffive)
	ffivey := []int{56, 57, 58, 59, 60}
	ffive = append(ffive, ffivey...)
	fmt.Println(ffive)

	fmt.Println("\n--------------- 46 ---------------")
	fsixx := []int{42, 43, 44, 45, 46, 47, 48, 49, 50, 51}
	fmt.Println(fsixx)
	fsixx = append(fsixx[:3], fsixx[6:]...)
	fmt.Println(fsixx)

	fmt.Println("\n--------------- 47 ---------------")
	fseven := make([]string, 0, 50) // len : 0, cap : 50
	fseven = append(fseven, " Alabama", " Alaska", " Arizona", " Arkansas", " California", " Colorado", " Connecticut", " Delaware", " Florida", " Georgia", " Hawaii", " Idaho", " Illinois", " Indiana", " Iowa", " Kansas", " Kentucky", " Louisiana", " Maine", " Maryland", " Massachusetts", " Michigan", " Minnesota", " Mississippi", " Missouri", " Montana", " Nebraska", " Nevada", " New Hampshire", " New Jersey", " New Mexico", " New York", " North Carolina", " North Dakota", " Ohio", " Oklahoma", " Oregon", " Pennsylvania", " Rhode Island", " South Carolina", " South Dakota", " Tennessee", " Texas", " Utah", " Vermont", " Virginia", " Washington", " West Virginia", " Wisconsin", " Wyoming")
	fmt.Println(len(fseven))
	fmt.Println(cap(fseven))
	for i := 0; i < len(fseven); i++ {
		fmt.Println("USA: ", i+1, fseven[i])
	}

	fmt.Println("\n--------------- 48 ---------------")
	feightx := []string{"James", "Bond", "Shaken, not stirred"}
	fmt.Println(feightx)
	feighty := []string{"Miss", "Moneypenny", "I'm 008."}
	fmt.Println(feighty)
	feightfinal := [][]string{feightx, feighty}
	fmt.Println(feightfinal)

	for i, v := range feightfinal {
		fmt.Println(i, v)
		for _, b := range v {
			fmt.Println(b)
		}
	}

}
