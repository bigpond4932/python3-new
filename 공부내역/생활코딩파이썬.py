# 데이터 타입을 중시하는 이유는 연산 방법이 다 타입별로 다르기 때문이다.
# 어떤 종류의 데이터 타입이 있는가? 각 종류별로 어떠한 연산방법이 있는가?

# 정수는 int (integer)
# 실수 float

# +  

# import math math를 실행한다.
# math. 으로 이용할 수 있는 연산들을 사용할 수 있게 된 것임.

import random
print(int(random.random()))

# 문자열=string

print(("용"+"택")) # 문자열과 문자열의 결합연산/ 
print(len("홍용택"*50))
print("홍용택".replace('홍', 'hong'))