task = "2"

action_to_figure = {
    "A": {
        "Y": "A",
        "X": "C",
        "Z": "B"
    },
    "B": {
        "Y": "B",
        "X": "A",
        "Z": "C"
    },
    "C": {
        "Y": "C",
        "X": "B",
        "Z": "A"
    },
}


score_dict = {
    "A": {
        "B": 8,
        "A": 4,
        "C": 3
    },
    "B": {
        "B": 5,
        "A": 1,
        "C": 9
    },
    "C": {
        "B": 2,
        "A": 7,
        "C": 6
    },
}

score = 0

with open(f"{task}/{task}.in", "r") as f:
    for line in f:
        enemy = line[0]
        me = line[2]
        score += score_dict[enemy][action_to_figure[enemy][me]]


# 9177
print(score)
