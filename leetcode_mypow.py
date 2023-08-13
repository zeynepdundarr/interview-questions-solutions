# class Solution(object):
#     def myPow(self, x, n):
        
#         if n == 0:
#             return 1

#         result = 1
#         if n < 0:
#             is_negative = True
#             exp = -n
        
#         while exp > 0:
#             print("exp: ", exp)
#             if exp%1 == 1:
#                 result *= x
#             x *= x
#             n //= 2


#         if is_negative: 
#             return 1/result 
#         else:
#             return result

class Solution:
    def myPow(self, base: float, exponent: int) -> float:
        if exponent == 0:
            return 1

        result = 1
        is_negative = False

        if exponent < 0:
            is_negative = True
            exponent = -exponent

        while exponent > 0:
            if exponent % 2 == 1:
                result *= base
            base *= base
            exponent //= 2

        print("exponent: ", exponent)
        return 1 / result if is_negative else result
    
sol = Solution()

print(sol.myPow(2,1))