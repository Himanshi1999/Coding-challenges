import sys
import os

args = sys.argv[1:]
file_name = None
option = "-clw"

if args:
    if args[0].startswith("-"):
        option = args[0]
        if len(args) > 1:
            file_name = args[1]
    else:
        file_name = args[0]

if file_name:
    with open(file_name, 'r', encoding='utf-8') as fp:
        data = fp.read()
else:
    if not sys.stdin.isatty():
        data = sys.stdin.read()
    else:
        print("Usage: ccwc [-clwm] [filename] or input via pipe")
        sys.exit(1)

lines = data.count('\n')
word_count = len(data.split())
char_count = len(data)
file_size = len(data.encode('utf-8'))

match option:
    case "-c":
        print(f"{file_size} {file_name if file_name else ''}")
    case "-l":
        print(f"{lines} {file_name if file_name else ''}")
    case "-w":
        print(f"{word_count} {file_name if file_name else ''}")
    case "-m":
        print(f"{char_count} {file_name if file_name else ''}")
    case _:
        print(f"{lines} {word_count} {file_size} {file_name if file_name else ''}")
