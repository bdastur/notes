package simpleutils

import (
	"fmt"
	"time"
)

/*
 * Spinner will spin till done.
 */
func Spinner(delay time.Duration) {
	for {
		for _, r := range `-\|/` {
			fmt.Printf("\r%c", r)
			time.Sleep(delay)
		}
	}
}
