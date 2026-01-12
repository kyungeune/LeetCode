class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxW = -1
        i = 0
        j = len(height)-1

        while i < j:
            if min(height[i], height[j]) * (j - i) > maxW:
                maxW = min(height[i], height[j]) * (j - i)

            if height[i] > height[j]:
                    j -= 1
            elif height[i] < height[j]:
                i += 1
            else:
                j -= 1
                i += 1

        return maxW
                




        # 시간 초과, 논리를 바꿔야 함
        # # 가로 * 세로가 가장 큰 값 두 개 찾으면 됨
        # maxW = -1
        # minLen = 10**9
        
        # for i in range(len(height)):
        #     for j in range(i, len(height)):
        #         if 
        #         if min(height[i], height[j]) * (j - i) > maxW:
        #             maxW = min(height[i], height[j]) * (j - i)
        #             minLen = min(height[i], height[j])
    
        # return maxW