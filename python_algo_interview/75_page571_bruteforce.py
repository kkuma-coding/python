nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3

"""
# 09/27/2021 13:16  Time Limit Exceeded
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        sol = []
        for i in range(len(nums)-(k-1)):
            sol.append(max(nums[i:i+k]))
        return sol
"""

for i in range(len(nums)-(k-1)):
    print(max(nums[i:i+k]))