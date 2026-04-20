class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "": return []

        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }
        ans = []

        def dfs(index, path):
            if index == len(digits):
                ans.append("".join(path[:]))
                return

            digit = digits[index]
            for i in range(len(digitToChar[digit])):
                path.append(digitToChar[digit][i])
                dfs(index + 1, path)
                path.pop()
        
        dfs(0, [])

        return ans