inpt = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw"""

def char_to_score(char):
    return ord(char) - [96, 38][char.isupper()]

def solve():
    score = 0
    # projde každý rucksack
    for rucksack in inpt.split("\n"):
        # 2. kapsa rucksacku
        compartment_2 = rucksack[int(len(rucksack) / 2):]
        # hledá jestli je v 1. kapse stejný item jako v 2.
        for char in rucksack[0: int(len(rucksack) / 2)]:
            if char in compartment_2:
                print(char)
                score += char_to_score(char)
                break
    return score


print(solve())
