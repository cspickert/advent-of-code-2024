from collections import defaultdict
from functools import cmp_to_key
from pathlib import Path


def part1(data):
    rules, updates = data
    result = 0
    for update in updates:
        if validate_update(rules, update):
            result += get_middle_value(update)
    return result


def part2(data):
    rules, updates = data
    result = 0
    for update in updates:
        if not validate_update(rules, update):
            fixed_update = get_fixed_update(rules, update)
            result += get_middle_value(fixed_update)
    return result


def validate_update(rules, update):
    for before, after in zip(update, update[1:]):
        if before in rules[after]:
            return False
    return True


def get_fixed_update(rules, update):
    def comparator(before, after):
        if before in rules[after]:
            return 1
        return -1

    return sorted(update, key=cmp_to_key(comparator))


def get_middle_value(values):
    return values[len(values) // 2]


def parse_data(input_file):
    rules_str, updates_str = input_file.read().split("\n\n")

    rules_lines = rules_str.split()
    rules_list = [rule_line.split("|") for rule_line in rules_lines]
    rules = defaultdict(set)
    for before, after in rules_list:
        rules[int(before)].add(int(after))

    updates_lines = updates_str.split()
    updates_list = [update_line.split(",") for update_line in updates_lines]
    updates = [[int(value) for value in update] for update in updates_list]

    return rules, updates


if __name__ == "__main__":
    input_file = (Path(__file__).parent / "input" / "day05.txt").open()
    data = parse_data(input_file)
    print(part1(data))
    print(part2(data))
