class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        total_customers = len(customers)
        total_waiting_time = 0
        time_cursor = 0

        for arrival, prep in customers:
            if time_cursor < arrival:
                time_cursor = arrival + prep
            else:
                time_cursor += prep

            total_waiting_time += time_cursor - arrival
        
        return total_waiting_time / total_customers
