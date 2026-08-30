class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        total_customers = len(customers)
        total_waiting_time = 0
        chef_free_time = 0

        for arrival, prep in customers:
            if chef_free_time < arrival:
                chef_free_time = arrival + prep
            else:
                chef_free_time += prep

            total_waiting_time += chef_free_time - arrival
        
        return total_waiting_time / total_customers
