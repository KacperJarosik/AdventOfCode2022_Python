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
                    elif head_position[1] < tail_positions[-1][1]:
                        x = tail_positions[-1][0] + 1
                        y = tail_positions[-1][1] - 1
                    else:
                        x = tail_positions[-1][0] + 1
                        y = tail_positions[-1][1]

                    if [x, y] in tail_positions:
                        tail_positions.remove([x, y])
                    tail_positions.append([x, y])

            if direction == "L":
                head_position[0] -= 1
                if head_position[0] < tail_positions[-1][0] - 1:
                    if head_position[1] > tail_positions[-1][1]:
                        x = tail_positions[-1][0] - 1
                        y = tail_positions[-1][1] + 1
                    elif head_position[1] < tail_positions[-1][1]:
                        x = tail_positions[-1][0] - 1
                        y = tail_positions[-1][1] - 1
                    else:
                        x = tail_positions[-1][0] - 1
                        y = tail_positions[-1][1]

                    if [x, y] in tail_positions:
                        tail_positions.remove([x, y])
                    tail_positions.append([x, y])

            if direction == "U":
                head_position[1] += 1
                if head_position[1] > tail_positions[-1][1] + 1:
                    if head_position[0] > tail_positions[-1][0]:
                        x = tail_positions[-1][0] + 1
                        y = tail_positions[-1][1] + 1
                    elif head_position[0] < tail_positions[-1][0]:
                        x = tail_positions[-1][0] - 1
                        y = tail_positions[-1][1] + 1
                    else:
                        x = tail_positions[-1][0]
                        y = tail_positions[-1][1] + 1

                    if [x, y] in tail_positions:
                        tail_positions.remove([x, y])
                    tail_positions.append([x, y])

            if direction == "D":
                head_position[1] -= 1
                if head_position[1] < tail_positions[-1][1] - 1:
                    if head_position[0] > tail_positions[-1][0]:
                        x = tail_positions[-1][0] + 1
                        y = tail_positions[-1][1] - 1
                    elif head_position[0] < tail_positions[-1][0]:
                        x = tail_positions[-1][0] - 1
                        y = tail_positions[-1][1] - 1
                    else:
                        x = tail_positions[-1][0]
                        y = tail_positions[-1][1] - 1

                    if [x, y] in tail_positions:
                        tail_positions.remove([x, y])
                    tail_positions.append([x, y])

    amount_tailpositions = len(tail_positions)
    file.close()
    return amount_tailpositions


def part2():
    def add_new_tail_position(xp, yp):
        if [xp, yp] in tail_positions[tail]:
            tail_positions[tail].remove([xp, yp])
        tail_positions[tail].append([xp, yp])

    file = open("input_day9.txt", "r")
    # (x,y) coordinate system
    tail_positions = [[[0, 0]], [[0, 0]], [[0, 0]], [[0, 0]], [[0, 0]],
                      [[0, 0]], [[0, 0]], [[0, 0]], [[0, 0]]]
    head_position = [0, 0]
    last_knot = [0, 0]
    for series_of_moves in file.readlines():
        direction = series_of_moves[0]
        number_of_moves = int(series_of_moves[2:])

        for number in range(number_of_moves):
            for tail in range(len(tail_positions)):

                #head position - right
                if direction == "R":
                    if tail == 0:
                        head_position[0] += 1
                        last_knot = head_position
                    else:
                        last_knot = tail_positions[tail - 1][-1]

                # head position - left
                if direction == "L":
                    if tail == 0:
                        head_position[0] -= 1
                        last_knot = head_position
                    else:
                        last_knot = tail_positions[tail - 1][-1]

                # head position - up
                if direction == "U":
                    if tail == 0:
                        head_position[1] += 1
                        last_knot = head_position
                    else:
                        last_knot = tail_positions[tail - 1][-1]

                # head position - down
                if direction == "D":
                    if tail == 0:
                        head_position[1] -= 1
                        last_knot = head_position
                    else:
                        last_knot = tail_positions[tail - 1][-1]

                # tail - move right
                if last_knot[0] > tail_positions[tail][-1][0] + 1:
                    if last_knot[1] > tail_positions[tail][-1][1]:
                        x = tail_positions[tail][-1][0] + 1
                        y = tail_positions[tail][-1][1] + 1
                    elif last_knot[1] < tail_positions[tail][-1][1]:
                        x = tail_positions[tail][-1][0] + 1
                        y = tail_positions[tail][-1][1] - 1
                    else:
                        x = tail_positions[tail][-1][0] + 1
                        y = tail_positions[tail][-1][1]
                    add_new_tail_position(x, y)
                # tail - move left
                elif last_knot[0] < tail_positions[tail][-1][0] - 1:
                    if last_knot[1] > tail_positions[tail][-1][1]:
                        x = tail_positions[tail][-1][0] - 1
                        y = tail_positions[tail][-1][1] + 1
                    elif last_knot[1] < tail_positions[tail][-1][1]:
                        x = tail_positions[tail][-1][0] - 1
                        y = tail_positions[tail][-1][1] - 1
                    else:
                        x = tail_positions[tail][-1][0] - 1
                        y = tail_positions[tail][-1][1]

                    add_new_tail_position(x, y)
                # tail - move up
                elif last_knot[1] > tail_positions[tail][-1][1] + 1:
                    if last_knot[0] > tail_positions[tail][-1][0]:
                        x = tail_positions[tail][-1][0] + 1
                        y = tail_positions[tail][-1][1] + 1
                    elif last_knot[0] < tail_positions[tail][-1][0]:
                        x = tail_positions[tail][-1][0] - 1
                        y = tail_positions[tail][-1][1] + 1
                    else:
                        x = tail_positions[tail][-1][0]
                        y = tail_positions[tail][-1][1] + 1

                    add_new_tail_position(x, y)
                # tail - move down
                elif last_knot[1] < tail_positions[tail][-1][1] - 1:
                    if last_knot[0] > tail_positions[tail][-1][0]:
                        x = tail_positions[tail][-1][0] + 1
                        y = tail_positions[tail][-1][1] - 1
                    elif last_knot[0] < tail_positions[tail][-1][0]:
                        x = tail_positions[tail][-1][0] - 1
                        y = tail_positions[tail][-1][1] - 1
                    else:
                        x = tail_positions[tail][-1][0]
                        y = tail_positions[tail][-1][1] - 1

                    add_new_tail_position(x, y)

    amount_last_tailpositions = len(tail_positions[-1])
    file.close()
    return amount_last_tailpositions


if __name__ == "__main__":
    print("Result Part 1: ", part1())
    print("Result Part 2: ", part2())
