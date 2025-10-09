import re
def solution(str1, str2):
    list1 = []
    list2 = []
    for i in range(len(str1)-1):
        if re.match(r'^[A-Za-z]+$', str1[i]+str1[i+1]):
            list1.append(str1[i].upper()+str1[i+1].upper())
        
    for i in range(len(str2)-1):
        if re.match(r'^[A-Za-z]+$', str2[i]+str2[i+1]):
            list2.append(str2[i].upper()+str2[i+1].upper())

    
    alllist = 0
    onlylist = 0

    length = len(list1)
    
    for i in range(length-1, -1, -1):
        if list1[i] in list2:
            onlylist += 1
            list2.remove(list1[i])
            list1.pop()
            

    alllist = onlylist + len(list1) + len(list2)

    if alllist == 0:
        return 65536
    return int((onlylist/alllist)*65536)