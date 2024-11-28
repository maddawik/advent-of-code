// Package solution contains solutions to part 1 and 2
package solution

import (
	"log"
	"os"
	"testing"
)

func getInput() string {
	data, err := os.ReadFile("input.txt")
	if err != nil {
		log.Fatal(err)
	}
	return string(data)
}

func TestPart1(t *testing.T) {
	input := getInput()
	type args struct {
		in0 string
	}
	tests := []struct {
		name string
		args args
		want int
	}{
		{"sample 1", args{"(())"}, 0},
		{"sample 2", args{"()()"}, 0},
		{"sample 3", args{"((("}, 3},
		{"sample 4", args{"(()(()("}, 3},
		{"sample 5", args{"))((((("}, 3},
		{"sample 6", args{"())"}, -1},
		{"sample 7", args{"))("}, -1},
		{"sample 8", args{")))"}, -3},
		{"sample 9", args{")())())"}, -3},
		{"actual input", args{input}, 0}, // Ravioli, ravioli - give me the formuoli!
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := Part1(tt.args.in0); got != tt.want {
				t.Errorf("Part1() = %v, want %v", got, tt.want)
			}
		})
	}
}

func TestPart2(t *testing.T) {
	input := getInput()
	type args struct {
		in0 string
	}
	tests := []struct {
		name string
		args args
		want int
	}{
		{"sample 1", args{")"}, 1},
		{"sample 2", args{"()())"}, 5},
		{"actual input", args{input}, 0}, // Ravioli, ravioli - give me the formuoli!
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := Part2(tt.args.in0); got != tt.want {
				t.Errorf("Part2() = %v, want %v", got, tt.want)
			}
		})
	}
}
