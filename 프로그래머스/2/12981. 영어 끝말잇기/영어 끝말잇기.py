def solution(n, words):
    a, b = 0, 0
    for i in range(len(words)):
        if i==0:
            continue
        if words[i][0] != words[i-1][-1]:
            a = i//n+1
            b = i%n+1
            break
        if words[i] in words[0:i]:
            a = i//n+1
            b = i%n+1
            break

    return [b, a]