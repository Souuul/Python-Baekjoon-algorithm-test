#1. 11654_아스키코드

# chr(45)
# ord("A")
# a= input()
# print(ord(a))

#2. 11720_숫자의 합
# import sys
# a = int(sys.stdin.readline())
# b = int(sys.stdin.readline())
# sum_number = 0
# for i in str(b):
#     sum_number += int(i)
# print(sum_number)

#3. 10809_알파벳 찾기

# import string, sys
# a = sys.stdin.readline()
# for i in string.ascii_lowercase:
#     print(a.find(i), end=' ')

#4. 2675_문자열 반복(alphanumeric)

# import sys
# a = int(sys.stdin.readline())
# for x in range(a):
#     my_str = str()
#     b, c = sys.stdin.readline().split()
#     for i in str(c):
#         my_str += (i*int(b))
#     print(my_str)

#5. 1157_단어공부
# import string
# a = str(input())
# my_dict = {}
# for i in string.ascii_uppercase:
#     my_dict[i] = a.upper().count(i)
# b = sorted(my_dict.items(), key=lambda item: item[1], reverse=True)
# if b[0][1] == b[1][1]:
#     print('?')
# else:
#     print(b[0][0])

#6. 1152_단어의 개수
# import sys
# a = (sys.stdin.readline().split())
# print(len(a))

#7 2908_상수
# def convert(a):
#     b = str(a)
#     c = str()
#     for i in range(len(b)-1,-1,-1):
#         c += b[i]
#     return int(c)
#
# a, b = map(int, input().split())
# if convert(a) > convert(b):
#     print(convert(a))
# else:
#     print(convert(b))

#8. 5622_다이얼
# dict 으로 풀어보자!
# my_dict = {'A': 3, 'B': 3, 'C' : 3,
#             'D' : 4, 'E' : 4, 'F' : 4,
#             'G' : 5,'H' : 5,'I' : 5,
# 'J' : 6,'K' : 6,'L' : 6,
# 'M' : 7,'N' : 7,'O' : 7,
# 'P' : 8,'Q' : 8,'R' : 8,'S' : 8,
# 'T' : 9,'U' : 9,'V' : 9,
# 'W' : 10,'X' : 10,'Y' : 10,'Z' : 10
#            }
#
# count = 0
# a = str(input())
# for i in a:
#     count += my_dict[i]
# print(count)

#9. 2941_크로아티아 알파벳
# a = str(input())
# count = len(a)
# my_list = ['c=', 'c-', 'dz=','d-','lj','nj','s=','z=']
# for i in my_list:
#     count -= a.count(i)
# print(count)

#10. 1316_그룹 단어 체커

import sys
N = int(input())
my_list = []
for ix in range(N):
    my_list.append(sys.stdin.readline())

count = 0
for i in my_list:
    len_count = 0
    for x in list(set(i)):
        if i.count(x * i.count(x)) == -1:
            break
        elif i.count(x * i.count(x)) ==1:
            len_count += len(x * i.count(x))
    if len(i) == len_count:
        count +=1
print(count)
