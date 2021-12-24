# 생활코딩 파이썬 제어문[반복문 for]

# for문은 이렇게 사용합니다
# 리스트 안에 있구요 for 문은 리스트 안의 값을 순차적으로 꺼내서 for 뒤의 변수의 값으로 할당을 합니다.
# 내가 착각하고 있던 부분 for 뒤의 변수를 내가 뭔가 지정해야 한다고 생각했음. 근데 리스트 안의 원소들이 자동으로 가서 적용됨. 이름만 정하면 되는 거였음.

# 다차원 list
# 변수에 이름을 제대로 부여하면 더 쉬운 코드를 짤 수 있다.

# list = [["홍용택", "김현우", "장세준", "김태현"],["토평동","다산동","인창동","교문동"],["국비지원교육","인턴","인턴","졸업준비생"]]
# # print(list)
# # print(list[0][0])
# for 정보 in list:
#     print(정보[0])

# 정보 = 

# 구구단 만들기
# num1 = int(input())

# for num2 in range(0, 10):
#     print(num1, '*', num2, "=", num1*num2)
#     #

list = []

for i in range(0,9):
    list.append(input())
    max = list[0]
    for h in range[0,len(list)]:
        if list[h] > max:
            list[h] = max 
            print(max)
            print()
# print(list)

#=> 코드를 위에서 알아야 된다.