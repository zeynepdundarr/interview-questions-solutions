class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_volume = 0
     
        i = 0
        j = len(height) - 1

        # while i <= math.floor(len(height)) and j >= math.ceil(len(height)):
        while i != j:
            min_height = (min(height[i], height[j]))
            length = j-i
            cur_volume = min_height * length
  
            if height[i] <= height[j]:
                i += 1
            else:
                j -= 1
                                    
            if cur_volume > max_volume:
                max_volume = cur_volume

        return max_volume
    

height = [1,3,2,5,25,24,5]
sol = Solution()
answer = sol.maxArea(height)
print(answer)