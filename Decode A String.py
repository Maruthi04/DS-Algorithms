class Solution:
    def decodeString(self, s: str) -> str:
        temp=0
        for i in range(len(s)):
            if s[i]==']':
                temp=i
        origs=s
        
        visited=[0]*(len(s))
        s=list(s)
        num=""
        while((s.count('[')!=0 and s.count(']')!=0)):
            num=""
            for i in range(len(s)):
                if(s[i].isnumeric() and visited[i]!=1):
                    #num=num+s[i]
                    k=i
            for i in range(k,-1,-1):
                if(s[i].isnumeric()):
                    num=num+s[i]
                    s[i]=""
                else:
                    break
            num=num[::-1]
            print("number is ",num)
            visited[k]=1
            x=0
            y=0
            print("k=",k)
            for j in range(k,len(s)):
                
                if s[j]=='[' and visited[j]==0:
                    x=j
                if s[j]==']' and visited[j]==0:
                    y=j
                    break
            print(j,s[j],visited[j])
            s2=""
            print("s[k] ",s[k],x,y,s[x+1:y])
            for i in range(int(num)):
                joins=""
                joins=joins.join(s[x+1:y])
                s2=s2+joins
            visited[x:y+1]=[1]*(y+1-x)
            arr=list(s)
            arr[k]=s2
            arr[x:y+1]=[""]*(y+1-x)
            print("array ",arr)
            #modstring=""
            #modstring=modstring.join(arr)
            #s=modstring
            s=arr
            print(visited)
            print(s)
            #visited=[0]*len(s)
        for i in origs:
            if(i.isnumeric()):
                temp=""
                return temp.join(s)
        temp=""
        return temp.join(s)
                
            
obj=Solution()
s = "3[a]2[bc]"
print(obj.decodeString(s))