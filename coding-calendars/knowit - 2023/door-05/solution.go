package main

import (
	"fmt"
	"math"
	"strconv"
)

// Check if number is prime
func isPrime(num int) bool {
	if num < 2 {
		return false
	}
	s := int(math.Sqrt(float64(num)))
	for i := 2; i <= s; i++ {
		if num%i == 0 {
			return false
		}
	}
	return true
}

// Criterias: sum of digits, divided by sum, is whole number, is prime
func isSumDividePrime(num int) bool {
	strNum := strconv.Itoa(num)
	sum := 0
	for _, digit := range strNum {
		digitInt, _ := strconv.Atoi(string(digit))
		sum += digitInt
	}
	dividedBySum := float64(num) / float64(sum)
	return dividedBySum == float64(int(dividedBySum)) && isPrime(int(dividedBySum))
}

func main() {
	sumDividePrimes := 0

	for i := 1; i <= 100000000; i++ {
		if isSumDividePrime(i) {
			sumDividePrimes++
		}
	}

	fmt.Println(sumDividePrimes)
}
