package main

import (
	"log"
	"testing"
)

func TestAdd(t *testing.T) {
	got := add(7, 5)
	want := 12
	if got != want {
		log.Fatalf("error, want %s, got %s", want, got)
	}
}
