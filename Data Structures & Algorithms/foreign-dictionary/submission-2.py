class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        graph = {c: set() for w in words for c in w}
        rank = {c: 0 for w in words for c in w}

        for i in range(1, len(words)):
            prev_word = words[i - 1]
            word = words[i]
            min_len = min(len(prev_word), len(word))

            if len(prev_word) > len(word) and prev_word[:min_len] == word:
                return ""

            for j in range(min_len):
                if word[j] != prev_word[j]:
                    if word[j] not in graph[prev_word[j]]:
                        graph[prev_word[j]].add(word[j])
                        rank[word[j]] += 1
                    break

        q = collections.deque()
        for char, r in rank.items():
            if r == 0:
                q.append(char)

        res = []
        while q:
            char = q.popleft()
            for nei in graph[char]:
                rank[nei] -= 1
                if rank[nei] == 0:
                    q.append(nei)

            res.append(char)

        if len(res) != len(rank):
            return ""

        return ''.join(res)