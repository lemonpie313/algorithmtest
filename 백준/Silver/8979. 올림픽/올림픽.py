import sys
input = sys.stdin.readline

M = input().split(" ")
numofnation = int(M[0])
ranknation = int(M[1])
nations = []
for n in range(numofnation):
    inputs = input().split(" ")
    if int(inputs[0]) == ranknation:
        gold = int(inputs[1])
        sil = int(inputs[2])
        bro = int(inputs[3])
    nations.append([inputs[0], int(inputs[1]), int(inputs[2]), int(inputs[3])])

rank = len([i[0] for i in nations if (i[1]>gold) or ((i[1]==gold) and (i[2]>sil)) or ((i[1]==gold) and (i[2]==sil) and (i[3]>bro))])+1
print(rank)