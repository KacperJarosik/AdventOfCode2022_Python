def part1():
    file = open("input_day9.txt", "r")
    # (x,y) coordinate system
    tail_positions = [[0, 0]]
    head_position = [0, 0]
    for series_of_moves in file.readlines():
        direction = series_of_moves[0]
        number_of_moves = int(series_of_moves[2:])
        for number in range(number_of_moves):
            if direction == "R":
                head_position[0] += 1
                if head_position[0] > tail_positions[-1][0] + 1:
                    if head_position[1] > tail_positions[-1][1]:
                        x = tail_positions[-1][0] + 1
                        y = tail_positions[-1][1] + 1
                        tail_positions.append([x, y])
                    elif head_position[1] < tail_positions[-1][1]:
                        x = tail_positions[-1][0] + 1
                        y = tail_positions[-1][1] - 1
                        tail_positions.append([x, y])
                    else:
                        x = tail_positions[-1][0] + 1
                        y = tail_positions[-1][1]
                        tail_positions.append([x, y])

            if direction == "L":
                head_position[0] -= 1
                if head_position[0] < tail_positions[-1][0] - 1:
                    if head_position[1] > tail_positions[-1][1]:
                        x = tail_positions[-1][0] - 1
                        y = tail_positions[-1][1] + 1
                        tail_positions.append([x, y])
                    elif head_position[1] < tail_positions[-1][1]:
                        x = tail_positions[-1][0] - 1
                        y = tail_positions[-1][1] - 1
                        tail_positions.append([x, y])
                    else:
                        x = tail_positions[-1][0] - 1
                        y = tail_positions[-1][1]
                        tail_positions.append([x, y])

            if direction == "U":
                head_position[1] += 1
                if head_position[1] > tail_positions[-1][1] + 1:
                    if head_position[0] > tail_positions[-1][0]:
                        x = tail_positions[-1][0] + 1
                        y = tail_positions[-1][1] + 1
                        tail_positions.append([x, y])
                    elif head_position[0] < tail_positions[-1][0]:
                        x = tail_positions[-1][0] - 1
                        y = tail_positions[-1][1] + 1
                        tail_positions.append([x, y])
                    else:
                        x = tail_positions[-1][0]
                        y = tail_positions[-1][1] + 1
                        tail_positions.append([x, y])

            if direction == "D":
                head_position[1] -= 1
                if head_position[1] < tail_positions[-1][1] - 1:
                    if head_position[0] > tail_positions[-1][0]:
                        x = tail_positions[-1][0] + 1
                        y = tail_positions[-1][1] - 1
                        tail_positions.append([x, y])
                    elif head_position[0] < tail_positions[-1][0]:
                        x = tail_positions[-1][0] - 1
                        y = tail_positions[-1][1] - 1
                        tail_positions.append([x, y])
                    else:
                        x = tail_positions[-1][0]
                        y = tail_positions[-1][1] - 1
                        tail_positions.append([x, y])

    amount_tailpositions = 0
    while len(tail_positions) != 0:
        if tail_positions.count(tail_positions[-1]) == 1:
            amount_tailpositions += 1
        tail_positions.pop()
    file.close()
    return amount_tailpositions


def part2():
    file = open("input_day9.txt", "r")

    file.close()
    return


if __name__ == "__main__":
    print("Result Part 1: ", part1())
    print("Result Part 2: ", part2())
