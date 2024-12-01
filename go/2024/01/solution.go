// Package solution contains solutions to part 1 and 2
package solution

import (
	"log"
	"sort"
	"strconv"
	"strings"
)

func parseInput(input string) (left []int, right []int) {
	// Remove whitespace
	lines := strings.Split(strings.Trim(string(input), "\n"), "\n")

	for _, line := range lines {
		stringSlice := strings.Fields(line)
		leftItem, err := strconv.Atoi(stringSlice[0])
		if err != nil {
			log.Fatalf("Couldn't convert left_item %v to int, %v", leftItem, err)
		}
		rightItem, err := strconv.Atoi(stringSlice[1])
		if err != nil {
			log.Fatalf("Couldn't convert right_item %v to int, %v", rightItem, err)
		}

		left = append(left, leftItem)
		right = append(right, rightItem)
	}

	return left, right
}

// Part1 returns the solution for day 1 part 1
func Part1(input string) int {
	answer := 0
	leftSlice, rightSlice := parseInput(input)

	sort.Slice(leftSlice, func(i, j int) bool {
		return leftSlice[i] < leftSlice[j]
	})
	sort.Slice(rightSlice, func(i, j int) bool {
		return rightSlice[i] < rightSlice[j]
	})

	for i := range leftSlice {
		left, right := leftSlice[i], rightSlice[i]
		if left < right {
			answer += right - left
		} else {
			answer += left - right
		}
	}

	return answer
}

// Part2 returns the solution for day 1 part 2
func Part2(input string) int {
	answer := 0
	leftSlice, rightSlice := parseInput(input)

	leftCount := map[int]int{}

	// Get unique values
	for _, v := range leftSlice {
		if _, ok := leftCount[v]; !ok {
			leftCount[v] = 0
		}
	}

	for key := range leftCount {
		for _, rightV := range rightSlice {
			if key == rightV {
				// Count occurrences
				leftCount[key]++
			}
		}
	}

	for _, v := range leftSlice {
		answer += v * leftCount[v]
	}

	return answer
}
