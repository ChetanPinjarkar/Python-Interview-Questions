def validate(s):
    if len(s)<=1:
        return False        
    stack = []
    for i in s:
        if i == "{" or i == "[" or i =="(":
            stack.append(i)
        else:
            if stack and ((stack[-1] == "{" and i == "}") or (stack[-1] == "[" and i == "]") or (stack[-1] == "(" and i == ")")):
                stack.pop()
            else:
                return False
    return not stack
    
if __name__ == "__main__":
    s = "{}"
    if validate(s):
        print(True)
    else:
        print(False)
