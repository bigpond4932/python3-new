#9개의 서로 다른 자연수가 주어질 때, 이들 중 최댓값을 찾고 
# 그 최댓값이 몇 번째 수인지를 구하는 프로그램을 작성하시오.

# for i in input():
    


# list= input()
# print(list)

# 굿맨 ~ 해냈다구~ fromat 을 쓰고 하려면 어캐 해야함?
# list = [90, 45, 70, 60, 55]
# # order = 0

# for i in range(0 , len(list)):
#     if list[i]>=60:
#         print(str(i+1) + "번 학생은 합격입니다.")
#     else:
#         print(str(i+1) + "번 학생은 불합격입니다.")

# str 부분이 1씩 올라갔으면 좋겠어 1 2 3 4 5 라는 값이 저절로 나오게 하고 싶어
# 반복할 때 마다 1씩 올라갔으면 좋겠어.


# format이라는 함수를 이용하면 
# s1 = 'name : {0}'.format('BlockDMask')
# print(s1)

# for a in range(2, 4):       # 앞에 표시하는 단 수 (2단, 3단)
#     for b in range(1, 10):  # 뒤에 곱하는 수
#         print('{0} x {1} = {2:2}'.format(a, b, a*b))

# list = [90, 45, 70, 60, 55]

# for i in range(0 , len(list)):
#     if list[i]>=60:
#         print(str(i+1) + "번 학생은 합격입니다.")
#     else:
#         print(str(i+1) + "번 학생은 불합격입니다.")


score_list = [100, 45, 70, 60, 55]
# score_list[2] = 50
# print(score_list)
for i in score_list:
    if i >= 60:
        print("합격 입니다")
    else:
        print("불합격 입니다.")

#for문은 이렇게 사용합니다.