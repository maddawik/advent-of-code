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
    answer = 0
    left, right = parse_lists(input)
    left.sort()
    right.sort()
    for index, _ in enumerate(left):
        answer += abs(left[index] - right[index])
    return answer


def part_2(input: str) -> int:
    answer = 0
    left, right = parse_lists(input)
    left_uniq = set(left)
    item_count = {}

    for left_item in left_uniq:
        item_count[left_item] = 0
        for right_item in right:
            if left_item == right_item:
                item_count[left_item] += 1

    for item in left:
        answer += item * item_count[item]

    return answer
