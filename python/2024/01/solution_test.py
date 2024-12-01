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

sample_input = """3    4
4    3
2    5
1    3
3    9
3    3
"""


def test_part_1():
    real_input = get_input("input.txt")

    inputs = {
        "3   7": 4,
        "9   3": 6,
        "2   2": 0,
        sample_input: 11,
        real_input: 0,  # Ravioli, ravioli... GIVE ME THE FORMUOLI!!
    }

    for k, v in inputs.items():
        run_test(part_1, k, v)


def test_part_2():
    real_input = get_input("input.txt")

    inputs = {
        sample_input: 31,
        real_input: 0,  # Ravioli, ravioli... GIVE ME THE FORMUOLI!!
    }

    for k, v in inputs.items():
        run_test(part_2, k, v)
