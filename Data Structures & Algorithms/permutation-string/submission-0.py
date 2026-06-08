class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        num_chars = len(s1)
        char_map = Counter(s1)

        l = 0
        freq_map = {}

        for r in range(len(s2)):
            if r - l >= num_chars:
                freq_map[s2[l]] -= 1
                l += 1
            
            freq_map[s2[r]] = freq_map.get(s2[r], 0) + 1

            if r - l == num_chars - 1:
                permutation = False
                for val in char_map.keys():
                    if val not in freq_map: 
                        permutation = False
                        break
                    if freq_map[val] != char_map[val]:
                        permutation = False
                        break
                    permutation = True

                if permutation == True: return True
        
        return False

            