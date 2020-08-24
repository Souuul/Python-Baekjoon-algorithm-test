#1. 10039_평균점수
# import sys
# my_list = []
# for i in range(5):
#     my_list.append(int(sys.stdin.readline()))
#     if my_list[i] < 40:
#         my_list[i] = 40
# print(int(sum(my_list)/5))

#2. 5543_상근날드

# import sys
# my_burger = []
# my_drink = []
# for i in range(3):
#     my_burger.append(int(sys.stdin.readline()))
# for z in range(2):
#     my_drink.append(int(sys.stdin.readline()))
# print(min(my_burger)+min(my_drink) - 50)

#3. 10817_세수

# a,b,c = map(int, input().split())
# my_list = [a,b,c]
# my_list.sort()
# print(my_list[1])

#4. 2523_별찍기 - 13
# import sys
# a = int(sys.stdin.readline())
# for i in range(1, a+1):
#     print('*'*i)
# for i in range(a-1, 0, -1):
#     print('*'*i)

#5. 2446_별찍기 - 9
# import sys
# a = int(sys.stdin.readline())
# for i in range(a, 0, -1):
#     print(' '*(a-i)+'*'*(2*i-1))
# for i in range(2, a+1):
#     print(' '*(a-i)+'*'*(2*i-1))

#6. 10996_별찍기 -21
# import sys
# a = int(sys.stdin.readline())
# for i in range(a):
#     print("* "*(int(0.5*(a+1))))
#     print(" *"*(a//2))

