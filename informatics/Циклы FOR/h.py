n = int(input())

answ = []


for i in range(1, n+1):
    if n % i  == 0 :
       answ.append(i)

print(' '.join(str(i) for i in answ))