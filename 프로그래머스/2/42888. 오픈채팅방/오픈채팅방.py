def solution(records):
    userdict = {}
    results = []
    answer = []
    
    for record in records:
        record = record.split()
        action = record[0]
        userid = record[1]
        if action != "Leave":
            nickname = record[2]
            userdict[userid] = nickname
        if action != "Change":
            results.append([action, userid])
    

    for result in results:
        if result[0] == 'Enter':
            info = '님이 들어왔습니다.'
        elif result[0] == 'Leave':
            info = '님이 나갔습니다.'
        info = userdict[result[1]] + info
        
        answer.append(info)
    
    return answer