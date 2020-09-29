import math
sum=0
n=10000
x = 2*math.pi /n #对应的宽
y=[]
for i in range(0,n+1):
    y.append(abs(math.sin(i*x)))
for h in y:
    s=x*h
    sum=sum+s
print(sum)