import math
def solution(expression):
    numbers = list("0123456789")
    num = []
    mul = []
    eachnum = []
    for i in range(len(expression)):
        if expression[i] not in numbers:
            mul.append(expression[i])
            num.append(int("".join(eachnum)))
            eachnum = []
        else:
            eachnum.append(expression[i])
    num.append(int("".join(eachnum)))
    
    def plus(mul, num):
        i = 0
        while i < len(mul):
            if mul[i] == "+":
                num[i] += num[i+1]
                del num[i+1]
                del mul[i]
            else:
                i += 1
        return mul, num
    
    def minus(mul, num):
        i = 0
        while i < len(mul):
            if mul[i] == "-":
                num[i] -= num[i+1]
                del num[i+1]
                del mul[i]
            else:
                i += 1
        return mul, num
    
    def multiply(mul, num):
        i = 0
        while i < len(mul):
            if mul[i] == "*":
                num[i] *= num[i+1]
                del num[i+1]
                del mul[i]
            else:
                i += 1
        return mul, num
    
    def case1(mul, num):
        mul, num = plus(mul, num)
        mul, num = minus(mul, num)
        mul, num = multiply(mul, num)
        return num[0]
    def case2(mul, num):
        mul, num = plus(mul, num)
        mul, num = multiply(mul, num)
        mul, num = minus(mul, num)
        return num[0]
    def case3(mul, num):
        mul, num = minus(mul, num)
        mul, num = plus(mul, num)
        mul, num = multiply(mul, num)
        return num[0]
    def case4(mul, num):
        mul, num = minus(mul, num)
        mul, num = multiply(mul, num)
        mul, num = plus(mul, num)
        return num[0]
    def case5(mul, num):
        mul, num = multiply(mul, num)
        mul, num = plus(mul, num)
        mul, num = minus(mul, num)
        return num[0]
    def case6(mul, num):
        mul, num = multiply(mul, num)
        mul, num = minus(mul, num)
        mul, num = plus(mul, num)
        return num[0]
    
    # print(case1(mul[:], num[:]))
    # return case1(mul[:], num[:])
    a = abs(case1(mul[:], num[:]))
    b = abs(case2(mul[:], num[:]))
    c = abs(case3(mul[:], num[:]))
    d = abs(case4(mul[:], num[:]))
    e = abs(case5(mul[:], num[:]))
    f = abs(case6(mul[:], num[:]))
    
    return max([a,b,c,d,e,f])