def solution(storey):
    result = 0
    i=1
    
    while i < len(str(storey))+1:
        num = storey % (10**i) // (10**(i-1))
        # print("num: " + str(num))
        if num == 0:
            i+=1
            continue
        elif num > 5:
            result += (10 - num)
            storey += (10 - num) * (10**(i-1))
            # print("result: " + str(result))
            # print("storey: " + str(storey))
        elif num == 5:
            if i < len(str(storey)) and storey % (10**(i+1)) // (10**(i)) >= 5:
                result += (10 - num)
                storey += (10 - num) * (10**(i-1))
            else:
                result += num
                storey -= num * (10**(i-1))
                
        else:
            result += num
            storey -= num * (10**(i-1))
            # print("result: " + str(result))
            # print("storey: " + str(storey))
        i += 1

    return result