class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals: return intervals

        intervals.sort(key=lambda x: x[0])
        res = [intervals[0]]

        if len(intervals) == 1: return res

        for i in range(1, len(intervals)):
            prev_start, prev_fin = res[-1][0], res[-1][1]
            curr_start, curr_fin = intervals[i][0], intervals[i][1]

            if prev_fin < curr_start:
                res.append([curr_start, curr_fin])
            else:
                res[-1] = [
                    min(prev_start, curr_start),
                    max(prev_fin, curr_fin)
                ]


        return res