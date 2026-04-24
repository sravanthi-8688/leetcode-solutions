class Solution(object):
    def furthestDistanceFromOrigin(self, moves):
        """
        :type moves: str
        :rtype: int
        """
        l=moves.count('L')
        r=moves.count('R')
        empty=moves.count('_')
        return abs(l-r)+empty
                   
            
            
        