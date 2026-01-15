class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        lst = []
        l = 0  # 왼쪽 인덱스
        r = len(numbers) - 1  # 오른쪽 인덱스

        total = numbers[l] + numbers[r]

        while l != r:
            if total == target:
                return [l+1, r+1]
            elif total < target:
                l += 1
            else:
                r -= 1

            total = numbers[l] + numbers[r]
        
        return [l+1, r+1]