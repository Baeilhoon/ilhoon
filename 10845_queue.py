import sys
from collections import deque

queue = deque()
n = int(sys.stdin.readline())

for _ in range(n):
    x = sys.stdin.readline().strip()

    if x.startswith("push"):
        _, num = x.split()
        queue.append(int(num))

    elif x == "pop":
        if queue:
            print(queue.popleft())
        else:
            print(-1)

    elif x == "size":
        print(len(queue))

    elif x == "empty":
        print(0 if queue else 1)

    elif x == "front":
        if queue:
            print(queue[0])
        else:
            print(-1)

    elif x == "back":
        if queue:
            print(queue[-1])
        else:
            print(-1)