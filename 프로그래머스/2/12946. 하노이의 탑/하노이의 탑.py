def solution(n):
    
    def moveforward(i):
        return i%3+1

    def movebackward(i):
        if i==1:
            return 3
        else:
            return i-1
    
    main = 1
    result = []
    plate = []
    location = {}
    
    for number in range(1, n+1):

        plate.append(number)

        if (n-number)%2 != 0:
            result.append([1, moveforward(1)])
            location[number] = moveforward(1)
        else:
            result.append([1, movebackward(1)])
            location[number] = movebackward(1)

        new_result = []
        new_plate = []
        
        if len(result) != 0:
            for i in range(len(result)-1):
                location_plate = location[plate[i]]
                if (n-plate[i]) %2 != 0:
                    new_result.append([location_plate, moveforward(location_plate)])
                    new_plate.append(plate[i])
                    location[plate[i]] = moveforward(location_plate)
                else:
                    new_result.append([location_plate, movebackward(location_plate)])
                    new_plate.append(plate[i])
                    location[plate[i]] = movebackward(location_plate)
            result = result + new_result
            plate = plate + new_plate
            
    return result