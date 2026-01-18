class Solution: 
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        rslt = []
        nums.sort()


        # 함수 정의 for 효율성
        def skip_forward(m: int, r: int) -> int:
            while m < r and nums[m] == nums[m - 1]:  # 중복 제거
                m += 1
            return m
        
        def skip_backward(m: int, r: int) -> int:
            while m < r and nums[r] == nums[r + 1]:  # 중복 제거
                r -= 1
            return r


        for i in range(len(nums) - 1):
            # Two Pointer 활용
            l = i  # 고정
            m = i + 1
            r = len(nums) - 1
            
            # 중복 제거 / 맨 처음은 예외 (ex. input : [0,0,0])
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            while i < m and m < r:
                total = nums[l] + nums[m] + nums[r]

                if total == 0:
                    rslt.append([nums[l], nums[m], nums[r]])
                    m += 1  # 무한 roop 방지
                    r -= 1
                    m = skip_forward(m, r)
                    r = skip_backward(m, r)
                elif total < 0:
                    m += 1
                    m = skip_forward(m, r)
                else:
                    r -= 1
                    r = skip_backward(m, r)
        
        return rslt