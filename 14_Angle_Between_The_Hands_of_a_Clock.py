class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        hourangle = (hour%12)*30
        minuteangle = minutes*6
        hourangle += (minutes)/2
        
        diff = abs(hourangle - minuteangle)
        return min(diff, 360-diff)