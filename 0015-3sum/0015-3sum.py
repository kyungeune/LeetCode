class Solution: 
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        rslt = []
        nums.sort()
        print(nums)

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
                    while m < r and nums[m] == nums[m - 1]:  # 중복 제거
                        m += 1
                    r -= 1
                    while m < r and nums[r] == nums[r + 1]:  # 중복 제거
                        r -= 1
                elif total < 0:
                    m += 1
                    while m < r and nums[m] == nums[m - 1]:  # 중복 제거
                        m += 1
                else:
                    r -= 1
                    while m < r and nums[r] == nums[r + 1]:  # 중복 제거
                        r -= 1
        
        return rslt