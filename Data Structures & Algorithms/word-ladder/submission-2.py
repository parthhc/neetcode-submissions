class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        graph = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i + 1:]
                graph[pattern].append(word)

        # min so bfs
        res = 0
        q = collections.deque()
        q.append(beginWord)

        visited = set()
        while q:
            level_len = len(q)
            res += 1
            for _ in range(level_len):
                word = q.popleft()
                if word == endWord:
                    return res
                
                visited.add(word)
                for i in range(len(word)):
                    pattern = word[:i] + "*" + word[i + 1:]
                    arr = graph[pattern]
                    for same_pattern_word in arr:
                        if same_pattern_word in visited: continue
                        q.append(same_pattern_word)


        return 0