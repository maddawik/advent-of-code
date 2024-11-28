def Part1(input: str) -> int:
    floor = 0
    for c in input:
        match c:
            case "(":
                floor += 1
            case ")":
                floor -= 1
    return floor


def Part2(input: str) -> int:
    floor = 0
    index = 0
    for c in input:
        index += 1
        match c:
            case "(":
                floor += 1
            case ")":
                floor -= 1
        if floor < 0:
            break
    return index
