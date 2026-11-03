class Solution:
    def isValid(self, s: str) -> bool:
        stack = [] 

        matching = {
            ")": "(",
            "]": "[",
            "}": "{"        
        }


        for i in s:
            if i in matching:
                if not stack or stack[-1] != matching[i]:
                    return False

                stack.pop()
            else:
                stack.append(i)

        # Return true when stack is null, since all the matching brackets were found so it popped the         corresponsing ones when the match was found
        return len(stack) == 0 