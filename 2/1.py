task = "2"

score_dict = {
    "A": {
        "Y": 8,
        "X": 4,
        "Z": 3
    },
    "B": {
        "Y": 5,
        "X": 1,
        "Z": 9
    },
    "C": {
        "Y": 2,
        "X": 7,
        "Z": 6
    },
}

score = 0

with open(f"{task}/{task}.in", "r") as f:
    for line in f:
        enemy = line[0]
        me = line[2]
        score += score_dict[enemy][me]


# 9177
print(score)
