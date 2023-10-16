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
    for rucksack in inpt.split("\n"):
        compartment_2 = rucksack[int(len(rucksack) / 2):]
        for char in rucksack[0: int(len(rucksack) / 2)]:
            if char in compartment_2:
                print(char)
                score += char_to_score(char)
                break
    return score


print(solve())