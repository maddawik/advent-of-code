package solution

import "testing"

func TestPart1(t *testing.T) {
	t.Run("the test input works", func(t *testing.T) {
		got := Part1()
		want := 0

		if got != want {
			t.Errorf("got %d, wanted %d", got, want)
		}
	})
}

func TestPart2(t *testing.T) {
	t.Run("the test input works", func(t *testing.T) {
		got := Part2()
		want := 0

		if got != want {
			t.Errorf("got %d, wanted %d", got, want)
		}
	})
}
