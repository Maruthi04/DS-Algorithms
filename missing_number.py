for t in range(int(input())):
    n=int(input())
    x=(input()).split()
    for i in range(len(x)):
        x[i]=int(x[i])
    value=n*(n+1)//2
    original=sum(x)
    print(value-original)