import sys
input = sys.stdin.readline

M = int(input())
cal = []
s = []

for ai in range(M):
    i = input()
    i = i.strip()
    if (i == 'all') or (i == 'empty'):
        if i == "all":
            s = list(range(1, 21))
        elif i == "empty":
            s = []
        continue
        
    t = i.split()[0]
    n = int(i.split()[1])
    if n in s:
        if (t == "remove") or (t == "toggle"):
            s.remove(n)
        elif t == "check":
            print("1")
    else:
        if (t == "add") or (t == "toggle"):
            s.append(n) 
        elif t == "check":
            print("0")