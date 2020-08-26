#1016
# a, b = map(int, input().split())
# my_list = []
# my_new_list = []
# c = b-a+1
# count = 0
# if a == 1:
#     a += 1
#
# for i in range(2, b+1):
#     if int(i**0.5) == i**0.5:
#             my_list.append(i)
# for i in range(a, b+1):
#     for x in my_list:
#         if i % x == 0:
#             my_new_list.append(i)
#
# print(c-len(set(my_new_list)))

#1002_터렛
# N =int(input())
# for _ in range(N):
#     a,b,c,d,e,f = map(int,input().split())
#     if a==d and b==e and c ==f:
#         print(-1)
#     elif (a-d)**2 + (b-e)**2 > (c+f)**2 or (a-d)**2 + (b-e)**2 < (c-f)**2 or (a==d and b==e and c !=f):
#         print(0)
#     elif (a-d)**2 + (b-e)**2 == (c+f)**2 or (a-d)**2 + (b-e)**2 == (c-f)**2:
#         print(1)
#     elif (a-d)**2 + (b-e)**2 < (c+f)**2 or (a-d)**2 + (b-e)**2 > (c-f)**2:
#         print(2)

# 1003_피보나치 함수
# T = int(input())
# for _ in range(T):
#     N = int(input())
#     my_list = [[1,0],[0,1]]
#     for n in range(2, N+1):
#         my_list.append([my_list[n-1][0] + my_list[n-2][0], my_list[n-1][1] + my_list[n-2][1]])
#     print('{} {}'.format(my_list[N][0],my_list[N][1]))

# 1009_분산처리
# for _ in range(int(input())):
#     a,b = map(int, input().split())
#     a = int(str(a)[-1])
#     if a == 1:
#         print(1)
#     elif a == 5:
#         print(5)
#     elif a == 6:
#         print(6)
#     elif a == 0:
#         print(10)
#     else:
#         print((a**b)%10)
#
#
# for _ in range(int(input())):
#     a,b = map(int, input().split())
#     a_a = int(str(a)[-1])
#     if a_a == 5 or a_a ==6 or a_a ==1:
#         print(a_a)
#     elif a%10 == 0:
#         print(10)
#     else:
#         print((a_a ** (b%4))%10)
#
# N = int(input())
# for i in range(N):
#     a,b = map(int, input().split())
#     if a**b%10 == 0:
#         print(10)
#     else:
#         print(a**b%10)
#
#
# import sys
# N = int(sys.stdin.readline())
# for _ in range(N):
#     a, b = map(int, sys.stdin.readline().split())
#     result = [(a ** i) % 10 for i in range(1,5)][(b % 4) -1]
#     print(result if result != 0 else 10)

#1010_다리 놓기
# import sys
# N = int(sys.stdin.readline())
# for _ in range(N):
#     a, b = map(int, sys.stdin.readline().split())
#
# for i in range(1, a+1):

# count1 = 1
# count2 = 1
#
# for i in range(29, 16, -1):
#     count1 *= i
#
# for i in range(1, 14):
#     count2 *= i
#
# print(count1/count2)


# import sys
# N = int(sys.stdin.readline())
# for _ in range(N):
#     N, M = map(int, sys.stdin.readline().split())
#     count1 = 1
#     count2 = 1
#
#     for i in range(M, M-N, -1):
#         count1 *= i
#
#     for i in range(1, N+1):
#         count2 *= i
#     print(int(count1/count2))

# 4153_ 직각삼각형
# import sys
# while True:
#     a, b, c = map(int, sys.stdin.readline().split())
#     my_list = [a, b, c]
#     my_list.sort()
#
#     if a == b == c ==0 :
#         break
#     elif (my_list[0])**2 + (my_list[1])**2 == (my_list[2])**2:
#         print('right')
#     else:
#         print('wrong')



#_3009_네 번째 점
# import sys
# a ,aa = map(int, sys.stdin.readline().split())
# b ,bb = map(int, sys.stdin.readline().split())
# c, cc = map(int, sys.stdin.readline().split())
# my_list_x = [a, b, c]
# my_list_y = [aa, bb, cc]
#
# x = 0
# y = 0
# for i in my_list_x:
#     if my_list_x.count(i) == 1:
#         x = i
#     else:
#         pass
# for i in my_list_y:
#     if my_list_y.count(i) == 1:
#         y = i
#     else:
#         pass
# print('{} {}'.format(x, y))
#

#10844_쉬운 계단 수


# N = int(input())
# count = 0
# for i in range(10**(N-1), 10**(N)):
#     answer_count = 0
#     for z in range(len(str(i))-1):
#         if int(str(i)[z+1]) - int(str(i)[z]) == 1 or int(str(i)[z+1]) - int(str(i)[z]) == -1:
#             answer_count += 1
#     if answer_count == len(str(i))-1:
#         count += 1
#
# print(count%1000000000)

#1075_나누기
# a = int(input())
# b = int(input())
#
# for i in range(a - (a % 100), a+100 - (a % 100), 1):
#     if i % b == 0:
#         if i%100 >= 10:
#             print('{}'.format(i%100))
#         else:
#             print('0{}'.format(i % 100))
#         break

#1040_정수
# import sys
# N,K = map(int,sys.stdin.readline().split())
#
# while True:
#     my_list = []
#     for i in str(N):
#         my_list.append(i)
#     if len(set(my_list)) == K:
#         print(N)
#         break
#     else:
#         N += 1

#10872_팩토리얼

# a = int(input())
# b = 1
# for a in range(1, a+1):
#     b *=a
# print(b)

#1085_직사각형에서 탈출
# import sys
# n = int(sys.stdin.readline())
# my_list = [0, 1]
# for i in range (2, n+1):
#     my_list.append(my_list[i-2] + my_list[i-1])
# print(my_list[-1])

#10953_A+B-6
# T = int(input())
# for _ in range(T):
#     a, b = map(int, input().split(','))
#     print(a+b)

#1475_날짜계산
#1 ≤ E ≤ 15, 1 ≤ S ≤ 28, 1 ≤ M ≤ 19)
# E, S, M = map(int, input().split())
#
# count = 0
# Es = 1
# Ss = 1
# Ms = 1
#
# while True:
#     count += 1
#     if Es == E and Ss == S and Ms == M:
#         print(count)
#         break
#     else:
#         Es = (Es)%15+1
#         Ss = (Ss)%28+1
#         Ms = (Ms)%19+1

#1676_팩토리얼 0의 개수
# N = int(input())
# b = 1
# for i in range(1, N+1):
#     b *=i
# count = 0
#
# for z in range(len(str(b))-1, -1,-1):
#     if int(str(b)[z]) == 0:
#         count+=1
#     else:
#         break
# print(count)

#1977_완전제곱수
a = int(input())
b = int(input())
my_list = []

for i in range(1, b+1):
    if i**2 <= b and i**2 >= a:
        my_list.append(i**2)
    elif i**2 > b:
        break
if my_list == []:
    print(-1)
else:
    print(sum(my_list))
    print(min(my_list))
