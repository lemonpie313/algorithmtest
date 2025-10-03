def solution(today, terms, privacies):
    result = []
    
    todaylist = today.split(".")
    [todayyear, todaymonth, todaydate] = [int(todaylist[0]), int(todaylist[1]), int(todaylist[2])]
    termsdict = {i.split()[0]: int(i.split()[1]) for i in terms}
    
    for num in range(len(privacies)):
        privacydate = privacies[num].split()[0].split(".")
        privacyterm = termsdict[privacies[num].split()[1]]
        privacydate[0] = int(privacydate[0])
        privacydate[1] = int(privacydate[1])+privacyterm 
        privacydate[2] = int(privacydate[2]) - 1
        if privacydate[2] < 1:
            privacydate[1] -=1
            privacydate[2] = 28

        if privacydate[1] > 12:
            if privacydate[1]%12 == 0:
                privacydate[0] = privacydate[0] + int(privacydate[1] / 12) - 1
                privacydate[1] = 12
            else:
                privacydate[0] += int(privacydate[1] / 12)
                privacydate[1] = privacydate[1] % 12

        if (privacydate[0] < todayyear) or ((privacydate[0] == todayyear) and (privacydate[1] < todaymonth)) or ((privacydate[0] == todayyear) and (privacydate[1] == todaymonth) and (privacydate[2] < todaydate)):
            result.append(num+1)
    
    return result