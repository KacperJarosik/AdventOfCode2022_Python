def part1():
    last_4_characters = []
    file = open("input_day06.txt", "r")
    line = file.readline()
    file.close()
    output = 0
    different_letters = 0
    for index in range(len(line)):
        if len(last_4_characters) < 4:
            last_4_characters.append(line[index])
            continue
        for previous in range(4):
            if last_4_characters.count(line[index - previous - 1]) != 1:
                last_4_characters.pop(0)
                last_4_characters.append(line[index])
                break
            if previous == 3:
                different_letters = 1
                output = index
        if different_letters == 1:
            return output
    return


def part2():
    last_14_characters = []
    file = open("input_day06.txt", "r")
    line = file.readline()
    file.close()
    output = 0
    different_letters = 0
    for index in range(len(line)):
        if len(last_14_characters) < 14:
            last_14_characters.append(line[index])
            continue
        for previous in range(14):
            if last_14_characters.count(line[index - previous - 1]) != 1:
                last_14_characters.pop(0)
                last_14_characters.append(line[index])
                break
            if previous == 13:
                different_letters = 1
                output = index
        if different_letters == 1:
            return output
    return


if __name__ == "__main__":
    print("Result Part 1: ", part1())
    print("Result Part 2: ", part2())
