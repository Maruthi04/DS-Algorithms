#nth term= ((sqrt(5)+1)/2)^n/sqrt(5)
import math
n=int(input("enter the range"))
for i in range(0,n+1):
    x=(1+math.sqrt(5))/2
    print(int(round((x**i)/math.sqrt(5))))


