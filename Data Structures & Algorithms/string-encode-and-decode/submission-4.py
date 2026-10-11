class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""

        for s in strs:
            encoded += str(len(s)) + '@' + s

        return encoded

    def decode(self, s: str) -> List[str]:
        res = []

        i = 0
        while i < len(s):
            str_len = ""

            while s[i] != '@':
                str_len += s[i]
                i += 1
            i += 1
            
            length = int(str_len)
            word = ""
            while length > 0:
                word += s[i]
                i += 1
                length -= 1

            res.append(word)

        return res
