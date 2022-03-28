import re

"""
Reads a text file and replaces a pattern inside
option (str) : -n - suppresses the duplicate rows
command (str) : s - to replace the text in a file
replace_str (str): the string to replace
to_pattern (str): the pattern to replace to
flag (str/int): g - global or not global / p - print duplicates
source (str): the text file to read / string to read
dest (str) : the text file to write

"""
"""
no command or flag - first occurrence in a line [1] V
int  - nth occurrence [2] V
g  - all occurrences in a line  [3]   V
int and g - from nth to all in a line [4] V   
p - duplicate the replaced occurrence [5] V
-n and p - print only the replaced lines [6] V
"""


def sed(option, command, replace_str, to_pattern, flag, source, dest):
    if re.match("[a-zA-z0-9]*.txt$", source):
        if re.match("^s$", command):
            if re.match("^g$", flag) and re.match("^$", option):

                replace_all_occur_line_from_file(option, command, replace_str, to_pattern, flag, source, dest)

            elif re.match("^$", flag) and re.match("^$", option):

                replace_first_occur_line_from_file(option, command, replace_str, to_pattern, flag, source, dest)

            elif re.match("^[0-9]*$", flag) and re.match("^$", option):

                replace_nth_occur_line_from_file(option, command, replace_str, to_pattern, flag, source, dest)

            elif re.match("^[0-9g]*$", flag) and re.match("^$", option):

                replace_nth_to_all_occur_line_from_file(option, command, replace_str, to_pattern, flag, source, dest)

            elif re.match("^p$", flag):
                if re.match("^-n$", option):

                    print_only_replaced_lines_from_file(option, command, replace_str, to_pattern, flag, source, dest)
                else:
                    print_replaced_lines_twice_from_file(option, command, replace_str, to_pattern, flag, source, dest)

            else:
                return

    else:
        if re.match("^s$", command):
            if re.match("^g$", flag) and re.match("^$", option):

                replace_all_occur_line_from_string_input(option, command, replace_str, to_pattern, flag, source, dest)

            elif re.match("^$", flag) and re.match("^$", option):

                replace_first_occur_line_from_string_input(option, command, replace_str, to_pattern, flag, source, dest)

            elif re.match("^[0-9]*$", flag) and re.match("^$", option):

                replace_nth_occur_line_from_string_input(option, command, replace_str, to_pattern, flag, source, dest)

            elif re.match("^[0-9g]*$", flag) and re.match("^$", option):

                replace_nth_to_all_occur_line_from_string_input(option, command, replace_str, to_pattern, flag, source,
                                                                dest)

            elif re.match("^p$", flag):
                if re.match("^-n$", option):

                    print_only_replaced_lines_from_string_input(option, command, replace_str, to_pattern, flag, source,
                                                                dest)

                else:

                    print_replaced_lines_twice_from_string_input(option, command, replace_str, to_pattern, flag, source,
                                                                 dest)
            else:
                return


def replace_all_occur_line_from_file(option, command, replace_str, to_pattern, flag, source, dest):
    try:
        file_read = open(source, "r")
        data = file_read.read()
        if replace_str not in data:
            # raise IOError("String not found in the text")
            print(data)
            return
        else:
            data = re.sub(replace_str, to_pattern, data)
            file_read.close()

        file_write = open(dest, "w")
        file_write.write(data)
        file_write.close()
        print(data)
    except IOError:
        print("Error: File does not appear to exist.")
        return


def replace_first_occur_line_from_file(option, command, replace_str, to_pattern, flag, source, dest):
    try:
        str_result = ""
        result = []
        file_read = open(source, "r")
        data = file_read.read()
        before = data.split("\n")
        if replace_str not in data:
            # raise IOError("String not found in the text")
            print(data)
            return
        else:
            for i in before:
                result.append(re.sub(replace_str, to_pattern, i, 1))
            for x in result:
                str_result += x + "\n"
            file_read.close()

        file_write = open(dest, "w")
        file_write.write(str_result)
        file_write.close()
        print(str_result)
    except IOError:
        print("Error: File does not appear to exist.")
        return


def replace_nth_occur_line_from_file(option, command, replace_str, to_pattern, flag, source, dest):
    try:
        file_read = open(source, "r")
        data = file_read.read()
        if replace_str not in data:
            # raise IOError("String not found in the text")
            print(data)
            return
        else:
            new_string = replace_nth(data, replace_str, to_pattern, int(flag[0]), "nth")
            file_read.close()

        file_write = open(dest, "w")
        file_write.write(new_string)
        file_write.close()
        print(new_string)
    except IOError:
        print("Error: File does not appear to exist.")
        return


def replace_nth_to_all_occur_line_from_file(option, command, replace_str, to_pattern, flag, source, dest):
    try:
        file_read = open(source, "r")
        data = file_read.read()
        if replace_str not in data:
            # raise IOError("String not found in the text")
            print(data)
            return
        else:
            new_string = replace_nth(data, replace_str, to_pattern, int(flag[0]), "nth_right")
            file_read.close()
        file_write = open(dest, "w")
        file_write.write(new_string)
        file_write.close()
        print(new_string)
    except IOError:
        print("Error: File does not appear to exist.")
        return


def print_only_replaced_lines_from_file(option, command, replace_str, to_pattern, flag, source, dest):
    try:
        str_result = ""
        result = []
        file_read = open(source, "r")
        data = file_read.read()
        if replace_str not in data:
            # raise IOError("String not found in the text")
            print(data)
            return
        else:
            before = data.split("\n")
            data = re.sub(replace_str, to_pattern, data)
            after = data.split("\n")

            for i, j in zip(after, before):
                if i != j:
                    result.append(i)
            for x in result:
                str_result += x + "\n"
            file_read.close()

        file_write = open(dest, "w")
        file_write.write(str_result)
        file_write.close()
        print(str_result)
    except IOError:
        print("Error: File does not appear to exist.")
        return


