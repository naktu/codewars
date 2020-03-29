//Write a function called repeatString which repeats the given String src exactly count times.
//
//repeatStr(6, "I") // "IIIIII"
//repeatStr(5, "Hello") // "HelloHelloHelloHelloHello"

package kata

func RepeatStr(repetitions int, value string) string {
	var res string
	for i := 0; i < repetitions; i++ {
		res += value
	}
	return res
}
