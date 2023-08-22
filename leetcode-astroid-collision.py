
def asteroidCollision(asteroids):
    """
    :type asteroids: List[int]
    :rtype: List[int]
    """
    stack = []
    for a in asteroids:
        while stack and a < 0 and stack[-1] > 0:
            diff = a + stack[-1]
            # if abs(a) > abs(stack)
            # pop stacks last element and push a 
            if diff < 0:
                stack.pop()
            # if abs(a) < abs(stack)
            # dont add astroid
            elif diff > 0:
                a = 0
            else: 
            # if abs(a) == abs(stack)
            # dont add both astroid
                a = 0
                stack.pop()

        if a:
            stack.append(a)
    return stack



print(asteroidCollision([5,10,-5]))