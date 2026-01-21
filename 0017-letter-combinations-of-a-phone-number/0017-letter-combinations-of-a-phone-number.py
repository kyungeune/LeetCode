class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # 딕셔너리
        phone = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        
        rslt = []

        def backtrack(index, path):
            if index == len(digits):
                rslt.append(path)
                return
            
            for i in phone[digits[index]]:
                backtrack(index + 1, path + i)

        backtrack(0, "")
        return rslt