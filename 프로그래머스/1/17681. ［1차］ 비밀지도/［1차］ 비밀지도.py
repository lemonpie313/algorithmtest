def solution(n, arr1, arr2):
    map = []
    for i in range(n):
        a = list(str(bin(arr1[i]))[2:])
        b = list(str(bin(arr2[i]))[2:])

        if len(a)<n:
            a = ['0' for i in range(n-len(a))] + a
        if len(b)<n:
            b = ['0' for i in range(n-len(b))] + b
        
        maplist = ''

        for j in range(n):
            if a[j]==b[j]=='0':
                maplist += ' '
            else:
                maplist += '#'
        map.append(maplist)
    return map