def part1():
    stacks = [[], [], [], [], [], [], [], [], []]
    output = ""
    end_move_between_stacks = 0
    end_stack_reading = 0
    file = open("input_day5.txt", "r")
    for line in file:
        if line[0] == 'm':
            if line[-1] == '\n':
                line = line[:-1]
            else:
                end_move_between_stacks = 1
            command = line.split(' ')
            quantity = int(command[1])
            from_stack = int(command[3])
            to_stack = int(command[5])
            for k in range(quantity):
                stacks[to_stack - 1].append(stacks[from_stack - 1][-1])
                stacks[from_stack - 1].pop()
            if end_move_between_stacks == 1:
                for k in range(9):
                    output += stacks[k][-1]
        elif len(line) < 2:
            continue
        elif line[1] != '1' and end_stack_reading == 0:
            for index in range(9):
                if (1 + index * 4) < len(line):
                    stacks[index].append(line[1 + index * 4])
        else:
            end_stack_reading = 1
            for index in range(9):
                while " " in stacks[index]:
                    stacks[index].remove(" ")
                stacks[index].reverse()
    file.close()
    return output


def part2():
    stacks = [[], [], [], [], [], [], [], [], []]
    output = ""
    end_move_between_stacks = 0
    end_stack_reading = 0
    file = open("input_day5.txt", "r")
    for line in file.readlines():
        if line[0] == 'm':
            if line[-1] == '\n':
                line = line[:-1]
            else:
                end_move_between_stacks = 1
            command = line.split(' ')
            quantity = int(command[1])
            from_stack = int(command[3])
            to_stack = int(command[5])
            stacks[to_stack - 1].extend(stacks[from_stack - 1][-quantity:])
            stacks[from_stack - 1] = stacks[from_stack - 1][:-quantity]
            if end_move_between_stacks == 1:
                for k in range(9):
                    output += stacks[k][-1]
        elif len(line) < 2:
            continue
        elif line[1] != '1' and end_stack_reading == 0:
            for index in range(9):
                if (1 + index * 4) < len(line):
                    stacks[index].append(line[1 + index * 4])
        else:
            end_stack_reading = 1
            for index in range(9):
                while " " in stacks[index]:
                    stacks[index].remove(" ")
                stacks[index].reverse()
    file.close()
    return output


if __name__ == "__main__":
    print("Result Part 1: ", part1())
    print("Result Part 2: ", part2())
