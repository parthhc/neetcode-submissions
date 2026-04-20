class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        l, r = 0, len(people) - 1
        num_boats = 0

        while l <= r:
            left_person = people[l]
            right_person = people[r]

            num_boats += 1

            if left_person + right_person > limit:
                r -= 1
            else:
                l += 1
                r -= 1

        return num_boats
            
