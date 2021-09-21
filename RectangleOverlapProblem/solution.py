class Solution:
    def rectangleOverlap(self, rect1, rect2):
        """
            If top left and bottom right coordinates are given for both rectangles(R1, R2) then the condition for their overlapping is -
            Y of top left of R1 must be greater than Y of bottom right of R2
            AND
            Y of top left of R2 must be greater than Y of bottom right of R1
            AND
            X of top left of R1 must be less than X of bottom right of R2
            AND
            X of top left of R2 must be less than X of bottom right of R1
        """
        return ((rect1[1] > rect2[3]) and (rect2[1] > rect1[3])) and ((rect1[0] < rect2[2]) and (rect2[0] < rect1[2]))


print(Solution().rectangleOverlap([0, 8, 8, 0], [5, 5, 15, 0]))
