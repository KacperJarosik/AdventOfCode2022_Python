def part1():
    file = open("input_day10.txt", "r")
    cycles_to_check = [20, 60, 100, 140, 180, 220]
    value_sum = 0
    cycles = 0
    value = 1

    for instruction in file.readlines():
        if instruction[:4] == "noop":
            cycles += 1
            if cycles in cycles_to_check:
                value_sum += value * cycles
        if instruction[:4] == "addx":
            cycles += 1
            if cycles in cycles_to_check:
                value_sum += value * cycles
            cycles += 1
            if cycles in cycles_to_check:
                value_sum += value * cycles
            value += int(instruction[4:])
    file.close()
    return value_sum


def part2():
    def check_to_draw(ctr, x):
        if abs(x - (ctr % 40)) <= 1:
            output[ctr] = "#"

    file = open("input_day10.txt", "r")
    output = []
    for index in range(240):
        output.append(" ")
    # after first cycle must be index 0
    cycles = -1
    value = 1

    for instruction in file.readlines():
        if instruction[:4] == "noop":
            cycles += 1
            check_to_draw(cycles, value)

        if instruction[:4] == "addx":
            cycles += 1
            check_to_draw(cycles, value)

            cycles += 1
            check_to_draw(cycles, value)

            value += int(instruction[4:])

    for index in range(240):
        if index % 40 == 0 and index > 0:
            print()
        if index % 5 == 4:
            print("\t", end="")
        print(output[index], end="")

    file.close()
    return


if __name__ == "__main__":
    print("Result Part 1: ", part1())
    print("Result Part 2: ")
    part2()
    print("\nCharacters which you can see above is your solution")
