def solution(s):
    s = list(s)
    o = []
    if (s[0] != '(') or (s[-1] != ')'):
        return False
    for i in range(len(s)):
        if s[i] == '(':
            o.append(i)
        else:
            if len(o) == 0:
                return False
            o.pop()
    
    if len(o) == 0:
        return True
    return False