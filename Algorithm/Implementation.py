# 동서남북 이동하기 // 방향성 정의하기
# 동북서남
# dx = [0, -1, 0, 1]
# dy = [1, 0, -1, 0]

# 현재위치
# x, y = 2, 2
#
# for i in range(4):
#     nx = x + dx[i]
#     ny = y + dy[i]
#     print(nx, ny)

# 시각
# 숫자 N 이 주어졌을때 00시 00분 00 초부터 N시 59분까지 모든시각중에서 3이 하나라도 포함되는모든경우의 수를 구한다
# N = int(input())
# count = 0
# for H in range(N+1):
#     for M in range(60):
#         for S in range(60):
#             if (str(H)+str(M)+str(S)).count('3'):
#                 count += 1
#
# print(count)

# ------------------
# 복잡도가 너무많이 나오면 DP 로
# N = int(input())
# count = 0
# for H in range(N+1):
#     for M in range(60):
#         for S in range(60):
#             if '3' in str(H)+str(M)+str(S):
#                 count += 1
#
# print(count)
# 1,1 에서 이동
# n = int(input())
# dir_list = list(map(str, input().split()))
# x, y = 1, 1
# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]
# direction = ['U', 'D', 'L', 'R']
#
# for i in dir_list:
#     ny = y + dy[direction.index(i)]
#     nx = x + dx[direction.index(i)]
#     if nx < 1 or ny < 1 or nx > n or ny > n:
#         continue
#     x, y = nx, ny
#
# print(x, y)

# 문자열 재정렬
# 알파벳 대문자와 숫자 (0~9)로 져있는 문자열이 주어지고 알파벳은 오름차순으로 정렬한뒤 숫자는 모두합한 값을 뒤에 명시한다
# 예를들어 K1KA5CB7 이라는 값이들어오면 ABCKK13을 출력한다.

import string
S = input()
sum_number = 0
str_list = []
for i in S:
    if i in string.ascii_uppercase:
        str_list.append(i)
    else:
        sum_number += int(i)
str_list.sort()
if sum_number != 0:
    str_list.append(str(sum_number))

print(''.join(str_list))


