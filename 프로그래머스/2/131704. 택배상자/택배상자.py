def solution(order):
    
    stack1 = [len(order)-i for i in range(0, len(order))]
    stack2 = []
    truck = []
    
    for i in range(len(order)):
        if len(stack1) != 0 and stack1[-1] == order[i]:
            load = stack1.pop()
            truck.append(load)
            continue
        
        elif len(stack1) != 0 and stack1[-1] < order[i]:
            while stack1:
                # print(stack2)
                load = stack1.pop()
                if load == order[i]:
                    truck.append(load)
                    break
                stack2.append(load)
                
        elif len(stack2) != 0:
            load = stack2.pop()
            if load == order[i]:
                truck.append(load)
            else:
                break
        else:
            break
    answer = len(truck)
    return answer