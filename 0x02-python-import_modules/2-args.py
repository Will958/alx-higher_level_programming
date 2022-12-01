#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    count = len(sys.agrv) - 1
    if count == 0:
        print("0 arguments.")
    else if count == 1:
        print("1 arguments:")
    else:
        print("{} arguments:".format(count)
              for i in range(count):
              print(f"{i + 1}: {sys.argv[i + 1]}")
