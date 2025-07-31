T = int(input())

for _ in range(T):
    line = input()
    stack = []
    VPS = "YES"

    for char in line:
        if char == '(':
            stack.append(char)
            
        elif char == ')':
            if len(stack) != 0 :
                stack.pop()
            else :
                VPS = "NO"

    if len(stack) != 0:
        VPS = "NO"

    print(VPS)