class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def isPalindrome(word: str):
            for i in range(len(word) // 2):
                if word[i] != word[len(word) - i - 1]:
                    return False
            return True

        stack = []
        res = []

        def getAllPalindoromePartions(i, path):
            if i == len(s):
                res.append(path[:])
                return
            # kinda like extending the string as much as possible to get the answer
            for j in range(i + 1, len(s) + 1):
                word = s[i:j]
                if isPalindrome(word):
                    path.append(word)
                    getAllPalindoromePartions(j, path)
                    path.pop()

        
        getAllPalindoromePartions(0, [])

        return res