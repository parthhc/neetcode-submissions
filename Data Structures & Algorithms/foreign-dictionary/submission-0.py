class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        if len(words) == 1: return words[0]
        
        graph = {c: set() for w in words for c in w}

        for i in range(1, len(words)):
            prev_word = words[i - 1]
            word = words[i]
            min_len = min(len(word), len(prev_word))

            # subsequent word is a substring of the previous word even though its lexographically smaller
            if len(prev_word) > len(word) and word[:min_len] == prev_word[:min_len]: 
                return ""

            for j in range(min_len):
                if word[j] != prev_word[j]:
                    graph[prev_word[j]].add(word[j])
                    break


        visited = {}
        res = []

        def dfs(char):
            if char in visited:
                return visited[char]
            
            visited[char] = True

            for adj in graph[char]:
                if dfs(adj):
                    return True

            visited[char] = False
            res.append(char)

        for char in graph.keys():
            if dfs(char):
                return ""

        res.reverse()
        return "".join(res)

            

