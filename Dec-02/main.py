# Opponent
# A - rock
# B - paper
# C - scissors

# You
# X - should lose
# Y - should draw
# Z - should win

# Results
# loss -> 0
# draw -> 3
# win -> 6
with open('input') as f:
    lines = f.readlines()

losingCounterpart = {
    "A": "C",
    "B": "A",
    "C": "B"
}

winningCounterPart = {
    "A": "B",
    "B": "C",
    "C": "A"
}

scoreboard = {
    "A": 1,
    "B": 2,
    "C": 3
}

score = 0
for line in lines:
    if line[2] == "X":
        play = losingCounterpart[line[0]]
    elif line[2] == "Y":
        play = line[0]
        score += 3
    else:
        play = winningCounterPart[line[0]]
        score += 6
    score += scoreboard[play]

print(score)
