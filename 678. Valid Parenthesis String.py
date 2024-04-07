# Using Two Stack one is cantain open parenthesis and 
# other is contain close parenthesis
class Solution:
    def checkValidString(self, s: str) -> bool:
        star, open = [], []
        for i in range(len(s)):
            if s[i] == '(':
                open.append(i)
            elif s[i] == "*":
                star.append(i)
            else:
                if open:
                    open.pop()
                elif star:
                    star.pop()
                else:
                    return False
        while open:
            if not star:
                return False
            elif star[-1] > open[-1]:
                star.pop()
                open.pop()
            else: # star[-1] < open[-1]
                return False
        return True
# Not using Stack only two variable one is min_open and other is max_open
class Solution:
    def checkValidString(self, s: str) -> bool:
        min_open, max_open = 0, 0
        for i in range(len(s)):
            if s[i] == '(':
                min_open += 1
                max_open += 1
            elif s[i] == ')':
                min_open = max(0, min_open-1) # Reduce the count of minimum open parentheses
                max_open -= 1
                if max_open < 0: # More closing parentheses than opening, invalid
                    return False
            else:
                min_open = max(0, min_open-1) # Treat '*' as '('
                max_open += 1  # Treat '*' as ')'
        # Check if there are remaining open parentheses
        return min_open == 0 
                