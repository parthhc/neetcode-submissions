class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList or (beginWord == endWord):
            return 0

        n, m = len(wordList), len(wordList[0])
        nei = collections.defaultdict(list)

        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i+1:]
                nei[pattern].append(word)

        q = collections.deque()
        q.append(beginWord)
        visited = set()
        res = 1

        while q:
            level_len = len(q)
            for i in range(level_len):
                word = q.popleft()
                if word == endWord: return res
                visited.add(word)
                for i in range(len(word)):
                    pattern = word[:i] + "*" + word[i+1:]

                    for neighbour in nei[pattern]:
                        if neighbour in visited: continue
                        q.append(neighbour)
            
            res += 1

        return 0