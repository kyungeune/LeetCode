class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        idx = []
        temp=0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i==j: continue
                if (nums[i]+nums[j])==target:
                    idx.append(i)
                    idx.append(j)
                    temp=1
                    break
            if temp==1:
                break
        return idx