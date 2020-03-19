import math
a = int(input())
b = int(input()) 


answ = []


for i in range(a, b+1):
    if  i % math.sqrt(i) == 0 :
       answ.append(i)

print(' '.join(str(i) for i in answ))