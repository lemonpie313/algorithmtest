import sys
input = sys.stdin.readline

def dev2(targetlist):
    if len(targetlist) == 1:
        return targetlist[0]
    elif len(targetlist)%2==0:
        return dev2([value for index, value in enumerate(targetlist) if index%2==1])
    else:
        return dev2([targetlist[-1]] + [value for index,value in enumerate(targetlist) if index%2==1])    

M = int(input())
targetlist = list(range(1, M+1))

print(dev2(targetlist))