package main

import (
    "fmt"
    "runtime"
    "time"
)

func worker(v int) {
  fmt.Printf("threead:%d  | value: %d\n", v, v + 1)
    time.Sleep(10 * time.Second)
}

func main() {
    fmt.Printf("Number of OS threads before: %d\n", runtime.NumGoroutine())

    for i := 0; i < 100; i++ {
        go worker(i)
    }

    fmt.Printf("Number of Goroutines after: %d\n", runtime.NumGoroutine())

    time.Sleep(3 * time.Second)

    fmt.Printf("Number of OS threads during: %d\n", runtime.NumGoroutine())
}

