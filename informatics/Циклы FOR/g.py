n = int(input())
i = 1


answ = []


for i in range(2, n+1):
    if n % i  == 0 :
       print(i) 
       break