class Solution:
    def findRepeatedDnaSequences(self, s):
        dic=dict()
        fin=[]
        for i in range(len(s)):
            if len(s[i:i+10])==10:
                if s[i:i+10] not in dic:
                    dic[s[i:i+10]]=1
                else:
                    dic[s[i:i+10]]+=1
        for i,j in dic.items():
            if j>1:
                fin.append(i)
        return fin
                
obj=Solution()
print(obj.findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"))
