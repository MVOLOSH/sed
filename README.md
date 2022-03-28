# sed
## basic sed command implementation

Reads a text file or a string input and replaces a pattern inside:
- option (str) : -n - suppresses the duplicate rows
- command (str) : s - to replace the text in a file
- replace_str (str): the string to replace
- to_pattern (str): the pattern to replace to
- flag (str/int): g - global or not global / p - print duplicates
- source (str): the text file to read / string to read
- destination (str) : the text file to write

Different flags/commands/options:
- no command or flag - first occurrence in a line
- int  - nth occurrence in a line
- g  - all occurrences in a line
- int and g - from nth to all in a line
- p - duplicate the replaced occurrence
- -n and p - print only the replaced lines

python version 3.7.7
