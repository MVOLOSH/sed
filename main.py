import re

"""
Basic SED Command implementation
"""
"""
Reads a text file and replaces a pattern inside
option (str) : -n - suppresses the duplicate rows
command (str) : s - to replace the text in a file
replace_str (str): the string to replace
to_pattern (str): the pattern to replace to
flag (str/int): g - global or not global / p - print duplicates
source (str): the text file to read / string to read
destination (str) : the text file to write

"""
"""
[1]: no command or flag - first occurrence in a line
[2]: int  - nth occurrence in a line
[3]: g  - all occurrences in a line
[4]: int and g - from nth to all in a line
[5]: p - duplicate the replaced occurrence
[6]: -n and p - print only the replaced lines
"""


def sed(option, command, replace_str, to_pattern, flag, source, destination):
    if re.match("[a-zA-z0-9]*.txt$", source):  # get input txt file
        if re.match("^s$", command):
            if re.match("^g$", flag) and re.match("^$", option):
                # replace all occurrences of a string
                replace_all_occur_line_from_file(replace_str, to_pattern, source, destination)

            elif re.match("^$", flag) and re.match("^$", option):
                # replace first occurence of a string on each line
                replace_first_occur_line_from_file(replace_str, to_pattern, source, destination)

            elif re.match("^[0-9]*$", flag) and re.match("^$", option):
                # replace the nth string occurrence on each line
                replace_nth_occur_line_from_file(replace_str, to_pattern, flag, source, destination)

            elif re.match("^[0-9g]*$", flag) and re.match("^$", option):
                # replace from the nth to the last occurrence on each line
                replace_nth_to_all_occur_line_from_file(replace_str, to_pattern, flag, source, destination)

            elif re.match("^p$", flag):
                if re.match("^-n$", option):
                    # print only the lines that had a string replaced
                    print_only_replaced_lines_from_file(replace_str, to_pattern, source, destination)
                else:
                    # print the lines that had a string replaced twice and other lines ones
                    print_replaced_lines_twice_from_file(replace_str, to_pattern, source, destination)

            else:
                return

    else:  # get an input string
        if re.match("^s$", command):
            if re.match("^g$", flag) and re.match("^$", option):
                # replace all occurrences of a string
                replace_all_occur_line_from_string_input(replace_str, to_pattern, destination)

            elif re.match("^$", flag) and re.match("^$", option):
                # replace first occurence of a string on each line
                replace_first_occur_line_from_string_input(replace_str, to_pattern, destination)

            elif re.match("^[0-9]*$", flag) and re.match("^$", option):
                # replace the nth string occurrence on each line
                replace_nth_occur_line_from_string_input(replace_str, to_pattern, flag, destination)

            elif re.match("^[0-9g]*$", flag) and re.match("^$", option):
                # replace from the nth to the last occurrence on each line
                replace_nth_to_all_occur_line_from_string_input(replace_str, to_pattern, flag, destination)

            elif re.match("^p$", flag):
                if re.match("^-n$", option):
                    # print only the lines that had a string replaced
                    print_only_replaced_lines_from_string_input(replace_str, to_pattern, destination)

                else:
                    # print the lines that had a string replaced twice and other lines ones
                    print_replaced_lines_twice_from_string_input(replace_str, to_pattern, destination)
            else:
                return


def replace_all_occur_line_from_file(replace_str, to_pattern, source, destination):
    try:
        file_read = open(source, "r")
        data = file_read.read()
        if replace_str not in data:
            print(data)
            return
        else:
            data = re.sub(replace_str, to_pattern, data)
            file_read.close()

        file_write = open(destination, "w")
        file_write.write(data)
        file_write.close()
        print(data)
    except IOError:
        print("Error: File does not appear to exist.")
        return


def replace_first_occur_line_from_file(replace_str, to_pattern, source, destination):
    try:
        str_result = ""
        result = []
        file_read = open(source, "r")
        data = file_read.read()
        before = data.split("\n")
        if replace_str not in data:
            print(data)
            return
        else:
            for i in before:
                result.append(re.sub(replace_str, to_pattern, i, 1))
            for x in result:
                str_result += x + "\n"
            file_read.close()

        file_write = open(destination, "w")
        file_write.write(str_result)
        file_write.close()
        print(str_result)
    except IOError:
        print("Error: File does not appear to exist.")
        return


