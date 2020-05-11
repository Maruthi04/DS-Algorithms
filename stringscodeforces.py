for i in range(int(input())):
    s=input()
    if len(s)>10:
        print(s[0]+str(len(s[1:len(s)-1]))+s[len(s)-1])
    else:
        print(s)