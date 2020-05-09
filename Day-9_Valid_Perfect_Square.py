'''
Given a positive integer num, write a function which returns True if num is a perfect square else False.

Note: Do not use any built-in library function such as sqrt.

Example 1:

Input: 16
Output: true
Example 2:

Input: 14
Output: false


'''
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        
        left,right = 0,num
        
        while left <=right:
          mid = (left + (right - left) //2)
          temp = mid * mid
          
          if temp ==  num:
            return True
          elif temp > num:
            right = mid - 1
          else:
            left = mid + 1
            
        return False