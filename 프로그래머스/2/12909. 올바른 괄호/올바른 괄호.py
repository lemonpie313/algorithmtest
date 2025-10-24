def solution(s):
    s = list(s)
    o = []
    p = []
    if (s[0] != '(') or (s[-1] != ')'):
        return False
    for i in range(len(s)):
        if s[i] == '(':
            o.append(i)
        else:
            p.append(i)
            
    if len(o) != len(p):
        return False
    for i in range(len(o)):
        if o[i] < p[i]:
            answer = True
        else:
            return False

    return answer