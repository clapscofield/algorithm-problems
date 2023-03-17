"""
Leetcode Problem
https://leetcode.com/problems/detect-squares/
"""

class DetectSquares(object):

    def __init__(self):
        self.plane = defaultdict(int)
        self.points = []

    def add(self, point):
        """
        :type point: List[int]
        :rtype: None
        """
        self.plane[tuple(point)] += 1
        self.points.append(point)

    def count(self, point):
        """
        :type point: List[int]
        :rtype: int
        """
        res = 0
        px, py = point

        #check all possible diagonal values
        for x, y in self.points:
            if (abs(py - y) != abs(px - x)) or x == px or y == py: #it is not diagonal
                continue
            res += self.plane[(x,py)] * self.plane[(px, y)]

        return res

        


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)
