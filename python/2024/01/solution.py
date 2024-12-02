from typing import Tuple


def parse_lists(input: str) -> Tuple[list, list]:
    lines = input.splitlines()
    a, b = [], []
    for line in lines:
        items = line.split()
        a.append(int(items[0]))
        b.append(int(items[1]))
    return a, b


def part_1(input: str) -> int:
    result = 0
    left, right = parse_lists(input)
    left.sort()
    right.sort()
    for index, _ in enumerate(left):
        result += abs(left[index] - right[index])
    return result


def get_item_count(item: int, item_count: dict) -> int:
    if item in item_count:
        return item_count[item]
    return 0


def get_occurrences(right: list) -> dict:
    result = {}
    for item in right:
        if item not in result:
            result[item] = 0
        result[item] += 1
    return result


def part_2(input: str) -> int:
    left_list, right_list = parse_lists(input)

    right_count = get_occurrences(right_list)

    result = 0
    for left_item in left_list:
        result += left_item * get_item_count(left_item, right_count)

    return result
