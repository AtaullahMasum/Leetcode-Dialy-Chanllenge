class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        
        # Sort balloons based on their end coordinates
        points.sort(key=lambda x: x[1])
        
        arrows = 1
        end = points[0][1]
        
        # Iterate through sorted balloons
        for i in range(1, len(points)):
            if points[i][0] > end:
                # Need a new arrow for the current balloon
                arrows += 1
                end = points[i][1]
        
        return arrows
        