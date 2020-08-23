#1. 2557_Hello World
# Hello World!를 출력하시오.
print('Hello World!')

#2. 10718_We love kriii
# 두 줄에 걸쳐 "강한친구 대한육군"을 한 줄에 한 번씩 출력한다.
print('강한친구 대한육군')
print('강한친구 대한육군')

#3. 10171_고양이

# \    /\
#  )  ( ')
# (  /  )
#  \(__)|

print("\    /\  \n )  ( ') \n(  /  ) \n \(__)| ")

#4. 10172_개

# |\_/|
# |q p|   /}
# ( 0 )"""\
# |"^"`    |
# ||_/=\\__|
print(str('|\_/|'))
print(str('|q p|   /}'))
print(str('( 0 )"""\{}'.format("")))
print(str('|"^"`    |'))
print(str('||_/=\{}\__|'.format("")))

# print('|\_/|\n|q p|   /}\n( 0 )"""\ \n|"^"`    |\n||_/=\\__|')

#5. 1000_A+B
# 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
# 입력 : 1 2 출력 : 3

# map(변환 함수, 순회 가능한 데이터)
# for name in map(conver_to_name, users):
#     print(name)
# for mail in map(lambda u: "남" if u["sex"] == "M" else "여", users):
# print(mail)

a, b = map(int, input().split())
print(a+b)

#6. 1001_A-B
# 두 정수 A와 B를 입력받은 다음, A-B를 출력하는 프로그램을 작성하시오.
# 입력 : 3 2 출력 : 1
a, b = map(int, input().split())
print(a-b)

#7. 10998_AXB
# 두 정수 A와 B를 입력받은 다음, AxB를 출력하는 프로그램을 작성하시오.
# 입력 : 1 2 출력 : 2
# 입력 : 3 4 출력 : 12
a, b = map(int, input().split())
print(a*b)

#8. 1008_A/B
# 두 정수 A와 B를 입력받은 다음, AxB를 출력하는 프로그램을 작성하시오.
# 입력 : 1 3 출력 : 0.33333
# 입력 : 4 5 출력 : 0.8
a, b = map(int, input().split())
print(a/b)

#9. 10869_사칙연산
# 두 자연수 A와 B가 주어진다. 이때, A+B, A-B, A*B, A/B(몫), A%B(나머지)를 출력하는 프로그램을 작성하시오.
a, b = map(int, input().split())
print(a+b)
print(a-b)
print(a*b)
print(a//b)
print(a%b)

#10. 10430_나머지
# 입력 : 첫째 줄에 A, B, C가 순서대로 주어진다. (2 ≤ A, B, C ≤ 10000)
# 출력 : 첫째 줄에 (A+B)%C, 둘째 줄에 ((A%C) + (B%C))%C, 셋째 줄에 (A×B)%C, 넷째 줄에 ((A%C) × (B%C))%C를 출력한다.

a, b, c = map(int, input().split())
print((a+b)%c)
print(((a%c)+(b%c))%c)
print((a*b)%c)
print(((a%c)*(b%c))%c)

#11. 2588_곱셈
# (세 자리 수) × (세 자리 수)는 다음과 같은 과정을 통하여 이루어진다.
#     472     (1)
# x   385     (2)
# -------------
#    2360     (3)
#   3776      (4)
#  1416       (5)
# -------------
#  181720     (6)

# (1)과 (2)위치에 들어갈 세 자리 자연수가 주어질 때 (3), (4), (5), (6)위치에 들어갈 값을 구하는 프로그램을 작성하시오.
a = int(input())
b = int(input())
print(a*(b%10))
print(a*((b//10)%10))
print(a*(b//100))
print(a*b)