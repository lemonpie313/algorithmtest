def solution(number, k):
    
    start = 0
    for i in range(k):
        remover = 0
        for j in range(start, len(number)-1):
            if number[j]<number[j+1]:
                start = max(j-1, 0)
                remover = number[j]
                break
            if j ==len(number)-2:
                return number[i:-1]
        number = number.replace(str(remover), '', 1)
                
        
    return number