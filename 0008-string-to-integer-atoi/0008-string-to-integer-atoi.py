class Solution:
    def myAtoi(self, s: str) -> int:
        minus = 0
        rslt = ""
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1

        # 1. 공백 무시!
        s = s.lstrip()
        
        # 길이는 공백이 무시된 후에 생성
        length = len(s)
        
        if length == 0:
            return 0
        
        # 2. - 는 음수로 취급!
        if s[0] == '-':
            minus = 1
            s = s[1:]  # '-' 제거
            length -= 1
        elif s[0] == '+':
            s = s[1:]  # '-' 제거
            length -= 1

        if length == 0:
            return 0
        
        # 3. 숫자를 읽다가 문자를 만나면, STOP!
        i = 0

        if s[0].isdigit() and length >= 1:
            while i < length and s[i].isdigit():
                rslt += s[i]
                i += 1
        else:
            return 0

        # 최종결과 설정
        rslt = int(rslt)
        if minus == 1:
            rslt = -rslt

        # 4. 범위를 벗어나면 제한하기!
        if int(rslt) < INT_MIN:
            return INT_MIN
        elif int(rslt) > INT_MAX:
            return INT_MAX
        
        return rslt