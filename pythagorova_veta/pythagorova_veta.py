import math
def pythagorova_veta(a, b):
    return math.sqrt(a**2 + b**2)

vstup = input("Napište strany odvěsen, formát a;b: ").split(";")
print(pythagorova_veta(float(vstup[0]), float(vstup[1])))