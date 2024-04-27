package main

import (
	"log"
	"testing"
)

func TestMulti5(t *testing.T){
	got := multi5(3) 
	want := 15
	if got != want {
		log.Fatalf("got %s, want %s", got, want)
	}

}