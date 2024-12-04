def part_1(input: str) -> int:
    lines = input.splitlines()

    reports = []

    for line in lines:
        reports.append(parse_report(line))

    result = 0
    for report in reports:
        result += validate_report(report)

    return result


def parse_report(input: str) -> list[int]:
    level_strings = input.split()

    result = []

    for level in level_strings:
        result.append(int(level))

    return result


def validate_delta(ascending, difference):
    if difference == 0:
        return False
    elif not (0 < abs(difference) < 4):
        return False
    elif difference > 0 and ascending:
        return False
    elif difference < 0 and not ascending:
        return False
    return True


def validate_report(report: list[int]) -> bool:
    ascending = False
    differences = []
    index = 0

    while index < len(report) - 1:
        differences.append(report[index] - report[index + 1])

        if index == 0 and differences[index] < 0:
            ascending = True

        if not validate_delta(ascending, differences[index]):
            return False

        index += 1
    return True


def part_2(input: str) -> int:
    lines = input.splitlines()

    reports = []

    for line in lines:
        reports.append(parse_report(line))

    result = 0
    for report in reports:
        result += validate_report_2_electric_boogaloo(report)

    return result


def validate_report_2_electric_boogaloo(report: list[int]) -> bool:
    if validate_report(report):
        return True

    for index, _ in enumerate(report):
        report_copy = report.copy()
        report_copy.pop(index)
        if validate_report(report_copy):
            return True

    return False
