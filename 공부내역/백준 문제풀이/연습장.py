# 곱셈
# a= int(input())
# b= int(input())


# print(a*(b%10))
# print (a*((b%100)//10))
# print (a*(b//100))
# print (a*b)

# 시험점수 = int(input())

# if 시험점수 >= 90 and 시험점수 <= 100:
#     print("A")
# elif 시험점수 >= 80 and 시험점수 <=89:
#   print("B")
# elif 시험점수 >= 70 and 시험점수 <=79:
#     print("C")
# elif 시험점수 >= 60 and 시험점수 <=69:
#     print("D")
# else:
#     print("F")   

# 질문 왜  tab 눌러서 if 안으로 들어가면 시험점수라는 변수가 사라지는가?

# N개의 정수가 주어진다. 이 때 최솟값과 최댓값을 구하는 프로그램을 작성하라

# list =input().split()
# # print(list)

# a= int(list[0])
# b= int(list[1])
# c= int(list[2])
# d= int(list[3])
# e= int(list[4])


# if a > b and a > c and a > d and a > e:
#     print(a)
# elif b > a and b > c and b > d and b > e:
#     print(b)
# elif c > a and c > b and c > d and c > e:
#     print(c)
# elif d > a and d > b and d > c and b > e:
#     print(d)
# else:
#     print(e)

# if a < b and a < c and a < d and a < e:
#     print(a)
# elif b > a and b > c and b > d and b > e:
#     print(b)
# elif c > a and c > b and c > d and c > e:
#     print(c)
# elif d > a and d > b and d > c and b > e:
#     print(d)
# else:
#     print(e)

# list = input().split()
# print(type(list))
# for i in range(0, len(list)):
#     if

# n = int(input())
# list = input().split()
# max = int(list[0])    # 최댓값을 기록할 새로운 변수 할당
# min = int(list[0])    # 최솟값을 기록할 새로운 변수 할당

# for i in range(0, len(list)): # 6까지
#     if int(list[i]) <= min: # i 0부터 예약명단의 길이까지 반복하는 숫자 => 0 ~ 5
#         min = int(list[i])
#     if int(list[i]) >= max:
#         max = int(list[i])
# print(str(min)+" "+str(max))


#20 10 35 30 7
# list[0] =20 ->10

#해당 물음표 부분에 왜 그게 들어가는지, 반복문 어떻게 돌아가는지 간단하게 설명한번 적어주시면 좋을거같아용

# i는 0~len(list)-1 까지 변하는 변수
# 여기서 min을 구하려면 min이 첫 번째 가진 값과 list 안의 요소들의 값을 비교하고 min을 작은 쪽으로 바꿔주는 작업이 필요함=>(if 사용) 
# list의 모든 요소들하고 반복해서  (len(list)-1 번)=>(for 사용)
#작동방식
#if i == 0 list[i] == min ==20 
#if i == 1 list[i] == 10 < min => min = list[i]
#if i == 2 list[i] == 35 > min => min값은 바뀌지 않음 

# for i in range(1,):
#     print((i)*'*')
#     for j in range(0,2):
#         print('*')


# # print(3*'*')

# N = int(input())
# for i in range(0,N):
#     print(i+1*'*')

# a = print(50%4)
# print(type(a))

