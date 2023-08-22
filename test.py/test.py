import math

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_volume = 0
        for i in range(0, math.floor(len(height)/2) + 1):
            for k in range(len(height)-1, math.ceil(len(height)/2) + 1, -1):
                cur_volume = (k-i) * (min(height[i], height[k]))
                if cur_volume > max_volume:
                    max_volume = cur_volume

        return max_volume
    

height = [1,8,6,2,5,4,8,3,7]
sol = Solution()
answer = sol.maxArea(height)
print(answer)