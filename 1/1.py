file = open("input.txt", "r")
elves = []
calories = 0
for line in file.readlines():
    line = line.strip()
    if line == "":
        elves.append(calories)
        calories = 0
    else:
        calories += int(line)
top_three = 0
for i in range(3):
    top_three += max(elves)
    elves.remove(max(elves))
print(top_three)
file.close()
