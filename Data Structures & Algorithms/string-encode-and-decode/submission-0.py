class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs: return ''
        new_word = ""
        for i in range(len(strs)):
            new_word += str(len(strs[i])) + '#' + strs[i]
        return new_word


    def decode(self, s: str) -> List[str]:
        if not s: return []
        
        res = []
        i = 0

        while i < len(s):
            j = i
            # go to first '#'
            while s[j] != '#':
                j += 1
            # gets character behind #, which is the length
            length = int(s[i:j])
            # move i to the next character (first char of the word)
            i = j + 1
            # j moves to the end of the word
            j = i + length
            # res appends the word
            res.append(s[i:j])
            # i moves to j
            i = j
            
        return res