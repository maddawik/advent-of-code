package solution

import "testing"

// Optionally convert these to table-driven tests
func TestPart1(t *testing.T) {
	t.Run("sample input", func(t *testing.T) {
		got := Part1()
		want := 0

		assertSolution(t, got, want)
	})
	t.Run("actual input", func(t *testing.T) {
		got := Part1()
		want := 0

		assertSolution(t, got, want)
	})
}

func TestPart2(t *testing.T) {
	t.Run("sample input", func(t *testing.T) {
		got := Part2()
		want := 1

		assertSolution(t, got, want)
	})
	t.Run("actual input", func(t *testing.T) {
		got := Part2()
		want := 1

		assertSolution(t, got, want)
	})
}

func assertSolution(t testing.TB, got int, want int) {
	t.Helper()

	if got != want {
		t.Errorf("got %d, wanted %d", got, want)
	}
}
