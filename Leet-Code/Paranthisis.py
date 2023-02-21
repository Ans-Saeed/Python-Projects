def isValid(s):
    stack = []
    pairs = {")": "(", "]": "[", "}": "{"}
    for char in s:
        if char in pairs:
            if not stack or stack[-1] != pairs[char]:
                return False
            
            stack.pop()
        else:
            stack.append(char)
    return not stack


print("The result is",isValid("(){}[]"))