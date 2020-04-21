class Solution:
    def check(self,s,max):
        dic=dict()
        for i in s:
            if i not in dic:
                dic[i]=i
        if len(dic.values())>max:
            return False
        return True      
    def maxFreq(self, s, maxLetters, minSize, maxSize):
        max=0
        arr=[]
        dic=dict()
        for k in range(minSize,maxSize+1):
            for i in range(len(s)):
                if len(s[i:i+k])==k and self.check(s[i:i+k],maxLetters):
                    if s[i:i+k] not in dic:
                        #print(s[i:i+k],k)
                        dic[s[i:i+k]]=1
                    elif s[i:i+k] in dic:
                        dic[s[i:i+k]]+=1
        max1=0
        #print(dic)
        for i in dic.values():
            if max1<=i:
                max1=i
        return max1                
obj=Solution()
print(obj.maxFreq("aababcaab",2,3,4))