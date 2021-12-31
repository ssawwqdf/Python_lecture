import datetime  #모듈
set_day = datetime.date(2019,3,1)
print(set_day, type(set_day))

# datetime. 입력하면 뭐뭐 쓸 수 있는지 나온다.

# datetime.date 에서 컨트롤 누르고 들어가면 여기로 들어가진다.
# def __new__(cls, year, month=None, day=None):
# 근데 설명에서는 month  없어도 된댔는데 막상 그러면 에러난다.
# 이런 오류 많음.

print(set_day.day, set_day.month, set_day.year)
# m : method. 내장 모듈을 통해 접근하는 거
# f : function. 파이썬이 기본으로 주는 거 import 필요 없다.
# p : ~. 쓰라는 얘기