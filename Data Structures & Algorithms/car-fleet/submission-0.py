class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [(position, speed) for position, speed in zip(position, speed)]
        pair.sort(reverse=True)

        stack = []

        for position, speed in pair:
            if stack == []: 
                stack.append((target - position) / speed)
                continue
            
            time_to_reach_end = (target - position) / speed
            if time_to_reach_end <= stack[-1]:
                continue
            else:
                stack.append(time_to_reach_end)

        return len(stack)