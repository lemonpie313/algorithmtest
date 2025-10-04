def solution(new_id):
    rule = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9','0','-','_','.']
    # 1단계
    new_id = new_id.lower()
    new_id = list(new_id)
    for i in range(len(new_id)):
        #2단계
        if new_id[i] not in rule:
            new_id[i] = '='
    new_id = [i for i in new_id if i != '=']
    
    for i in range(len(new_id)):
        #3단계
        if (i>=1) and (new_id[i] == '.') and (new_id[i-1] == '.'):
            new_id[i-1]='='
    new_id = [i for i in new_id if i != '=']
    
    #4단계
    if new_id[0] == '.':
        del new_id[0]
    if (len(new_id)>1) and (new_id[-1] == '.'):
        new_id.pop()
    
    new_id = ''.join(new_id)
    
    #5단계
    if new_id == '':
        new_id = 'a'
    
    #6단계
    if len(new_id)>=16:
        new_id = new_id[0:15]
        if (len(new_id)>1) and (new_id[-1] == '.'):
            new_id = new_id[:-1]
    #7단계
    elif len(new_id)==2:
        new_id+=new_id[-1]
    elif len(new_id)==1:
        new_id = new_id + new_id[-1] + new_id[-1]

    answer = new_id
    return answer