def part1():
    sum_priorities = 0
    priorities = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12,
                  'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23,
                  'x': 24, 'y': 25, 'z': 26, 'A': 27, 'B': 28, 'C': 29, 'D': 30, 'E': 31, 'F': 32, 'G': 33, 'H': 34,
                  'I': 35, 'J': 36, 'K': 37, 'L': 38, 'M': 39, 'N': 40, 'O': 41, 'P': 42, 'Q': 43, 'R': 44, 'S': 45,
                  'T': 46, 'U': 47, 'V': 48, 'W': 49, 'X': 50, 'Y': 51, 'Z': 52}
    file = open("input_day03.txt", "r")
    for line in file:
        middle = int(len(line) / 2)
        rucksack_first_compartment = line[:middle]
        rucksack_second_compartment = line[middle:]
        used_letter = []
        for letter in rucksack_first_compartment:
            if letter in rucksack_second_compartment and letter not in used_letter:
                used_letter.append(letter)
                sum_priorities += priorities[letter]
    file.close()
    return sum_priorities


def part2():
    first_rucksack = ''
    second_rucksack = ''
    third_rucksack = ''
    sum_priorities_of_groups = 0
    rucksack_number = 0
    priorities = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12,
                  'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23,
                  'x': 24, 'y': 25, 'z': 26, 'A': 27, 'B': 28, 'C': 29, 'D': 30, 'E': 31, 'F': 32, 'G': 33, 'H': 34,
                  'I': 35, 'J': 36, 'K': 37, 'L': 38, 'M': 39, 'N': 40, 'O': 41, 'P': 42, 'Q': 43, 'R': 44, 'S': 45,
                  'T': 46, 'U': 47, 'V': 48, 'W': 49, 'X': 50, 'Y': 51, 'Z': 52}
    file = open("input_day03.txt", "r")
    for rucksack in file:
        if rucksack[-1] == '\n':
            rucksack = rucksack[:-1]
        if rucksack_number % 3 == 0:
            first_rucksack = rucksack
        if rucksack_number % 3 == 1:
            second_rucksack = rucksack
        if rucksack_number % 3 == 2:
            third_rucksack = rucksack
            used_letter = []
            for letter in priorities.keys():
                if letter in first_rucksack and letter in second_rucksack and letter in third_rucksack:
                    used_letter.append(letter)
                    sum_priorities_of_groups += priorities[letter]
        rucksack_number += 1
    file.close()
    return sum_priorities_of_groups


if __name__ == "__main__":
    print("Result Part 1: ", part1())
    print("Result Part 2: ", part2())
