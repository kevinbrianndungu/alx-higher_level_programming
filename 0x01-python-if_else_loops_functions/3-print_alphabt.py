#!/usr/bin/python3
for char in range(ord('a'), ord('z') + 1):
    if char not in [ord('e'), ord('q')]:
        print("{}".format(chr(char)), end="")
print()  # Print a newline at the end
