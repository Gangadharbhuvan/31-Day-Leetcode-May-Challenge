'''
    You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents the coordinate of a point. Check if these points make a straight line in the XY plane.

 

 

Example 1:



Input: coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
Output: true
Example 2:



Input: coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
Output: false
 

Constraints:

2 <= coordinates.length <= 1000
coordinates[i].length == 2
-10^4 <= coordinates[i][0], coordinates[i][1] <= 10^4
coordinates contains no duplicate point.

   Hide Hint #1  
If there're only 2 points, return true.

   Hide Hint #2  
Check if all other points lie on the line defined by the first 2 points.

   Hide Hint #3  
Use cross product to check collinearity.


'''

class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if len(coordinates) == 2:
            return True
        try:
            slope = (coordinates[1][1] - coordinates[0][1])/(coordinates[1][0] - coordinates[0][0])
        except:
            slope = None
        for i in range(2,len(coordinates)):
            try:
                m = (coordinates[i][1] - coordinates[0][1])/(coordinates[i][0] - coordinates[0][0])
            except:
                m = None
            if m != slope:
                return False
        return True
        