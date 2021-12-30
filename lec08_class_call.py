#모듈: lec08.py 같이 띄워놓고 보자.
# 모듈 = .py(확장자) 파일 : lec08_class_call.py

# dummy(5)
 # -> 그냥 불러오면 실행 안 됨.

from pkg import lec08 #from 안 쓰면 lec08 자동완성 안 먹음


lec08.dummy(2) #lec08. 찍으면 보이는 것들이 다 객체
# 값 안 넣으면 dummy() missing 1 required positional argument: 'num'

lec08.UserClass.userPrint('혤니')

# lec08.UserClass.userSearch('haha') 문법적으로는 말이 됨. 이렇게 쓰진 마라

# uc=UserClass() #마음대로 만든 변수에 클래스 넣어라
#                 # 생성자
# uc.          #이렇게 접근해라.

from pkg.lec08 import UserClass #클래스로 잡아 들어가야 한다.
UserClass.userPrint('훗')

#self 들어간 건 생성자 만들어 써라.
uc1=UserClass()
uc1.userSearch()
# uc1 주소가 self로 들어간다.
# 에러 메세지: <pkg.lec08.UserClass object at 0x000001F2518166D0>
# uc1.userPrint('홍')
# 에러 메세지: TypeError: userPrint() takes 1 positional argument but 2 were given
# 하나 넣었는데 왜 두 개 넣었다고 할까? 생성자로 호출한 순간 주소가 들어가기 때문
# uc1.userPrint()
# 결과: <pkg.lec08.UserClass object at 0x0000020C85F566D0>님입니다.
# 주소가 첫번째 파라미터로 들어가기 때문.
uc1.userInsert2('김')
# self는 주소값이 자동 바인딩 된다.(넘겨준다.)
# self라고 안 해도 첫번째 파라미터에 주소가 넘어간다.
# 그래도 알아보기 편하라고 self
# 그래서 변수 self, name 두 개로 지정했어도 하나만 써도 에러 안 남.

# self 안 들어간 애들은 class에서 바로 실행
UserClass.userPrint('이')

uc2=UserClass
uc2.userSearch()
# 에러 메세지: <pkg.lec08.UserClass object at 0x00000258D81666D0> 주소

# -> uc1과 uc2의 주소 둘이 다르다.
