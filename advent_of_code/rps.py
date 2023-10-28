from functools import reduce
# body za kamen nužky papir
def rps(A, B):
    transf = {"A": "X", "B": "Y", "C" : "Z"}
    win_conds = {"X": "Z", "Y": "X", "Z" : "Y"}
    if transf[A] == B: return 3
    elif win_conds[transf[A]] == B: return 0
    else: return 6

# body za kamen nužky papir + body za volbu předmětu
def scor_check(op, you):
    return rps(op, you) + {"X": 1, "Y": 2, "Z": 3}[you]

inpt = """A Y
B X
C Z"""

# rozdělí vstup na řádky, najde volby předmětů -> zjistí skóre kola -> udělá součet všech skóre z ruzných kol
print(reduce(lambda b, c: b + c, list(map(lambda a: scor_check(a[0], a[2]), inpt.split("\n")))))
