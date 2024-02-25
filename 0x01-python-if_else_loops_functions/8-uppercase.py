#!/usr/bin/python3
def uppercase(s):
    for char in s:
        upper_char = chr(ord(char) - 32) if 'a' <= char <= 'z' else char
        print("{}".format(upper_char), end="")
    print()  # Print a newline at the end

# Test cases
if __name__ == "__main__":
    uppercase("best")
    uppercase("Best School 98 Battery street")
