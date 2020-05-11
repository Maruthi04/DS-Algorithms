dic=dict()
for i in range((int(input()))):
    x=input()
    if x in dic:
        dic[x]+=1
        print(x+str(dic[x]))
    else:
        dic[x]=0
        print("OK")