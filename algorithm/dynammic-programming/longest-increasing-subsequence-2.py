# leetcode problem:
#     https://leetcode.com/discuss/general-discussion/662866/dp-for-beginners-problems-patterns-sample-solutions
# Tushar's lecture: https://www.youtube.com/watch?v=CE2b_-XfVDk
# Tushar's page: https://github.com/mission-peace/interview/wiki

# Input: [10,9,2,5,3,7,101,18]
# Output: 4
# Explanation: The longest increasing subsequence is [2,3,7,101],
#              therefore the length is 4.

import numpy as np

def lis(list):
    # print ("Finding out longest increasing subsequence")
    m = []
    for v in list:
        m.append(1)
    print (m)

input = [10,9,2,5,3,7,101,18]
lis(input)