class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == '':
            return 0

        cnt=0  # 매번 갱신되는 cnt 값
        maxN = -1  # max cnt 값
        num=''  # 기존 str 저장
        i=0
        while i<len(s):
            x = s[i]
            if x not in num:  # 반복되지 않았다면
                num+=x
                cnt+=1
                if cnt>maxN:  # maxN 갱신
                    maxN=cnt
            else:
                # 슬라이싱을 활용한 겹친 글자 손절
                k = num.index(x)
                num = num[k+1:]
                num+=x
                cnt=len(num)
            i+=1
            print(num, cnt)

        return maxN