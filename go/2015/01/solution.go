// Package solution contains solutions to part 1 and 2
package solution

// Part1 returns the solution for day 1 part 1
func Part1(input string) int {
	floor := 0
	for _, v := range input {
		switch v {
		case '(':
			floor++
		case ')':
			floor--
		}
	}
	return floor
}

// Part2 returns the solution for day 1 part 2
func Part2(input string) int {
	floor := 0
	for i, v := range input {
		switch v {
		case '(':
			floor++
		case ')':
			floor--
		}
		if floor <= -1 {
			return i + 1
		}
	}
	return 0
}
