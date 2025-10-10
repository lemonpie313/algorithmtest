def solution(files):
    newfiles = []
    for i in range(len(files)):
        newfiles.append([])
        head = ""
        number = ""
        tail = ""
        hasnumber = False
        for j in range(len(files[i])):
            if files[i][j] in ['0','1','2','3','4','5','6','7','8','9']:
                number += files[i][j]
                hasnumber = True
            elif hasnumber == True:
                tail += files[i][j:]
                break
            else:
                head += files[i][j]
        newfiles[i] = [head, number, tail]
    
    answer =  sorted(newfiles, key = lambda x: (x[0].upper(), int(x[1])))
    
    for i in range(len(answer)):
        answer[i] = "".join(answer[i])
            
    return answer