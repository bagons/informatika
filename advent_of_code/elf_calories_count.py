from functools import reduce
import numpy
inpt = """1000
2000
3000

4000

5000
6000

7000
8000
9000

10000"""
print(numpy.max(list(map(lambda a: reduce(lambda c, d: c + d, list(map(lambda b: int(b), a.split("\n")))), inpt.split("\n\n")))))