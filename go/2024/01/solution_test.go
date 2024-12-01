package solution

import (
	"log"
	"os"
	"testing"
)

const SampleInput = `3   4
4   3
2   5
1   3
3   9
3   3
`

// Helper function for reading the input file to a string
func readInputFile() string {
	data, err := os.ReadFile("input.txt")
	if err != nil {
		log.Fatalf("Couldn't read input.txt file, %v\n", err)
	}
	return string(data)
}

func TestPart1(t *testing.T) {
	t.Run("sample input", func(t *testing.T) {
		got := Part1(SampleInput)
		want := 11

		assertSolution(t, got, want)
	})
	t.Run("actual input", func(t *testing.T) {
		got := Part1(readInputFile())
		want := 1603498

		assertSolution(t, got, want) // Ravioli, ravioli - give me the formuoli!
	})
}

func TestPart2(t *testing.T) {
	t.Run("sample input", func(t *testing.T) {
		got := Part2(SampleInput)
		want := 31

		assertSolution(t, got, want)
	})
	t.Run("actual input", func(t *testing.T) {
		got := Part2(readInputFile())
		want := 25574739

		assertSolution(t, got, want) // Ravioli, ravioli - give me the formuoli!
	})
}

func assertSolution(t testing.TB, got int, want int) {
	t.Helper()

	if got != want {
		t.Errorf("got %d, wanted %d", got, want)
	}
}
