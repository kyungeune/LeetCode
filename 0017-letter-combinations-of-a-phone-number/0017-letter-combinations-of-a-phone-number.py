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

            # 아래처럼 낱개로 진행됨
            # ch = "a" → backtrack(1, "a")
            # ch = "b" → backtrack(1, "b")
            # ch = "c" → backtrack(1, "c")
            
            # ch = "d" → backtrack(2, "ad")
            # ch = "e" → backtrack(2, "ae")
            # ch = "f" → backtrack(2, "af")


        backtrack(0, "")
        return rslt