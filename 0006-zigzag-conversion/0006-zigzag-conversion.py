class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows==1:
            return s
        # 열 개수 판별 - 시간 소요 小
        cycle = 2*numRows-2
        colN = ceil(len(s) / cycle) * (numRows - 1)
        # 열 개수 판별 - 시간소요 多
        # colN = 0 # 열 개수
        # x = len(s)
        # imsi = 1
        # while x>=1:
        #     if imsi == 1:
        #         x-=numRows
        #         imsi = numRows-1
        #     else:
        #         x-=1
        #         imsi-=1
        #     colN+=1

        print(colN)
        arr=[['' for c in range(colN)] for d in range(numRows)]

        
        a = 0  # arr Index
        imsi = 1
        for j in range(colN):  # j 자체가 열 index
            if imsi == 1:  # 세로로 쫙 넣어야 하는 경우
                for i in range(numRows):
                    if a<len(s):
                        arr[i][j] = s[a]
                        a+=1
                    else:
                        break
                imsi = numRows-1
            else:  # 한 글자씩 들어가는 경우
                if a<len(s):
                    arr[imsi-1][j] = s[a]
                    a+=1
                else:
                    break
                imsi-=1
        
        answer = ''
        for c in range(numRows):
            for d in range(colN):
                if arr[c][d]!='':
                    answer+=arr[c][d]
        return answer