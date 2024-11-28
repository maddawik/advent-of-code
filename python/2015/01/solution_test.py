from solution import Part1, Part2

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


def test_part_1():
    """
    Should work for the examples
    """
    input = get_input("input.txt")

    inputs = {
        "(())": 0,
        "()()": 0,
        "(((": 3,
        "(()(()(": 3,
        "))(((((": 3,
        "())": -1,
        "))(": -1,
        ")))": -3,
        ")())())": -3,
        input: 0,  # Ravioli, ravioli... give me the formuoli!
    }

    for k, v in inputs.items():
        run_test(Part1, k, v)


def test_part_2():
    input = get_input("input.txt")

    inputs = {
        ")": 1,
        "()())": 5,
        input: 0,  # Ravioli, ravioli... give me the formuoli!
    }

    for k, v in inputs.items():
        run_test(Part2, k, v)
