class Solution: 
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        rslt = []
        nums.sort()
        n = len(nums)

        for i in range(n - 2):
            # 중복 제거 / 맨 처음은 예외 (ex. input : [0,0,0])
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            # 시간 줄이기 1 : 가지치기
            if nums[i] > 0:
                break

            # Two Pointer 활용
            l = i  # 고정
            m = i + 1
            r = n - 1

            # 시간 줄이기 2 : 조건 바꾸기
            while m < r: 
                total = nums[l] + nums[m] + nums[r]

                if total == 0:
                    rslt.append([nums[l], nums[m], nums[r]])
                    m += 1  # 무한 roop 방지
                    r -= 1

                    # ✅ m, r 중복 스킵 (정답 찾았을 때만)
                    while m < r and nums[m] == nums[m - 1]:
                        m += 1
                    while m < r and nums[r] == nums[r + 1]:
                        r -= 1
                
                elif total < 0:
                    m += 1
                else:
                    r -= 1
                    
        return rslt