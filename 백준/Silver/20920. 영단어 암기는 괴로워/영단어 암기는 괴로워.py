import sys
input = sys.stdin.readline

[M, N] = list(map(int, input().split()))
wordlist = {}

for i in range(M):
    word = input().strip()
    if len(word) >= N:
        if word in wordlist:
            wordlist[word] += 1
        else:
            wordlist[word] = 1
            
sortedword=dict(sorted(wordlist.items(), key=lambda x: (-x[1],-len(x[0]),x[0])))
for i in sortedword:
    print(i)