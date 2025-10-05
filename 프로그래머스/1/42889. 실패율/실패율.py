def solution(N, stages):
    failureresult = {}
    for i in range(1, N+1):
        still = stages.count(i)
        now = [n for n in stages if n>=i]
        if len(now)==0:
            failure = 0
        else:
            failure = still/len(now)
        failureresult[i] = failure
    
    failures = sorted(failureresult, key=lambda x: failureresult[x], reverse = True)
    return failures