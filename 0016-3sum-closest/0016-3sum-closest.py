class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        min_diff = 9999999999
        nums.sort()
        rslt = 0
        

        for i in range(len(nums) - 2):
            l = i + 1
            r = len(nums) - 1
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            while l < r:
                total = nums[i] + nums[l] + nums[r]
                diff = abs(total - target)
                
                if min_diff > diff:
                    min_diff = diff
                    print("min_diff:",min_diff, " i,l,r",i,l,r,"\n")
                    rslt = total
                

                if total < target:
                    l += 1
                elif total > target:
                    r -= 1
                else:
                    r -= 1
                    l += 1

        return rslt