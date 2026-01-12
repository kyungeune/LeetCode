class Solution:
    def maxArea(self, height: List[int]) -> int:
        # 넓이
        maxW = -1  
        # 왼쪽부터 이동하는 pointer
        i = 0  
        # 오른쪽부터 이동하는 pointer
        j = len(height)-1  

        while i < j:
            # 만약 현재 넓이가 최대 넓이라면
            if min(height[i], height[j]) * (j - i) > maxW:
                maxW = min(height[i], height[j]) * (j - i)

            # i와 j 중 height가 더 작은 것을 이동시킴, 단 둘의 길이가 동일할 경우에는 둘 다 이동시킴
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