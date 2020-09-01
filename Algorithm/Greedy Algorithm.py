# 알고리즘 문제_개미전사
#1 3 1 5
# n = int(input())
# array = list(map(int, input().split()))
# d = [0] * 100
# d[0] = array[0]
# d[1] = max(array[0], array[1])
# for i in range(2,n):
#     d[i] = max(d[i-1], d[i-2] + array[i])
#     print(d[i])
#
# print(d[n-1])

# 함수 테스트
# def retune_test(n):
#     if n == 1 or n == 0:
#         print('aaaaaa')
#         print(n)
#         print('aaaaaa')
#         return 1
#     else:
#         print(n)
#         return retune_test(n-1) + retune_test(n-2)
#
# print(retune_test(5))



# 연산문제
# a = int(input())
# coin = [500, 100, 50, 10]
# count = 0
# for i in coin:
#     count += a//i
#     a = a%i
# print(count)


# 곱하기 혹은 더하기 문제
# N = 100000
# K = 7
#
# count = 0
#
# while N > 1:
#     if N % K == 0:
#         N = N / K
#
#     else:
#         N = N - 1
#
#     count += 1
# print(count)



# 곱하기 혹은 더하기
# S = input()
#
# sum_num = int(S[0])
#
# for i in range(1, len(S)):
#     if int(S[i]) <= 1:
#         sum_num += int(S[i])
#     else:
#         sum_num *= int(S[i])
#
# print(sum_num)


# S = input()
# sum_num = 0
# for i in range(0, len(S)):
#     sum_num = max(sum_num + int(S[i]), sum_num * int(S[i]))
#
# print(sum_num)