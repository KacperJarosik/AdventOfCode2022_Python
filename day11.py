def part1():
    class Monkey:
        def __init__(self, description_of_monkey):
            first_line, second_line, third_line, fourth_line, fifth_line, sixth_line = description_of_monkey.split('\n')
            self.items = [int(item) for item in second_line[18:].split(',')]
            self.operation = lambda old, mathematical_operation=third_line[19:]: eval(mathematical_operation)
            self.divisible = int(fourth_line[20:])
            self.true = int(fifth_line[28:])
            self.false = int(sixth_line[29:])
            self.act = 0

    monkeys = [*map(Monkey, open("input_day11.txt").read().split('\n\n'))]

    for number in range(20):
        for monkey in monkeys:
            for item in monkey.items:
                item = int(monkey.operation(item) / 3)
                destination = monkey.false if item % monkey.divisible else monkey.true
                monkeys[destination].items += [item]
                monkey.act += 1
            monkey.items = []

    worry_level_top1, worry_level_top2, *number = sorted(-monkey.act for monkey in monkeys)
    return worry_level_top1 * worry_level_top2


def part2():
    # inspireted from reddit
    from math import prod

    class Monkey:
        def __init__(self, description_of_monkey):
            first_line, second_line, third_line, fourth_line, fifth_line, sixth_line = description_of_monkey.split('\n')
            self.items = [int(item) for item in second_line[18:].split(',')]
            self.operation = lambda old, b=third_line[19:]: eval(b)
            self.divisible = int(fourth_line[20:])
            self.true = int(fifth_line[28:])
            self.false = int(sixth_line[29:])
            self.act = 0

    monkeys = [*map(Monkey, open("input_day11.txt").read().split('\n\n'))]
    p = prod(m.divisible for m in monkeys)

    for number in range(10000):
        for monkey in monkeys:
            for item in monkey.items:
                item = monkey.operation(item) % p
                dest = monkey.false if item % monkey.divisible else monkey.true
                monkeys[dest].items += [item]
                monkey.act += 1
            monkey.items = []

    worry_level_top1, worry_level_top2, *number = sorted(-monkey.act for monkey in monkeys)
    return worry_level_top1 * worry_level_top2


if __name__ == "__main__":
    print("wait 5 seconds to receive full solutions")
    print("Result Part 1: ", part1())
    print("Result Part 2: ", part2())

