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

        l, r = 0, len(arr) - 1

        while l <= r:
            m = (l + r) // 2

            value, time = arr[m]

            if timestamp == time: return value

            if time > timestamp:
                r = m - 1
            else:
                l = m + 1
        
        return arr[r][0] if r >= 0 else ""
        
