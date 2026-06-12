class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = Counter(tasks)
        max_heap = [-occ for occ in counter.values()]
        heapq.heapify(max_heap)

        time = 0
        q = collections.deque()

        while max_heap or q:
            time += 1

            if not max_heap:
                time = q[0][1]
            else:
                count = heapq.heappop(max_heap) + 1
                if count != 0:
                    q.append((count, time + n))
            
            if q and q[0][1] == time:
                heapq.heappush(max_heap, q.popleft()[0])
        
        return time



        

