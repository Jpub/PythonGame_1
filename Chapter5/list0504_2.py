import random
ALP = ["A", "B", "C", "D", "E", "F", "G"]
r = random.choice(ALP)
alp = ""
for i in ALP:
    if i != r:
        alp = alp + i
print(alp)