def replace_nth_occur_line_from_file(replace_str, to_pattern, flag, source, destination):
    try:
        result = []
        str_result = ""
        file_read = open(source, "r")
        data = file_read.read()
        before = data.split("\n")
        if replace_str not in data:
            print(data)
            return
        else:
            for i in before:
                if len(re.findall(replace_str, i)) >= int(flag[0]):
                    new_string = replace_nth(i, replace_str, to_pattern, int(flag[0]), "nth")
                    result.append(new_string)
                else:
                    print(data)
                    return
            for x in result:
                str_result += x + "\n"
            file_read.close()

        file_write = open(destination, "w")
        file_write.write(str_result)
        file_write.close()
        print(str_result)
    except IOError:
        print("Error: File does not appear to exist.")
        return


def replace_nth_to_all_occur_line_from_file(replace_str, to_pattern, flag, source, destination):
    try:
        result = []
        str_result = ""
        file_read = open(source, "r")
        data = file_read.read()
        before = data.split("\n")
        if replace_str not in data:
            print(data)
            return
        else:
            for i in before:
                if len(re.findall(replace_str, i)) >= int(flag[0]):
                    new_string = replace_nth(i, replace_str, to_pattern, int(flag[0]), "nth_right")
                    result.append(new_string)
                else:
                    print(data)
                    return
            for x in result:
                str_result += x + "\n"
            file_read.close()

        file_write = open(destination, "w")
        file_write.write(str_result)
        file_write.close()
        print(str_result)
    except IOError:
        print("Error: File does not appear to exist.")
        return


def print_only_replaced_lines_from_file(replace_str, to_pattern, source, destination):
    try:
        str_result = ""
        result = []
        temp = []
        file_read = open(source, "r")
        data = file_read.read()
        if replace_str not in data:
            print(data)
            return
        else:
            before = data.split("\n")
            for k in before:
                temp.append(re.sub(replace_str, to_pattern, k, 1))
            for i, j in zip(temp, before):
                if i != j:
                    result.append(i)
            for x in result:
                str_result += x + "\n"
            file_read.close()

        file_write = open(destination, "w")
        file_write.write(str_result)
        file_write.close()
        print(str_result)
    except IOError:
        print("Error: File does not appear to exist.")
        return


def print_replaced_lines_twice_from_file(replace_str, to_pattern, source, destination):
    try:
        str_result = ""
        result = []
        temp = []
        file_read = open(source, "r")
        data = file_read.read()
        if replace_str not in data:
            print(data)
            return
        else:
            before = data.split("\n")
            for k in before:
                temp.append(re.sub(replace_str, to_pattern, k, 1))

            for i, j in zip(temp, before):
                if i != j:
                    for k in range(2):
                        result.append(i)
                else:
                    result.append(j)
            for x in result:
                str_result += x + "\n"
            file_read.close()

        file_write = open(destination, "w")
        file_write.write(str_result)
        file_write.close()
        print(str_result)
    except IOError:
        print("Error: File does not appear to exist.")
        return


def replace_all_occur_line_from_string_input(replace_str, to_pattern, destination):
    try:
        to_replace = input("Write the string to change: ")
        if replace_str not in to_replace:
            print(to_replace)
            return
        else:
            new_string = re.sub(replace_str, to_pattern, to_replace)

            file_write = open(destination, "w")
            file_write.write(new_string)
            file_write.close()
            print(new_string)
    except IOError:
        print("Error: File does not appear to exist.")
        return


def replace_first_occur_line_from_string_input(replace_str, to_pattern, destination):
    try:
        str_result = ""
        result = []
        to_replace = input("Write the string to change: ")
        before = to_replace
        if replace_str not in before:
            print(before)
            return
        else:
            result.append(re.sub(replace_str, to_pattern, to_replace, 1))
            for x in result:
                str_result += x

        file_write = open(destination, "w")
        file_write.write(str_result)
        file_write.close()
        print(str_result)
    except IOError:
        print("Error: File does not appear to exist.")
        return


