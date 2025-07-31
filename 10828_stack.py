import sys

stack = []
n = int(sys.stdin.readline())

for _ in range(n):
    x = sys.stdin.readline().strip()

    if x.startswith("push"):
        _, num = x.split()
        stack.append(int(num))

    elif x == "pop":
        if stack:
            print(stack.pop())
        else:
            print(-1)

    elif x == "size":
        print(len(stack))

    elif x == "empty":
        print(0 if stack else 1)

    elif x == "top":
        if stack:
            print(stack[-1])
        else:
            print(-1)
