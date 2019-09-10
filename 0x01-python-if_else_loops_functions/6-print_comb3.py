#!/usr/bin/python3
for i in range(0, 9 + 1):
    for j in range(i + 1, 9 + 1):
        print("{}".format(i), end="")
        if i < 8:
            print("{}".format(j), end=", ")
        else:
            print("{}".format(j))
