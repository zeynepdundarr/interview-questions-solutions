# def threeSum(nums):
#     """
#     :type nums: List[int]
#     :rtype: List[List[int]]
#     """
#     nums = sorted(nums)
#     triple_sum = []
#     for i in range(len(nums)):
#         s = 0
#         e = len(nums) - 1
#         triple_list = []

#         while s < len(nums) and e >= 0 and s < e:
#             if i == e: 
#                 e -= 1
#             elif i == s:
#                 s += 1
#             else:   
#                 a = nums[i]
#                 # if numbers < -a, numbers go bigger
#                 if nums[s] + nums[e] < -a:
#                     s += 1
#                 elif nums[s] + nums[e] == -a:
#                     triple_list.append(nums[i])
#                     triple_list.append(nums[s])
#                     triple_list.append(nums[e])
#                     triple_sum.append(sorted(triple_list))
#                     break
#                 # if numbers > -a, numbers go smaller
#                 else:
#                     e -= 1
#         unique_arrays = [list(t) for t in set(tuple(arr) for arr in triple_sum)]

#     return unique_arrays

# print(threeSum( [-1,0,1,2,-1,-4]))



class Solution(object):
    def threeSum(self, nums):
        nums = sorted(nums)
        triple_sum = set()
        for i in range(len(nums)):
            s = i + 1
            e = len(nums) - 1
   

            while s < len(nums) and e >= 0 and s < e:
                if i == e: 
                    e -= 1
                elif i == s:
                    s += 1
                else:   
                    a = nums[i]
                    # if numbers < -a, numbers go bigger
                    if nums[s] + nums[e] < -a:
                        s += 1
                    elif nums[s] + nums[e] == -a:
                        triple_sum.add((nums[i], nums[s], nums[e]))
                        s += 1
                    # if numbers > -a, numbers go smaller
                    else:
                        e -= 1

        return triple_sum

sol = Solution()
nums =  [-1,0,1,2,-1,-4,-2,-3,3,0,4]

print(sol.threeSum(nums))