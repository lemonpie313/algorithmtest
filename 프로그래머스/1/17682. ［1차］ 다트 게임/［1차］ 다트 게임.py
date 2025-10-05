import re
def solution(dartresult):
    result = []
    dartresult = re.split('([^0-9])',dartresult)
    dartresult = ' '.join(dartresult).split()
    
    for i in range(len(dartresult)):
        
        if dartresult[i].isdigit():
            score = int(dartresult[i])
            
            if dartresult[i+1] == 'D':
                score = score**2
            elif dartresult[i+1] == 'T':
                score = score**3
            
            if (len(dartresult) > i+2) and (dartresult[i+2] == '*'):
                if  len(result)!=0:
                    result[-1] = result[-1]*2
                score = score * 2
            elif (len(dartresult) > i+2) and (dartresult[i+2] == '#'):
                score = score * (-1)
            result.append(score)
            
            
    return sum(result)