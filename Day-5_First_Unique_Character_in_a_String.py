'''
    Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
Note: You may assume the string contain only lowercase letters.


'''


class Solution:
    def firstUniqChar(self, s: str) -> int:
        counter = {}
        for char in s:
            if char in counter:
                counter[char] += 1
            else:
                counter[char] = 1
                
        for index, char in counter.items():
            if char == 1:
                return s.index(index)
        return -1