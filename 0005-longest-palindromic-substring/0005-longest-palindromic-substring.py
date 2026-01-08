class Solution:
    def longestPalindrome(self, s: str) -> str:
        # 길이가 1이면 문자열을 그대로 return 하십시오.
        if len(s)==1:
            return s
        
        res = ""
        
        # 홀수 길이 ex) a aba
        for i in range(len(s)):
            l, r = i, i
            while l>=0 and r<len(s) and s[l] == s[r]:
                word = s[l:r+1]
                if len(word) > len(res):
                    res = word
                l-=1
                r+=1


        # 짝수 길이 ex) abba
        for i in range(len(s)):
            l, r = i, i+1
            while l>=0 and r<len(s) and s[l] == s[r]:
                word = s[l:r+1]
                if len(word) > len(res):
                    res = word
                l-=1
                r+=1

        return res