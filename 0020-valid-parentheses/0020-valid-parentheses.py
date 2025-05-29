class Solution:
    def isValid(self, s: str) -> bool:
        a=[0]*len(s)
        aIdx=-1  # 마지막으로 들어있는 값

        for i in range(len(s)):
            if s[i]=='(' or s[i]=='[' or s[i]=='{':
                aIdx+=1
                a[aIdx]=s[i]
            elif s[i]==')' and i>0:
                if a[aIdx]=='(':
                    a.pop()
                    aIdx-=1
                else:
                    return False
            elif s[i]=='}' and i>0:
                if a[aIdx]=='{':
                    a.pop()
                    aIdx-=1
                else:
                    return False
            elif s[i]==']' and i>0:
                if a[aIdx]=='[':
                    a.pop()
                    aIdx-=1
                else:
                    return False
            else:
                return False
        if aIdx!=-1:
            return False
        return True