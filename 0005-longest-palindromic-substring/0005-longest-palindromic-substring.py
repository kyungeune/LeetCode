class Solution:
    def longestPalindrome(self, s: str) -> str:
        # 길이가 1이면 문자열을 그대로 return 하십시오.
        if len(s)==1:
            return s
        
        res = ""
        
        # 홀수 길이씩 순회합니다. ex) a aba
        for i in range(len(s)):
            # l : left, r : right
            l, r = i, i
            
            # l은 계속 작아지고, r은 계속 커지며 양 옆이 같은 경우만 palindrome로 판별
            while l >= 0 and r < len(s) and s[l] == s[r]:
                word = s[l:r+1]
                
                # 만약 단어가 기존 res보다 길다면
                if len(word) > len(res):
                    res = word
                l-=1
                r+=1


        # 짝수 길이로 순회합니다. ex) abba
        for i in range(len(s)):
            l, r = i, i+1
            while l>=0 and r<len(s) and s[l] == s[r]:
                word = s[l:r+1]
                if len(word) > len(res):
                    res = word
                l-=1
                r+=1

        return res