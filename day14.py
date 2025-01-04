from pathlib import Path
import re
from dataclasses import dataclass
from collections import Counter
from copy import deepcopy


def part1(data):
    data = deepcopy(data)
    for _ in range(100):
        data.move()
    return data.get_safety_factor()


def part2(data):
    data = deepcopy(data)
    for seconds in range(1, 10000):
        data.move()
        if data.is_showing_picture():
            return seconds


@dataclass
class Robot:
    position: tuple[int, int]
    velocity: tuple[int, int]

    def move(self):
        self.position = (
            self.position[0] + self.velocity[0],
            self.position[1] + self.velocity[1],
        )


@dataclass
class Game:
    robots: list[Robot]
    size: tuple[int, int] = (101, 103)

    def move(self):
        for robot in self.robots:
            robot.move()

    def get_position(self, robot):
        x = robot.position[0] % self.size[0]
        y = robot.position[1] % self.size[1]
        return (x, y)

    def get_quadrant(self, robot):
        x, y = self.get_position(robot)
        mid_x = self.size[0] // 2
        mid_y = self.size[1] // 2
        if x < mid_x and y < mid_y:
            return "top-left"
        if x > mid_x and y < mid_y:
            return "top-right"
        if x < mid_x and y > mid_y:
            return "bottom-left"
        if x > mid_x and y > mid_y:
            return "bottom-right"
        return None

    def get_safety_factor(self):
        counts = Counter(
            quad for robot in self.robots if (quad := self.get_quadrant(robot))
        )
        result = 1
        for quad, count in counts.items():
            result *= count
        return result

    def display(self):
        positions = set(self.get_position(robot) for robot in self.robots)
        for y in range(self.size[1]):
            line = ""
            for x in range(self.size[0]):
                if (x, y) in positions:
                    line += "x"
                else:
                    line += " "
            print(line)

    def is_showing_picture(self):
        positions = set(self.get_position(robot) for robot in self.robots)
        long_run = 0
        for y in range(self.size[1]):
            run = 0
            for x in range(self.size[0]):
                if (x, y) in positions and (x - 1, y) in positions:
                    run += 1
                    long_run = max(long_run, run)
                else:
                    run = 0
            if long_run > 10:
                return True
        return False


def parse_data(input_file):
    game = Game(robots=[])
    for line in input_file.readlines():
        values = tuple(int(chunk) for chunk in re.findall(r"(-?\d+)", line))
        robot = Robot(position=values[:2], velocity=values[2:])
        game.robots.append(robot)
    return game


if __name__ == "__main__":
    input_file = (Path(__file__).parent / "input" / "day14.txt").open()
    data = parse_data(input_file)
    print(part1(data))
    print(part2(data))
