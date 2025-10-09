def solution(n, t, m, p):
    tube = []
    number = 0
    cnt = 1

    over10 = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    
    while len(tube) < t:
        changednum = []
        if number == 0:
            changednum.append(number)
        else:
            lasts = number
            while lasts >= n:
                toappend = lasts % n
                if toappend >= 10:
                    toappend = over10[toappend]           
                changednum.append(toappend)
                lasts = lasts // n
            if lasts != 0:
                if lasts >= 10:
                    changednum.append(over10[lasts])
                else:
                    changednum.append(lasts)
            
        for i in range(len(changednum)-1, -1, -1):
            if (cnt % m == p) or ((cnt%m)+m == p):
                tube.append(str(changednum[i]))
            if len(tube) == t:
                break
            cnt += 1
        number += 1
    return "".join(tube)