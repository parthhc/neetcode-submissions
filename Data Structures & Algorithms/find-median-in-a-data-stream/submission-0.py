class MedianFinder:

    def __init__(self):
        self.smaller_half = []
        self.larger_half = []

    def addNum(self, num: int) -> None:
        # add
        if self.larger_half and num > self.larger_half[0]:
            heapq.heappush(self.larger_half, num)
        else:
            heapq.heappush(self.smaller_half, num * -1)

        # rebalance
        if len(self.larger_half) > len(self.smaller_half):
            val = heapq.heappop(self.larger_half)
            heapq.heappush(self.smaller_half, val * -1)
        elif len(self.smaller_half) > len(self.larger_half) + 1:
            val = heapq.heappop(self.smaller_half)
            heapq.heappush(self.larger_half, val * -1)


    def findMedian(self) -> float:
        length = len(self.smaller_half) + len(self.larger_half)
        if length % 2 == 0:
            return (self.smaller_half[0] * -1 + self.larger_half[0]) / 2

        return self.smaller_half[0] * -1
        
        