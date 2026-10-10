class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        mapp = {}

        for i, char in enumerate(s):
            if char in mapp:
                mapp[char][1] = max(mapp[char][1], i)
            else:
                mapp[char] = [i, i]

        intervals = list(mapp.values())
        intervals.sort(key = lambda x: x[0])
        merged_intervals = []
        merged_intervals.append(intervals[0])

        for i in range(1, len(intervals)):
            start, fin = intervals[i]
            prev_start, prev_fin = merged_intervals[-1]
            if start < prev_fin:
                merged_intervals[-1][1] = max(fin, prev_fin)
            else:
                merged_intervals.append([start, fin])
        
        res = []
        for start, fin in merged_intervals:
            res.append(fin - start + 1)

        return res