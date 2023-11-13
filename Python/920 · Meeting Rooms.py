from typing import (
    List,
)
from lintcode import (
    Interval,
)

"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: if a person could attend all meetings
    """
    def can_attend_meetings(self, intervals: List[Interval]) -> bool:
        # Write your code here

        intervals.sort(key = lambda i: i[0])

        for i in range(1,len(intervals)):
            i1=intervals[i-1]
            i2=intervals[i]

            if i1[1] >i2[0]:
                return False
        return True        
