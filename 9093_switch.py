T = int(input()) 

for _ in range(T):
    line = input()
    stack = []
    result = ''
    words = line.split()       
    
    for word in words:
        for char in word:
            stack.append(char)
        
        while stack:
            result += stack.pop()

        result += ' '  

    print(result.rstrip())  

print("-------------------------------")

for _ in range(T):
    line = input()

    words = line.split()  # 공백 기준으로 단어 나누기

    reverse= [str[::-1] for str in words]  # 각 단어 뒤집기

    print(' '.join(reverse))  # 다시 공백으로 연결

# 리스트 컨프리헨션을 쓰는 방법으로 시간복잡도는 같으나
# 걸리는 시간이 더 적다고 함