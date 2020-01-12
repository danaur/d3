def distance_between(a: List[int], b: List[int]) -> int:
    return max(abs(b[0] - a[0]), abs(b[1] - a[1]))

class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        distance = 0
        for index in range(len(points) - 1):
            distance += distance_between(points[index], points[index+1])

        return distance
