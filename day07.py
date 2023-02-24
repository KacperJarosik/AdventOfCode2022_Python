def part1():
    file = open("input_day07.txt", "r")
    commands = file.readlines()

    dirs = {"/home": 0}
    path = "/home"

    # Process every command
    for command in commands:

        # Commands that start with $
        if command[0] == "$":

            # Do nothing
            if command[2:4] == "ls":
                pass

            # Manage changing the path
            elif command[2:4] == "cd":

                # # Go back to the root
                if command[5] == "/":
                    path = "/home"

                # Go back in the path
                elif command[5:7] == "..":
                    path = path[0:path.rfind("/")]

                # Change the path
                else:
                    dir_name = command[5:]  # Get name of directory
                    path = path + "/" + dir_name  # Add to the path
                    dirs.update({path: 0})  # Update our dictionary


        # Do nothing when listing directories available
        elif command[0:3] == "dir":
            pass

        else:
            size = int(command[:command.find(" ")])  # Get size of file

            # Update size for every directory down to /home
            dir = path
            for i in range(path.count("/")):
                dirs[dir] += size
                dir = dir[:dir.rfind("/")]

    total = 0
    for dir in dirs:
        if dirs[dir] < 100000:
            total += dirs[dir]
    file.close()
    return total


def part2():
    file = open("input_day07.txt", "r")
    commands = file.readlines()

    dirs = {"/home": 0}
    path = "/home"

    # Process every command
    for command in commands:

        # Commands that start with $
        if command[0] == "$":

            # Do nothing
            if command[2:4] == "ls":
                pass

            # Manage changing the path
            elif command[2:4] == "cd":

                # # Go back to the root
                if command[5] == "/":
                    path = "/home"

                # Go back in the path
                elif command[5:7] == "..":
                    path = path[0:path.rfind("/")]

                # Change the path
                else:
                    dir_name = command[5:]  # Get name of directory
                    path = path + "/" + dir_name  # Add to the path
                    dirs.update({path: 0})  # Update our dictionary


        # Do nothing when listing directories available
        elif command[0:3] == "dir":
            pass

        else:
            size = int(command[:command.find(" ")])  # Get size of file

            # Update size for every directory down to /home
            dir = path
            for i in range(path.count("/")):
                dirs[dir] += size
                dir = dir[:dir.rfind("/")]

    # space required - space unused (total space - space used)
    limit = 30000000 - (70000000 - dirs["/home"])
    valid_dirs = []

    # Iterate through every path
    for dir in dirs:

        if limit <= dirs[dir]:
            valid_dirs.append(dirs[dir])

    smallest = min(valid_dirs)
    file.close()
    return smallest


if __name__ == "__main__":
    # inspireted from https://www.youtube.com/watch?v=FXQWIWHaFBE&ab_channel=JefferyFrederic
    print("Result Part 1: ", part1())
    print("Result Part 2: ", part2())
