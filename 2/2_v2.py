with open('input.txt') as file:
    rounds = [line.replace(" ", "") for line in file.read().strip().split("\n")]
    outcomes = {
        "AX": 3, "AY": 4, "AZ": 8,
        "BX": 1, "BY": 5, "BZ": 9,
        "CX": 2, "CY": 6, "CZ": 7
    }
    total_score = 0
    for round in rounds:
        total_score += outcomes[round]

    print(total_score)