def solution(friends, gifts):
    fnum = len(friends)
    recieved = {f: 0 for f in friends}
    sames = []
    giftnums = []
    giftslist = list([gift.split()[0], gift.split()[1]] for gift in gifts)
    for i in range(fnum):
        fromi = len([a for a in giftslist if a[0] == friends[i]])
        toi = len([a for a in giftslist if a[1] == friends[i]])
        giftnums.append(fromi - toi)

        for j in range(i+1, fnum):
            atob = giftslist.count([friends[i],friends[j]])
            btoa = giftslist.count([friends[j],friends[i]])
            if atob > btoa:
                recieved[friends[i]] += 1
            elif atob < btoa:
                recieved[friends[j]] += 1
            else:
                sames.append([i, j])

    for same in sames:
        if giftnums[same[0]]>giftnums[same[1]]:
            recieved[friends[same[0]]]+=1
        elif giftnums[same[1]]>giftnums[same[0]]:
            recieved[friends[same[1]]]+=1

    most = max(recieved.values())
    
    return most