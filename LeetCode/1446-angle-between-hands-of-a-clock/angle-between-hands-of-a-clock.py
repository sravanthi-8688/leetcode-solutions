class Solution(object):
    def angleClock(self, hour, minutes):
        hour = hour % 12
        angle = abs(30 * hour + 0.5 * minutes - 6 * minutes)
        return min(angle, 360 - angle)
        