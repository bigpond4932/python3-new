# long 타입은 int 타입이 표현할 수 없는 숫자를 표현하는데 이용함.
# import sys

# type(9223372036854775807)
# print(type(9223372036854775807 + 1))


# 예약명단 = ['홍용택', '김재원', '김희대', '정의환', '윤민혁', '아무개'] # 예약정보
# 손님 = input('고객님 성함 : ') # String 문자열 - 기본자료형

# for i in range(0, len(예약명단)): # i = 1 손님 = 김희대
#     if 예약명단[i] == 손님: # 예약명단[i] = 김재원 != 김희대
#         print(str(손님)+ '님은 '+str(i+1)+'번 째 손님입니다.' )
#         break
#     else:
#         print('예약되지 않은 손님입니다.')
#         break


# # print 를 했을 때 stop 인건가?
# # 근거를 대라

# N찍기 기찍N
# N = int(input())
# for i in range(0,N):
#     print(N-i)

# N = int(input())
# for i in range(1,10):
#     print(str(N), '*',str(i), '=',str(N*i))
#     # 이해가 잘 안가는 부분 +하고 ,하고 print 문장 쓸 때 잘 모르겠다.

# 문제 A+B -3  
# list=[]
# T = int(input())
# for i in range(0,T):
#     list.append(input().split())
#     print(list)


#     print(A+B)


# T = int(input())
# => 정답!
# list = []
# for i in range(0,T):
#     list.append(input().split())
#     A = int(list[i][0])
#     B = int(list[i][1])
#     print(A+B)

# list = [['1', '1'], ['2', '3'], ['3', '4'], ['9', '8'], ['5', '2']]
# A = int(list[1][0])
# B = int(list[1][1]) 
# print(A)

# for i in range(0, 5):
#     input().split()

# 약 10배는 쉬운 방법....
# T = int(input())
# list = []
# for i in range(0,T):
#     list = input().split()
#     print(int(list[0])+int(list[1]))


# n이 주어졌을 때, 1부터 n까지 합을 구하는 프로그램을 작성하시오.
# n = int(input())
# sum = 0 
# for i in range(1, n+1): 
#     sum += i 
# print(sum)
# ------할당연산자 a += b => a = a+b--------------

# n = int(input())
# # for i in range(1, n+1): 
# print((n*(n+1))//2)



# A+B - 7
# list=[]
# T = int(input())
# for i in range(0, T):
#     list = input().split()
#     # print(list)
#     # print(type(list[0]))
#     A = int(list[0])
#     B = int(list[1])
#     print('Case #'+ str(i+1)+ ': '+ str(A) + ' + ' + str(B) + ' = ' + str(A+B) )

# 별 찍기 -1
# N = int(input())
# for 별갯수 in range(1,N+1):
#     print(별갯수*'*')

# 별 찍기 -2
# N = int(input())
# for i in range(1,N+1):
#     print((N-i)*' ' + (i*'*'))

# # x보다 작은 수
# 작은정수=[]
# list = input().split()
# N = int(list[0])
# X = int(list[1])
# A = input().split()
# # print(A)
# for i in range(0, N):
#     if int(A[i]) < X:
#         작은정수.append(int(A[i]))
# print(" ".join(map(str, 작은정수)))
# 리스트 값 출력 시 조작방법.


# 10 5
# 1 10 4 9 2 3 8 5 7 6
# list = [1,2, 3,4]
# print(1,2,3,4)
# print(" ".join(map(str, list)))