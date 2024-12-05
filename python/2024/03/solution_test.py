from solution import part_1, part_2

##################
# Helper Methods #
##################


def get_input(filename: str) -> str:
    file = open(filename)
    lines = file.read().splitlines()

    result = ""
    for line in lines:
        result += line
    return result


def run_test(fun, input: str, want: int):
    got = fun(input)
    assert got == want


#########
# Tests #
#########

actual_input = get_input("input.txt")


def test_part_1():
    inputs = {
        "mul(44,46)": 2024,
        "mul(123,4)": 492,
        "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))": 161,
        actual_input: 175700056,
    }

    for k, v in inputs.items():
        run_test(part_1, k, v)


def test_part_2():
    inputs = {
        "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))": 48,
        actual_input: 71668682,
    }

    for k, v in inputs.items():
        run_test(part_2, k, v)
