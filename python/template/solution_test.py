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


def test_part_1():
    inputs = {
        "sample1": 0,
        "sample2": 0,
        "sample3": 0,
    }

    for k, v in inputs.items():
        run_test(part_1, k, v)


def test_part_2():
    inputs = {
        "sample1": 0,
        "sample2": 0,
        "sample3": 0,
    }

    for k, v in inputs.items():
        run_test(part_2, k, v)
