#1. 10818_최소,최대
# a = int(input())
# my_list = list(map(int, input().split()))
# print('{} {}'.format(min(my_list),max(my_list)))

#2. 2562_최대값
# my_list = []
# for i in range(1, 10):
#     my_list.append(int(input()))
#
# for i in enumerate(my_list):
#     if max(my_list) == i[1]:
#         print(i[1])
#         print(i[0] + 1, end='')

#3. 2577_숫자의 개수
# a = int(input())
# b = int(input())
# c = int(input())
# my_number = str(a*b*c)
#
# for i in range(10):
#     count = 0
#     for x in my_number:
#         if i == int(x):
#             count += 1
#
#         else:
#             pass
#     print(count)

#4. 3052_나머지
# my_list = []
# for i in range(0, 10):
#     my_list.append((int(input())%42))
#
# print(len(list(set(my_list))))

#5. 1546_평균
# N = int(input())
# my_list = list(map(int, input().split()))
# M = max(my_list)
# mean = 0
# for i in my_list:
#     mean += (100 * i /M)/N
# print(mean)

#6. 4344_평균은 넘겠지
# N = int(input())
#
# for i in range(N):
#     my_list = list(map(int, input().split()))
#     first_mylist = my_list[0]
#     my_list.pop(0)
#     mean = sum(my_list) / first_mylist
#     count = 0
#     for i in my_list:
#         if mean < i:
#             count += 1
#         percent = round(100 * (count / first_mylist), 3)
#     print("{:.3f}{}".format(percent, '%'))


# print('%.3f' % percent)


#7. 8958_OX 퀴즈
# def my_func(a):
#     my_list = []
#     for i in a:
#         my_list.append(i)
#
#     new_my_list = list()
#     for i in enumerate(my_list):
#         if i[1] =='X':
#             new_my_list.append(i[0])
#     score = 0
#
#     if new_my_list == list():
#         for z in range(len(a)+1):
#             score += z
#
# # 첫수
#     else:
#         for z in range(new_my_list[0]+1):
#             score += z
#
# #끝수
#         for z in range(len(a) - new_my_list[-1]):
#             score += z
#
#
# # 중간수
#         for z in range(len(new_my_list)-1):
#             for w in range(new_my_list[z+1] - new_my_list[z]):
#                 score += w
#
#     return print(score)
#
#
# N = int(input())
# my_list = []
# for i in range(N):
#     my_list.append(input())
#
# for a in my_list:
#     my_func(a)


def solve(a: list):
    count = 0
    for i in a:
        count += i
    return print(count)
