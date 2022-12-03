file = open("input.txt","r")
total_score = 0
score = 0
for line in file.readlines():
    if line[0] == "A":
        if line[2] == "X":
            score += 1 + 3
        elif line [2] == "Y":
            score += 2 + 6
        else:
            score += 3
    if line[0] == "B":
        if line[2] == "X":
            score += 1
        elif line[2] == "Y":
            score += 2 + 3
        else:
            score += 3 + 6
    if line[0] == "C":
        if line[2] == "X":
            score += 1 + 6
        elif line[2] == "Y":
            score += 2
        else:
            score += 3 + 3

    total_score += score
    score = 0

print(total_score)
