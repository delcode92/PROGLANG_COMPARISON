package main

import (
    "fmt"
    "runtime"
    "sync"
    "time"
)

func main() {
    var wg sync.WaitGroup
    
    // Create a large number of goroutines
    for i := 0; i < 20; i++ {
        wg.Add(1)

        go func(id int) {
            defer wg.Done()
            // Each goroutine just prints its ID
            number := 1

            for number <= 1 {
              fmt.Printf("Goroutine %d\n", id)
              time.Sleep(1*time.Second)
            }

        }(i)
    }

    // Wait for all goroutines to finish
    wg.Wait()

    // Print the number of OS threads used
    fmt.Printf("Number of OS threads used: %d\n", runtime.NumGoroutine())
}
