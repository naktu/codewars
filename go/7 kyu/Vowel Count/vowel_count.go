//Return the number (count) of vowels in the given string.
//
//We will consider a, e, i, o, and u as vowels for this Kata.
//
//The input string will only consist of lower case letters and/or spaces.
package kata

import (
	"strings"
)

func GetCount(str string) (count int) {
	count = 0
	for _, letter := range "aeiou" {
		count += strings.Count(str, string(letter))
	}
	return count
}
