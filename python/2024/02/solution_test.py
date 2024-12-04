from solution import part_1, part_2

##################
# Helper Methods #
##################


def get_input(filename: str):
    file = open(filename)
    return file.read()


def run_test(fun, input: str, want: int):
    got = fun(input)
    assert got == want


#########
# Tests #
#########

sample_input = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
"""

actual_input = get_input("input.txt")


def test_part_1():
    inputs = {
        "7 6 4 2 1": 1,
        "1 2 7 8 9": 0,
        "9 7 6 2 1": 0,
        "1 3 2 4 5": 0,
        "8 6 4 4 1": 0,
        "1 3 6 7 9": 1,
        actual_input: 660,
    }

    for k, v in inputs.items():
        run_test(part_1, k, v)


def test_part_2():
    inputs = {
        "7 6 4 2 1": 1,
        "1 2 7 8 9": 0,
        "9 7 6 2 1": 0,
        "1 3 2 4 5": 1,
        "8 6 4 4 1": 1,
        "1 3 6 7 9": 1,
        actual_input: 689,
    }

    for k, v in inputs.items():
        run_test(part_2, k, v)
