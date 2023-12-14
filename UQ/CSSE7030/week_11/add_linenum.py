import sys
import itertools

in_file = sys.argv[1]

f = open(in_file, 'rU')

for line in map("{0:4d}: {1}".format, itertools.count(1), f):
    print(line, end="")

f.close()