def print_replaced_lines_twice_from_file(option, command, replace_str, to_pattern, flag, source, dest):
    try:
        str_result = ""
        result = []
        file_read = open(source, "r")
        data = file_read.read()
        if replace_str not in data:
            # raise IOError("String not found in the text")
            print(data)
            return
        else:
            before = data.split("\n")
            data = re.sub(replace_str, to_pattern, data)
            after = data.split("\n")

            for i, j in zip(after, before):
                if i != j:
                    for k in range(2):
                        result.append(i)
                else:
                    result.append(j)
            for x in result:
                str_result += x + "\n"
            file_read.close()

        file_write = open(dest, "w")
        file_write.write(str_result)
        file_write.close()
        print(str_result)
    except IOError:
        print("Error: File does not appear to exist.")
        return


def replace_all_occur_line_from_string_input(option, command, replace_str, to_pattern, flag, source, dest):
    try:
        to_replace = input("Write the string to change: ")
        if replace_str not in to_replace:
            # raise IOError("String not found in the text")
            print(to_replace)
            return
        else:
            new_string = re.sub(replace_str, to_pattern, to_replace)

            file_write = open(dest, "w")
            file_write.write(new_string)
            file_write.close()
            print(new_string)
    except IOError:
        print("Error: File does not appear to exist.")
        return


def replace_first_occur_line_from_string_input(option, command, replace_str, to_pattern, flag, source, dest):
    try:
        str_result = ""
        result = []
        to_replace = input("Write the string to change: ")
        before = to_replace
        if replace_str not in before:
            # raise IOError("String not found in the text")
            print(before)
            return
        else:
            result.append(re.sub(replace_str, to_pattern, to_replace, 1))
            for x in result:
                str_result += x

        file_write = open(dest, "w")
        file_write.write(str_result)
        file_write.close()
        print(str_result)
    except IOError:
        print("Error: File does not appear to exist.")
        return


def replace_nth_occur_line_from_string_input(option, command, replace_str, to_pattern, flag, source, dest):
    try:
        to_replace = input("Write the string to change: ")
        if replace_str not in to_replace:
            # raise IOError("String not found in the text")
            print(to_replace)
            return
        else:
            new_string = replace_nth(to_replace, replace_str, to_pattern, int(flag[0]), "nth")
            file_write = open(dest, "w")
            file_write.write(new_string)
            file_write.close()
            print(new_string)
    except IOError:
        print("Error: File does not appear to exist.")
        return


def replace_nth_to_all_occur_line_from_string_input(option, command, replace_str, to_pattern, flag, source, dest):
    try:
        to_replace = input("Write the string to change: ")
        if replace_str not in to_replace:
            # raise IOError("String not found in the text")
            print(to_replace)
            return
        else:
            new_string = replace_nth(to_replace, replace_str, to_pattern, int(flag[0]), "nth_right")
            file_write = open(dest, "w")
            file_write.write(new_string)
            file_write.close()
            print(new_string)
    except IOError:
        print("Error: File does not appear to exist.")
        return


def print_only_replaced_lines_from_string_input(option, command, replace_str, to_pattern, flag, source, dest):
    try:
        str_result = ""
        result = []
        to_replace = input("Write the string to change: ")
        if replace_str not in to_replace:
            # raise IOError("String not found in the text")
            print(to_replace)
            return
        else:
            before = to_replace
            new_string = re.sub(replace_str, to_pattern, to_replace)
            after = new_string
            if before != after:
                result.append(after)
            else:
                result.append(before)
            for x in result:
                str_result += x + "\n"

        file_write = open(dest, "w")
        file_write.write(str_result)
        file_write.close()
        print(str_result)
    except IOError:
        print("Error: File does not appear to exist.")
        return


def print_replaced_lines_twice_from_string_input(option, command, replace_str, to_pattern, flag, source, dest):
    try:
        str_result = ""
        result = []
        to_replace = input("Write the string to change: ")
        if replace_str not in to_replace:
            # raise IOError("String not found in the text")
            print(to_replace)
            return
        else:
            before = to_replace
            new_string = re.sub(replace_str, to_pattern, to_replace)
            after = new_string
            if before != after:
                result.append(after)
                result.append(after)
            else:
                result.append(before)
            for x in result:
                str_result += x + "\n"

        file_write = open(dest, "w")
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
sed("", "s", "cat", "zebra", "", "input.txt", "output.txt")
sed("", "s", "cat", "zebra", "g", "input.txt", "output.txt")
sed("", "s", "cat", "zebra", "2", "input.txt", "output.txt")
sed("", "s", "cat", "zebra", "3g", "input.txt", "output.txt")
sed("", "s", "cat", "zebra", "p", "input.txt", "output.txt")
sed("-n", "s", "cat", "zebra", "p", "input.txt", "output.txt")

with string:
sed("", "s", "cat", "zebra", "", "", "output.txt")
sed("", "s", "cat", "zebra", "g", "", "output.txt")
sed("", "s", "cat", "zebra", "1", "", "output.txt")
sed("", "s", "cat", "zebra", "4g", "", "output.txt")
sed("", "s", "cat", "zebra", "p", "", "output.txt")
sed("-n", "s", "cat", "zebra", "p", "", "output.txt")
"""
sed("", "s", "cat", "ZEBRA", "2", "input.txt", "output.txt")
