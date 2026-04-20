class TimeMap:

    def __init__(self):
        self.mapp = {}        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.mapp:
            self.mapp[key] = []

        self.mapp[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.mapp: return ""

        arr = self.mapp[key]
        if not arr: return ""

        if arr[0][1] > timestamp: return ""

        l, r = 0, len(arr) - 1

        while l <= r:
            m = (l + r) // 2

            if arr[m][1] == timestamp:
                return arr[m][0]

            if arr[m][1] > timestamp:
                r = m - 1
            elif arr[m][1] < timestamp:
                l = m + 1 

        return arr[r][0]
