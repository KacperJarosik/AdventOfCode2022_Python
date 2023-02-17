def part1():
    file = open("input_day8.txt", "r")
    forest = []
    amount_of_visible_trees = 0
    for line in file.readlines():
        trees_line = []
        for tree in line.strip():
            trees_line.append(int(tree))
        forest.append(trees_line)

    for trees_line_number in range(len(forest)):
        for tree_number in range(len(forest[trees_line_number])):
            if tree_number == 0 or tree_number == len(forest[trees_line_number]) - 1 \
                    or trees_line_number == 0 or trees_line_number == len(forest) - 1:
                amount_of_visible_trees += 1
            else:
                block = 0
                # searching left
                for counter in range(1, tree_number + 1):
                    if forest[trees_line_number][tree_number] > forest[trees_line_number][tree_number - counter] and (
                            tree_number - counter) == 0:
                        amount_of_visible_trees += 1
                        block = 1
                    if not forest[trees_line_number][tree_number] > forest[trees_line_number][tree_number - counter]:
                        break
                # searching right
                if block == 0:
                    for counter in range(tree_number + 1, len(forest[trees_line_number])):
                        if forest[trees_line_number][tree_number] > forest[trees_line_number][counter] and counter == len(forest[trees_line_number]) - 1:
                            amount_of_visible_trees += 1
                            block = 1
                        if not forest[trees_line_number][tree_number] > forest[trees_line_number][counter]:
                            break
                # searching up
                if block == 0:
                    for counter in range(1, trees_line_number + 1):
                        if forest[trees_line_number][tree_number] > forest[trees_line_number - counter][tree_number] and (trees_line_number - counter) == 0:
                            amount_of_visible_trees += 1
                            block = 1
                        if not forest[trees_line_number][tree_number] > forest[trees_line_number - counter][tree_number]:
                            break
                # searching down
                if block == 0:
                    for counter in range(trees_line_number + 1, len(forest)):
                        if forest[trees_line_number][tree_number] > forest[counter][tree_number] and counter == len(
                                forest) - 1:
                            amount_of_visible_trees += 1
                        if not forest[trees_line_number][tree_number] > forest[counter][tree_number]:
                            break
    file.close()
    return amount_of_visible_trees


def part2():
    file = open("input_day8.txt", "r")
    forest = []
    value_max = 0
    for line in file.readlines():
        trees_line = []
        for tree in line.strip():
            trees_line.append(int(tree))
        forest.append(trees_line)

    for trees_line_number in range(len(forest)):
        for tree_number in range(len(forest[trees_line_number])):
            value_right = 0
            value_left = 0
            value_up = 0
            value_down = 0
            if tree_number == 0 or tree_number == len(forest[trees_line_number]) - 1 \
                    or trees_line_number == 0 or trees_line_number == len(forest) - 1:
                pass
            else:
                # searching left
                for counter in range(1, tree_number + 1):
                    value_left += 1
                    if not forest[trees_line_number][tree_number] > forest[trees_line_number][tree_number - counter]:
                        break
                # searching right
                for counter in range(tree_number + 1, len(forest[trees_line_number])):
                    value_right += 1
                    if not forest[trees_line_number][tree_number] > forest[trees_line_number][counter]:
                        break
                # searching up
                for counter in range(1, trees_line_number + 1):
                    value_up += 1
                    if not forest[trees_line_number][tree_number] > forest[trees_line_number - counter][tree_number]:
                        break
                # searching down
                for counter in range(trees_line_number + 1, len(forest)):
                    value_down += 1
                    if not forest[trees_line_number][tree_number] > forest[counter][tree_number]:
                        break
                current_value = value_up * value_down * value_right * value_left
                if value_max < current_value:
                    value_max = current_value
    file.close()
    return value_max


if __name__ == "__main__":
    print("Result Part 1: ", part1())
    print("Result Part 2: ", part2())
