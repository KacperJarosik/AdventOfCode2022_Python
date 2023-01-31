def part1():
    account_compartment_within_the_compartment = 0
    file = open("input_day4.txt", "r")
    for line in file:
        if line[-1] == "\n":
            line = line[:-1]
        line = line.replace(",", "-")
        line = line.split("-")
        first_down = int(line[0])
        first_up = int(line[1])
        second_down = int(line[2])
        second_up = int(line[3])
        if (first_down <= second_down <= first_up and first_down <= second_up <= first_up) or (
                second_down <= first_down <= second_up) and (second_up >= first_up >= second_down):
            account_compartment_within_the_compartment += 1
    file.close()
    return account_compartment_within_the_compartment


def part2():
    account_compartment_within_the_compartment = 0
    file = open("input_day4.txt", "r")
    for line in file:
        if line[-1] == "\n":
            line = line[:-1]
        line = line.replace(",", "-")
        line = line.split("-")
        first_down = int(line[0])  # first1
        first_up = int(line[1])  # second1
        second_down = int(line[2])  # first2
        second_up = int(line[3])  # second2
        if not (first_down > second_up or first_up < second_down or second_down > first_up or second_up < first_down):
            account_compartment_within_the_compartment += 1
    file.close()
    return account_compartment_within_the_compartment


if __name__ == "__main__":
    print("Result Part 1: ", part1())
    print("Result Part 2: ", part2())
