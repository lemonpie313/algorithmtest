import sys
input = sys.stdin.readline

def changeSwitch(switch):
    if switch == 1:
        return 0
    else:
        return 1

N = int(input())
switches = list(map(int, input().split()))
students = int(input())
for i in range(students):
    student = list(map(int, input().split()))
    gender = student[0]
    number = student[1]

    # 남자
    if gender == 1:
        for j in range(N):
            if (j+1)%number == 0:
                switches[j] = changeSwitch(switches[j])

    # 여자
    else:
        switches[number-1] = changeSwitch(switches[number-1])
        if N-number > number-1:
            rangeNumber = number-1
        else:
            rangeNumber = N-number

        for k in range(1, rangeNumber+1):
            if (number+k > N) or (number-k < 0):
                break
            if switches[number+k-1] == switches[number-k-1]:
                switches[number+k-1] = changeSwitch(switches[number+k-1])
                switches[number-k-1] = changeSwitch(switches[number-k-1])
            else:
                break
i = 0
while i < N:
    print(" ".join(str(a) for a in switches[i: i+20]))
    i+=20