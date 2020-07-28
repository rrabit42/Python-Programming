import random

dice = [0, 0, 0, 0, 0, 0]  # 또는 dice = [0 for i in range (6)]
for i in range (10000) :
    n = random.randint(1, 6)
    dice[n-1] += 1

print(dice)