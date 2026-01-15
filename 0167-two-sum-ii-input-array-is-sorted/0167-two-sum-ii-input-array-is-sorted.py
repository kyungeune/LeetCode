class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        lst = []
        l=0
        r=len(numbers)-1

        while l < r:
            total = numbers[l] + numbers[r]
            if total == target:
                lst.append(l + 1)
                lst.append(r + 1)
                return lst
            elif total < target:
                l += 1
            else:
                r -= 1
        
        return lst