a = input()
channel = []
for i in range(int(a)):
    num = input()
    channel.append(num)

mtd = ''

kbs1 = 'KBS1'
kbs2 = 'KBS2'

kbs1loc = channel.index(kbs1)
kbs2loc = channel.index(kbs2)

if int(a)==2:
    mtd = "3"

elif kbs1loc < kbs2loc:
    mtd = ('1'*kbs1loc) + ('4'*kbs1loc) + ('1'*kbs2loc) + ('4'*(kbs2loc-1))
else:
    mtd = ('1'*kbs1loc) + ('4'*kbs1loc) + ('1'*(kbs2loc+1)) + ('4'*kbs2loc)
print(mtd)