import sys
input = sys.stdin.readline

M =  int(input())
cities = sorted(list(map(int, input().split())))
amounts = int(input())

sumofcity = sum(cities)

if sumofcity <= amounts:
    print(cities[-1])
else:
    for i in range(M):
        if cities[i]*(M-i) + sum(cities[0:i]) > amounts:
            higher = i
            break
    pre_sum = sum(cities[0:higher])
    print((amounts - pre_sum) // (M-higher))