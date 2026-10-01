class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        freq = Counter(hand)
        heap = []
        for key in freq.keys():
            heapq.heappush(heap, key)

        res = []

        while heap:
            tentative_group = [heapq.heappop(heap)]
            for _ in range(1, groupSize):
                if not heap: return False
                elem = heapq.heappop(heap)
                if elem - 1 == tentative_group[-1]:
                    tentative_group.append(elem)
                else: 
                    return False
            
            for elem in tentative_group:
                freq[elem] -= 1
                if freq[elem] != 0:
                    heapq.heappush(heap, elem)

        return True