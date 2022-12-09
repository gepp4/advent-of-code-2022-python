with open("input.txt") as file:
    pairs = [pair for pair in file.read().split("\n")]
    total_fully_contained = 0

    for pair in pairs:
        first, second = pair.split(",")
        first = [int(shift) for shift in first.split("-")]
        second = [int(shift) for shift in second.split("-")]
        if first[0] >= second[0] and first[1] <= second[1]:
            total_fully_contained += 1
        elif second[0] >= first[0] and second[1] <= first[1]:
            total_fully_contained += 1

    print(total_fully_contained)


