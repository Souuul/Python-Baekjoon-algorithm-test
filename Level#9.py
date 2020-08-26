#1. 1712_손익분기점
# import sys
# import math
#
# my_list = list(sys.stdin.readline().split())
# A = int(my_list[0])
# B = int(my_list[1])
# C = int(my_list[2])
#
#
# if B >= C:
#     print('-1')
# else:
#     if int(A/(C-B)) == A/(C-B):
#         print(1+math.ceil(A/(C-B)))
#     else:
#         print(math.ceil(A / (C - B)))
# 첫 번째 줄에 손익분기점 즉 최초로 이익이 발생하는 판매량을 출력한다. 손익분기점이 존재하지 않으면 -1을 출력한다.


#2. 2839_설탕배달


# def my_func(kg):
#     my_list = []
#     for a in range (2+kg//5):
#         for b in range(2 + kg//3):
#             if kg == 5*a + 3*b:
#                 my_list.append(a+b)
#     if my_list == []:
#         return print(-1)
#     else:
#         my_list.sort()
#         return print(my_list[0])
#
# kg = int(input())
# my_func(kg)

#3. 2292_벌집
# def bee_house(N):
#     count = 1
#     my_list = []
#     for i in range(N):
#         if count < N:
#             count += 6*i
#             my_list.append(count)
#         else:
#             break
#
#     for z in range(1, count+1):
#         if N == 1:
#             print(1)
#         elif my_list[z-1]< N <= my_list[z]:
#             return print(z+1)
#
# N = int(input())
# bee_house(N)

#4. 1193_분수찾기
# import sys
# def find_number(N):
#     my_list = []
#     for i in range(1, N+1):
#         for x in range(1, i+1):
#             if len(my_list) >= N:
#                 break
#             elif i % 2 == 0:
#                 my_list.append((x, (1 + i -x)))
#             else:
#                 my_list.append(((1 + i -x),x ))
#     return print('{}/{}'.format(my_list[N-1][0],my_list[N-1][1]))
# find_number(int(sys.stdin.readline()))

# a = int(input())
# line = 0
#
# while line < a:
#     a -= line
#     line += 1
#
# if line % 2 == 0:
#     print('{}/{}'.format(a, (line-a+1)))
# else:
#     print('{}/{}'.format((line-a+1),a))

#5. 2869_달팰이는 올라가고 싶다
# import sys
# A, B, V = sys.stdin.readline()
# A, B, V = map(int, input().split())
# day = 0
# while V > 0:
#     V -=  A
#     day += 1
#     if V > 0:
#         V += B
#     else:
#         break
# print(day)
# A, B, V = map(int, input().split())
# if (V - B) % (A - B) == 0:
#     print((V - B) // (A - B))
# else:
#     print(1+(V - B) // (A - B))

#6. 10250_ACM호텔
# T = int(input())
# for i in range(T):
#     H, W, N = map(int, input().split())
#
#     if N%H == 0:
#         print(H*100+N//H)
#
#     else:
#         print(N%H*100 +N//H+1)

#7. 2775_부녀회장이 될테야

# def floor(k ,n):
#     my_total_list = []
#     for x in range(k+1):
#         my_list = []
#         for i in range(1, n+1):
#             if x == 0:
#                 my_list.append(i)
#             else:
#                 my_list.append(sum(my_total_list[x-1][:i]))
#         my_total_list.append(my_list)
#     return print(my_total_list[-1][-1])
#
# T = int(input())
# for _ in range(T):
#     k = int(input())
#     n = int(input())
#     floor(k, n)





#8. 1011_fly me to the Alpha Centauri
# 처음과 마지막 이동거리 1
# T = int(input())
# my_list = []
# for i in range(T):
#     x, y = map(int, input().split())
#     distance = y-x
#     k = 1
#     p = 1
#     while distance > 0:
#         distance -= k
#         k += 1
#         if distance >= p:
#             distance -= p
#             p += 1
#
#     my_list.append(k+p-2)
#
# for i in my_list:
#     print(i)









