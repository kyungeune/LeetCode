class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        min_diff = 9999999999
        nums.sort()
        rslt = 0
        
        for i in range(len(nums) - 2):
            # two pointer
            l = i + 1
            r = len(nums) - 1

            # 중복 제거
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            while l < r:
                total = nums[i] + nums[l] + nums[r]
                diff = abs(total - target)
                
                # 최소 차이를 도달한 경우
                if min_diff > diff:
                    min_diff = diff
                    # print("min_diff:",min_diff, " i,l,r",i,l,r,"\n")
                    rslt = total
                
                # pointer 이동
                if total < target:
                    l += 1
                elif total > target:
                    r -= 1
                else:
                    r -= 1
                    l += 1

        return rslt