def solution(numbers):
    
    result = [-1 for i in range(len(numbers))]
    
    stack = [numbers[len(numbers)-1]]
    
    for i in range(len(numbers)-2, -1, -1):
        if stack[0] > numbers[i]:
            for j in range(len(stack)-1, -1, -1):
                if stack[j] > numbers[i]:
                    result[i] = stack[j]
                    break
                else:
                    stack.pop()
            stack.append(numbers[i])
            
        else:
            result[i] = -1
            stack = [numbers[i]]
             
    answer = []
    return result