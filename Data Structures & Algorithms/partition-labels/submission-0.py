class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        letterIdx = {}
        intervals = []

        for i in range(len(s)):
            char = s[i]
            if char in letterIdx:
                intervals[letterIdx[char]][1] = i
            else:
                intervals.append([i, -1])
                letterIdx[char] = len(intervals) - 1

        mergedIntervals = []
        for i in range(len(intervals)):
            if intervals[i][1] == -1:
                intervals[i][1] = intervals[i][0]
            if not mergedIntervals:
                mergedIntervals.append(intervals[i])
            else:
                currInterval = mergedIntervals[-1]
                if currInterval[1] > intervals[i][0]:
                    mergedIntervals[-1][1] = max(currInterval[1], intervals[i][1])
                else:
                    mergedIntervals.append(intervals[i])
        
        res = []
        for start, finish in mergedIntervals:
            res.append(finish - start + 1)
        
        return res