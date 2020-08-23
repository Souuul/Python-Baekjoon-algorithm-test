# a, b = map(int, input().split())
# print(a+b)
# #
# #
# print(len(str(100)))
#
# a, b = map(int, input().split())
# if a > b:
#     print('>')
# elif a < b:
#         print('<')
# elif a == b:
#         print('==')
# a = int(input())
# if a % 4 == 0 and a % 400 == 0:
#     print(1)
# elif a % 4 == 0 and a % 100 == 0:
#     print(0)
# elif a % 4 == 0:
#     print(1)
# else:
#     print(0)

# a = int(input())
# print(a)

# a, b = map(int, input().split())
# if b >= 45:
#     print('{} {}'.format(a,b-45))
# elif a == 0 and  b < 45:
#     print('{} {}'.format(23,b+15))
# else:
#     print('{} {}'.format(a-1,b+15))
#
# a = int(input())
# for i in range(1, a+1):
#     print('{}{}'.format(' '*(a-i),'*'*i))
#
# l = int(input())
# for i in range(l):
#     a, b = input().split()
#     print(int(a) + int(b))
import sys
# a, b = map(int, sys.stdin.readline().split())
# print(a+b)


# T = int(input())
# for i in range(T):
#     a, b = map(int, sys.stdin.readline().split())
#     print(int(a)+int(b))

# T = int(input())
# for i in range(1, T+1):
#     a, b = map(int, sys.stdin.readline().split())
#     print('Case #{}: {}'.format(i, int(a)+int(b)))

# import sys
# # T = int(input())
# # for i in range(1, T+1):
# #     a, b = map(int, sys.stdin.readline().split())
# #     print('Case #{}: {} + {} = {}'.format(i, a, b ,int(a)+int(b)))
# a, b = map(int, sys.stdin.readline().split())
# c = list(map(int, sys.stdin.readline().split()))
#
# for i in c:
#     if i < b:
#         print(i,end=' ')

# import sys
# while True:
#     a, b = map(int, sys.stdin.readline().split())
#     if a == 0 and b == 0:
#         break
#     print(a+b)


import sys
# while True:
#     a, b = map(int, sys.stdin.readline().split())
#     print(a+b)
#
#
# while True:
#     try:
#         a, b = map(int, input().split())
#         print(a+b)
#     except:
#         break


import sys
count = 0
a = int(sys.stdin.readline())
b = a
while 1:
    b = (b%10)*10 + (b//10 + b%10)%10
    count += 1
    if a == b:
        print(count)
        break
