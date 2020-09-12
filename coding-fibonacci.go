package main

import (
	"fmt"
	"time"
)

// ref: https://github.com/godsman-yang/coding-learn/blob/master/coding-fibonacci.py

func fibonacciCalc(num int) int {
	Counter++ // global varialble

	if num < 2 {
		return num
	}

	n0 := 0
	n1 := 1
	// n2 := 1
	result := 0

	// for i in range(3, num+1):
	for i := 2; i <= num; i++ {
		result = n0 + n1
		n0, n1 = n1, result
	}
	return result
}

func fibonacciRecursive(num int) int {
	Counter++

	if num < 2 {
		return num
	}
	result := fibonacciRecursive(num-1) + fibonacciRecursive(num-2)
	// return fibonacci_recursive(num-1) + fibonacci_recursive(num-2)
	return result
}

//global variable
var Memo map[int]int = map[int]int{0: 0, 1: 1}

func fibonacciRecursiveMemo(num int) int {
	Counter++

	if num < 2 {
		return Memo[num]
	}

	_, ok := Memo[num]
	if ok == false {
		Memo[num] = fibonacciRecursiveMemo(num-1) + fibonacciRecursiveMemo(num-2)
	}
	return Memo[num]
}

func fibonacciGolang(num int) int {
	Counter++

	a, b := 1, 0
	for i := 0; i < num; i++ {
		a, b = b, a+b
	}
	return b
}

// global variables
var Counter int

func main() {
	num := InputFibonacciNumber()
	fmt.Println("")

	Counter = 0
	startTime := time.Now()
	fibonacciNumber := fibonacciCalc(num)
	elapsedTime := time.Since(startTime)

	fmt.Println("Function call count(clac):", Counter)
	fmt.Printf("Elaspsed time(calc): %s\n", elapsedTime)
	fmt.Println("Result:", fibonacciNumber)
	fmt.Println()

	Counter = 0
	startTime = time.Now()
	fibonacciNumber = fibonacciRecursive(num)
	elapsedTime = time.Since(startTime)

	fmt.Println("Function call count(recursive):", Counter)
	fmt.Printf("Elaspsed time(recursive): %s\n", elapsedTime)
	fmt.Println("Result:", fibonacciNumber)
	fmt.Println()

	Counter = 0
	startTime = time.Now()
	fibonacciNumber = fibonacciRecursiveMemo(num)
	elapsedTime = time.Since(startTime)

	fmt.Println("Function call count(memo):", Counter)
	fmt.Printf("Elaspsed time(memo): %s\n", elapsedTime)
	fmt.Println("Result:", fibonacciNumber)
	fmt.Println()

	Counter = 0
	startTime = time.Now()
	fibonacciNumber = fibonacciGolang(num)
	elapsedTime = time.Since(startTime)

	fmt.Println("Function call count(golang):", Counter)
	fmt.Printf("Elaspsed time(golang): %s\n", elapsedTime)
	fmt.Println("Result:", fibonacciNumber)
	fmt.Println()
}

func InputFibonacciNumber() int {
	var number int

	fmt.Printf("Enter number for fibonacci> ")
	_, _ = fmt.Scanf("%d", &number)

	return number
}
