import string

VALUES = list(string.ascii_letters)

# Part 1
with open("input") as file:

    rucksacks = [line for line in file.read().split("\n")]
    total_priority = 0

    for sack in rucksacks:
        half = len(sack) // 2
        left_compartment = set(sack[:half])
        right_compartment = set(sack[half:])

        for item in VALUES:
            if item in right_compartment and item in left_compartment:
                total_priority += VALUES.index(item) + 1

    print(total_priority)

# Part 2
with open("input") as file:
    rucksacks = [line for line in file.read().split("\n")]
    elves_group = []
    total_priority = 0
    for i in range(0, len(rucksacks), 3):
        print(i)
        group = [rucksacks[i], rucksacks[i + 1], rucksacks[i + 2]]
        elves_group.append(group)

    for group in elves_group:
        for item in VALUES:
            if item in group[0] and item in group[1] and item in group[2]:
                total_priority += VALUES.index(item) + 1

    print(total_priority)


