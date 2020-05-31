'''
    Given two words word1 and word2, find the minimum number of operations required to convert word1 to word2.

You have the following 3 operations permitted on a word:

Insert a character
Delete a character
Replace a character
Example 1:

Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation: 
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')
Example 2:

Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation: 
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')






'''

class Solution:
  def minDistance(self, word1, word2):
    word1, word2 = "!" + word1, "!" + word2
    n_1, n_2 = len(word1), len(word2)
    dp = [[0] * n_2 for _ in range(n_1)]

    for i_1 in range(n_1): dp[i_1][0] = i_1
    for i_2 in range(n_2): dp[0][i_2] = i_2

    for i_1 in range(1, n_1):
      for i_2 in range(1,n_2):
        Cost = (word1[i_1] != word2[i_2])
        dp[i_1][i_2] = min(dp[i_1-1][i_2] + 1, dp[i_1][i_2-1] + 1, dp[i_1-1][i_2-1] + Cost)

    return int(dp[-1][-1])