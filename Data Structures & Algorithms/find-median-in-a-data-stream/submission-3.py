class MedianFinder:

    def __init__(self):
        self.smaller = []
        self.larger = []
        

    def addNum(self, num: int) -> None:
        if len(self.smaller) == len(self.larger):
            if self.larger and num > self.larger[0]:
                heapq.heappush(self.smaller, heapq.heappop(self.larger) * -1)
                heapq.heappush(self.larger, num)
            else:
                heapq.heappush(self.smaller, num * -1)
        else:
            if num < self.smaller[0] * -1:
                heapq.heappush(self.larger, heapq.heappop(self.smaller) * -1)
                heapq.heappush(self.smaller, num * -1)
            else:
                heapq.heappush(self.larger, num)
        

    def findMedian(self) -> float:
        if len(self.larger) < len(self.smaller):
            return self.smaller[0] * -1
        else:
            return (self.larger[0] + self.smaller[0] * -1)/2

        
        