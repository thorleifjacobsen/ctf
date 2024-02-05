package main

import (
	"fmt"
	"os"
)

type N struct {
	data string
	i    int
}

func (n N) get() string {
	return string(n.data[n.i])
}

func main() {
	flag, _ := os.ReadFile("flag.txt")
	n := N{string(flag), -1}
	t := func(n N) N {
		n.i += 1
		return n
	}
	for i := 0; i < len(n.data); i++ {
		n :  t(n)
		fmt.Print(n.get())
	}
	fmt.Println()
}