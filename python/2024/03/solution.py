import re


def part_1(input: str) -> int:
    valid_memory = parse_valid_memory(input)

    result = 0
    for mem in valid_memory:
        result += parse_and_multiply_memory(mem)
    return result


def parse_valid_memory(input: str) -> list[str]:
    return re.findall("mul\\(\\d+,\\d+\\)", input)


def parse_and_multiply_memory(input: str) -> int:
    number_strings = re.findall("\\d+", input)

    return int(number_strings[0]) * int(number_strings[1])


def part_2(input: str) -> int:
    clean_memory = remove_donts(input)

    return part_1(clean_memory)


def remove_donts(input: str) -> str:
    return re.sub("don't\\(\\)(.*?)(do\\(\\)|\\Z)", "", input)
