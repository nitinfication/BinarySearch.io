import heapq
class Solution:
    def solve(self, nums):
        nums=[-x for x in nums]
        heapq.heapify(nums)
        return heapq.heappop(nums) < 2*heapq.heappop(nums)
