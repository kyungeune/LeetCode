class Solution:
    def reverse(self, x: int) -> int:
        # 음수인지 확인
        minus = 0
        # 반환할 값
        rslt = 0
        
        # 음수이면, 맨 앞 -를 제외해주기
        if x < 0:
            minus = 1
        
        # x를 양수로 변환
        x = abs(x)

        # 순서를 반대로 넣기
        while x != 0:
            rslt *= 10
            rslt += x % 10

            # 제출 가능 범위 필터링
            if rslt > 2**31 - 1:
                return 0

            x //= 10

        # 원래 음수였던 값은 양수로 변환
        if minus == 1:
            rslt = -rslt
        
        return rslt