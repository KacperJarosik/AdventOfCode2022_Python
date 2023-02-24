def part1():
    max_equipment_calory = 0
    curent_equipment_calory = 0
    file = open("input_day01.txt", "r")
    for line in file:
        if line == "\n":
            if curent_equipment_calory > max_equipment_calory:
                max_equipment_calory = curent_equipment_calory
            curent_equipment_calory = 0
        else:
            curent_equipment_calory += int(line)
    file.close()
    return max_equipment_calory


def part2():
    max1_equipment_calory = 0
    max2_equipment_calory = 0
    max3_equipment_calory = 0
    curent_equipment_calory = 0
    file = open("input_day01.txt", "r")
    for line in file:
        if line == "\n":
            if curent_equipment_calory > max1_equipment_calory:
                max1_equipment_calory = max2_equipment_calory
                max2_equipment_calory = max3_equipment_calory
                max3_equipment_calory = curent_equipment_calory
                curent_equipment_calory = 0
            elif curent_equipment_calory > max2_equipment_calory:
                max2_equipment_calory = max3_equipment_calory
                max3_equipment_calory = curent_equipment_calory
                curent_equipment_calory = 0
            elif curent_equipment_calory > max3_equipment_calory:
                max3_equipment_calory = curent_equipment_calory
                curent_equipment_calory = 0
        else:
            curent_equipment_calory += int(line)
    file.close()
    return max1_equipment_calory + max2_equipment_calory + max3_equipment_calory


if __name__ == "__main__":
    print("Result Part 1: ", part1())
    print("Result Part 2: ", part2())
