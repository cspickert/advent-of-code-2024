from pathlib import Path


def part1(data):
    return sum(valid_report(report) for report in data)


def part2(data):
    return sum(valid_report_with_removal(report) for report in data)


def valid_report_with_removal(report):
    if valid_report(report):
        return True
    for i in range(len(report)):
        if valid_report(report[:i] + report[i + 1 :]):
            return True
    return False


def valid_report(report):
    return valid_report_increasing(report) or valid_report_increasing(report[::-1])


def valid_report_increasing(report):
    prev = report[0]
    for val in report[1:]:
        if not (1 <= (val - prev) <= 3):
            return False
        prev = val
    return True


def parse_data(input_file):
    data = []
    for line in input_file.readlines():
        values = line.split()
        data.append([int(value) for value in values])
    return data


if __name__ == "__main__":
    input_file = (Path(__file__).parent / "input" / "day02.txt").open()
    data = parse_data(input_file)
    print(part1(data))
    print(part2(data))
