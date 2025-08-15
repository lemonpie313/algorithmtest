from collections import Counter
a = input().upper()
a = list(a)
counter = Counter(a)
tmp = [k for k,v in counter.items() if max(counter.values()) == v]
if len(tmp) >= 2:
    print("?")
else:
    print(tmp[0])