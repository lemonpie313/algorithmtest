def solution(number, k):
    array = [number[0]]

    for i in number[1:]:
        while (len(array) != 0) and (array[-1] < i) and (k != 0):
            k -= 1
            array.pop()
        array.append(i)
    if k != 0:
        array = array[:-k]
    return "".join(array)