inputs = input()
inputs = inputs.split(" ")
a = int(inputs[0])
b = int(inputs[1])
dis_a = int(inputs[2])
dis_b = int(inputs[3])

print(int((a+dis_a)/(dis_a+1)) * int((b+dis_b)/(dis_b+1)))