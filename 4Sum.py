class Solution(object):
    def fourSum(self, nums, target):
        nums = sorted(nums)
        four_sum = set()
        for i in range(len(nums)-3):
            for j in range(i+1, len(nums)-2):
                sum =  nums[i] + nums[j] 
                u = j + 1
                k = len(nums) - 1
                searched = target - sum
                while u < k and u :
                    if nums[u] + nums[k] < searched:
                        u += 1
                    elif nums[u] + nums[k] > searched:
                        k -= 1
                    else:
                        arr = sorted((nums[i], nums[j], nums[u], nums[k]))
                        four_sum.add(tuple(arr))
                        u += 1

        return list(set(four_sum))

sol = Solution()
nums = [1,0,-1,0,-2,2]
print(sol.fourSum(nums, 0))