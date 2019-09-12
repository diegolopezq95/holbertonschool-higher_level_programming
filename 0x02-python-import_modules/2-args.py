#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    if len(argv) == 1:
        str = "arguments."
    elif len(argv) == 2:
        str = "argument:"
    else:
        str = "arguments:"
    print("{} {}".format(len(argv) - 1, str))
    cont = 1
    for arg in argv[1:]:
        print("{}: {}".format(cont, arg))
        cont = cont + 1