def replace_nth_occur_line_from_string_input(replace_str, to_pattern, flag, destination):
    try:
        to_replace = input("Write the string to change: ")
        if replace_str not in to_replace:
            print(to_replace)
            return
        else:
            new_string = replace_nth(to_replace, replace_str, to_pattern, int(flag[0]), "nth")
            file_write = open(destination, "w")
            file_write.write(new_string)
            file_write.close()
            print(new_string)
    except IOError:
        print("Error: File does not appear to exist.")
        return


def replace_nth_to_all_occur_line_from_string_input(replace_str, to_pattern, flag, destination):
    try:
        to_replace = input("Write the string to change: ")
        if replace_str not in to_replace:
            print(to_replace)
            return
        else:
            new_string = replace_nth(to_replace, replace_str, to_pattern, int(flag[0]), "nth_right")
            file_write = open(destination, "w")
            file_write.write(new_string)
            file_write.close()
            print(new_string)
    except IOError:
        print("Error: File does not appear to exist.")
        return


def print_only_replaced_lines_from_string_input(replace_str, to_pattern, destination):
    try:
        str_result = ""
        result = []
        to_replace = input("Write the string to change: ")
        if replace_str not in to_replace:
            print(to_replace)
            return
        else:
            before = to_replace
            new_string = re.sub(replace_str, to_pattern, to_replace, 1)
            after = new_string
            if before != after:
                result.append(after)
            else:
                result.append(before)
            for x in result:
                str_result += x + "\n"

        file_write = open(destination, "w")
        file_write.write(str_result)
        file_write.close()
        print(str_result)
    except IOError:
        print("Error: File does not appear to exist.")
        return


def print_replaced_lines_twice_from_string_input(replace_str, to_pattern, destination):
    try:
        str_result = ""
        result = []
        to_replace = input("Write the string to change: ")
        if replace_str not in to_replace:
            print(to_replace)
            return
        else:
            before = to_replace
            new_string = re.sub(replace_str, to_pattern, to_replace, 1)
            after = new_string
            if before != after:
                result.append(after)
                result.append(after)
            else:
                result.append(before)
            for x in result:
                str_result += x + "\n"

        file_write = open(destination, "w")
        file_write.write(str_result)
        file_write.close()
        print(str_result)
    except IOError:
        print("Error: File does not appear to exist.")
        return


def replace_nth(string, old_str, new_str, n=1, option="nth"):
    if option == 'nth':
        left_join = old_str
        right_join = old_str
    elif option == 'nth_right':
        left_join = old_str
        right_join = new_str
    else:
        return
    groups = string.split(old_str)
    nth_split = [left_join.join(groups[:n]), right_join.join(groups[n:])]
    return new_str.join(nth_split)


# sample inputs
"""
with text file:
sed("", "s", "cat", "ZEBRA", "", "input.txt", "output.txt")
sed("", "s", "cat", "ZEBRA", "g", "input.txt", "output.txt")
sed("", "s", "cat", "ZEBRA", "2", "input.txt", "output.txt")
sed("", "s", "cat", "ZEBRA", "2g", "input.txt", "output.txt")
sed("", "s", "cat", "ZEBRA", "p", "input.txt", "output.txt")
sed("-n", "s", "cat", "ZEBRA", "p", "input.txt", "output.txt")

with string:
sed("", "s", "cat", "ZEBRA", "", "", "output.txt")
sed("", "s", "cat", "ZEBRA", "g", "", "output.txt")
sed("", "s", "cat", "ZEBRA", "1", "", "output.txt")
sed("", "s", "cat", "ZEBRA", "1g", "", "output.txt")
sed("", "s", "cat", "ZEBRA", "p", "", "output.txt")
sed("-n", "s", "cat", "ZEBRA", "p", "", "output.txt")
"""
