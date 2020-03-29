//Create a function (or write a script in Shell) that takes an integer as an argument and returns "Even" for even
//numbers or "Odd" for odd numbers.

package kata

func EvenOrOdd(number int) string {
	if number < 0 {
		number = -number
	}
	result := number % 2
	if result > 0 {
		return "Odd"
	}
	return "Even"
}
