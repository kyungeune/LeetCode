class Solution:
    def romanToInt(self, s: str) -> int:
        answer = 0
        
        # 하나하나 할당하기.. 과연 이 방법이 먹힐것인가
        number = {}
        number['I'] = 1
        number['IV'] = 4
        number['V'] = 5
        number['IX'] = 9
        number['X'] = 10
        number['XL'] = 40
        number['L'] = 50
        number['XC'] = 90
        number['C'] = 100
        number['CD'] = 400
        number['D'] = 500
        number['CM'] = 900
        number['M'] = 1000

        i = 0
        while i<len(s):
            x = ''
            y = ''

            # x, y 할당
            if i+1<len(s):
                x+=s[i]+s[i+1]  # 알파벳 두개짜리 우선순위로 다뤄줘야 함
            y=s[i]
            
            # x값 존재하면 먼저 할당 후 i+=2
            if x in number:
                answer += int(number[x])
                i+=2
            else:
                answer += int(number[y])
                i+=1
            
            
        return answer


# Symbol       Value
# I             1
# IV            4
# V             5
# IX            9
# X             10
# XL            40
# L             50
# XC            90
# C             100
# CD            400
# D             500
# CM            900
# M             1000