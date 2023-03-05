
class Solution:
    def rob(self, nums):
        a = b = c = d = 0
        for i in range(len(nums)-1): 
            a, c, b, d = b, d, max(b, a + nums[i]), max(d, c + nums[i+1])
        return max(b, d, nums[0])

Time Complexity: O(n)
Space Complecity: O(1)
