class Solution:
    def findAnagrams(self, s, p):
        if(s==p):
            return [0]
        n=len(p)
        temp2=list(p)
        temp2.sort()
        arr=[]
        for i in range(len(s)):
            temp=list(s[i:i+n])
            if(len(temp)==n):
                temp.sort()
                if(temp==temp2):
                    arr.append(i)
        return (arr)
            
obj=Solution()
s="cbaebabacd"
p="abc"
obj.findAnagrams(s,p)