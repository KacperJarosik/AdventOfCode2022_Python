def part1():
    rock_points = 1
    paper_points = 2
    scissors_points = 3
    win_points = 6
    draw_points = 3
    # lose points -> 0
    my_points = 0
    file = open("day2.txt", "r")
    for line in file:
        if line[0] == "A":
            if line[2] == "X":
                my_points += draw_points + rock_points
            elif line[2] == "Y":
                my_points += win_points + paper_points
            elif line[2] == "Z":
                my_points += scissors_points
        elif line[0] == "B":
            if line[2] == "X":
                my_points += rock_points
            elif line[2] == "Y":
                my_points += draw_points + paper_points
            elif line[2] == "Z":
                my_points += win_points+scissors_points
        elif line[0] == "C":
            if line[2] == "X":
                my_points += win_points + rock_points
            elif line[2] == "Y":
                my_points += paper_points
            elif line[2] == "Z":
                my_points += draw_points+scissors_points
    file.close()
    return my_points


def part2():
    pass


if __name__ == "__main__":
    print("Result Part 1: ", part1())
    print("Result Part 2: ", part2())
