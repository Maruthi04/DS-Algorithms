class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        ans=0
        bal=0
        s=S
        for i in range(len(s)):
            if(s[i]=='('):
                bal+=1
            else:
                bal-=1
                if(s[i-1]=='('):
                    ans+=1<<bal
        return ans
            
obj=Solution()
s="(()(()))"
print(obj.scoreOfParentheses(s))