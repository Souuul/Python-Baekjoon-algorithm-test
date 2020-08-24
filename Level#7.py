#1. 15596_정수 N개의 합 
# def solve(a):
#     ans = 0
#     for i in a:
#         ans += i
#     return ans


#2. 4673_셀프 넘버
# def d(n):
#     a = len(str(n))
#     new_number = n
#     for i in range(a):
#         new_number += int((n/(10**i))%10)
#     return new_number
#
#
# my_list = []
# for n in range(1, 10001):
#     if d(n) <= 10000:
#         my_list.append(d(n))
# newmy_list = list(set(my_list))
# for i in range(1, 10001):
#     if i not in newmy_list:
#         print(i)

#3. 1065_한수
# def hansoo(N):
#
#     if N < 100:
#         count = 0
#         count = N
#     else:
#         count = 99
#         for i in range(100, N+1):
#             my_list = []
#             my_list2 = []
#             for x in range(len(str(i))):
#                 my_list.append(int((i/(10**x))%10))
#             for z in range(len(my_list)-1):
#                 my_list2.append(my_list[z+1] - my_list[z])
#             if len(list(set(my_list2))) == 1:
#                 count += 1
#     return print(count)
#
#
# hansoo(int(input()))




