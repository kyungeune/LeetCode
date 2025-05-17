class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # answer = [0]*2
        # visited=[0]*len(max(nums))
        # nums = sorted(nums)
        # print(nums)
        # 논리 : sort한 후, visited는 방문하지 않고, 정답 나오는 순간 break
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