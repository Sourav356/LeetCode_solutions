class Solution:
    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:
        def time_to_min(time_str):
            hours, mins = map(int, time_str.split(':'))
            return hours * 60 + mins
        
        start_time1, end_time1 = event1
        start_time2, end_time2 = event2
        
        start_min1 = time_to_min(start_time1)
        end_min1 = time_to_min(end_time1)
        start_min2 = time_to_min(start_time2)
        end_min2 = time_to_min(end_time2)
        
        
        return end_min1 >= start_min2 and end_min2 >= start_min1
        
        