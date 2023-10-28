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
# rozdělí inpt na jednotlivé elfy (\n\n) -> rozdělí na jednotlivé jídla -> sečte je -> vrátí do pole (celkové kalorie každého elfa) -> vrátí největší číslo v poli
print(numpy.max(list(map(lambda a: reduce(lambda c, d: c + d, list(map(lambda b: int(b), a.split("\n")))), inpt.split("\n\n")))))
