import string

with open("input") as file:
    data = [i for i in file.read().strip().split("\n")]
    # ==== PART 1 ====

    # # Iterate through out dataset
    totalSum = 0
    for entry in data:
        # Get the half way mark
        half = len(entry) // 2

        # Split up the string
        leftSide = set(entry[:half])
        rightSide = set(entry[half:])

        # print(leftSide, rightSide)
        for value, character in enumerate(string.ascii_letters):
            print(value)
            print(character)
            if character in leftSide and character in rightSide:
                totalSum += value + 1

    print("Answer to part 1: ", totalSum)