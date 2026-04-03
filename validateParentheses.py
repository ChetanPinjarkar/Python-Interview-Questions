def paranth_valid(s):
  print(s)
  if len(s)%2!=0:
    return False

  stack = []
  matching = {']':'[', '}':'{', ')':'('}

  for char in s:
    if char in matching.values():
      stack.append(char)
    
    elif not stack or stack.pop() != matching[char]:
      return False
  return not stack


print(paranth_valid("([[]]{"))
print(paranth_valid("[{()}]"))
print(paranth_valid("[()()]{}"))
print(paranth_valid("([]"))
print(paranth_valid("([{]})"))


#### Alternative ####
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
