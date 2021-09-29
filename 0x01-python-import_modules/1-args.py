#!/usr/bin/python3
if __name__ == "__main__":

    import sys

numargs = len(sys.argv) - 1

if numargs == 0:
    print("{:d} arguments.".format(0, sys.argv[numargs]))

elif numargs == 1:
    print("{:d} arguments:".format(1))

else:
    print("{:d} arguments:".format(numargs))

for i in range(1, numargs + 1):
    print("{:d}: {}".format(i, sys.argv[i]))
