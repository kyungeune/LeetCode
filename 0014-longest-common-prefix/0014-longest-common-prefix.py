class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        answer=''
        if len(strs)==1:
            return strs[0]
        if '' in strs:
            return answer

        # answer 담기
        for i, j in zip(strs[0], strs[1]):
            if i == j:
                answer+=i
            else:
                break
        # 중간 체크
        if answer=='':
            return answer

        for i in range(2,len(strs)):
            if answer=='':
                return answer
            x = strs[i]
            # if answer in x:
            #     continue
            newOne = ''
            for j in range(len(x)):
                if len(answer)<=j:
                    break
                elif x[j] == answer[j]:
                    newOne+=x[j]
                else:
                    break
            answer=newOne

        return answer