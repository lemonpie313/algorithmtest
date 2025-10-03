def solution(s):
    numbers = ['zero','one','two','three','four','five','six','seven','eight','nine']
    for num in range(len(numbers)):
        s = s.replace(numbers[num], str(num))
    return int(s)