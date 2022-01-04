# 네임스페이스 -> 파이썬에서는 메모리 대신 네임스페이스라는 표현을 쓴다.
# 네임 스페이스: 변수가 객체 바인딩 할 때 그 둘의 관계를 저장하는 공간
# 모든 객체가 key 값이 되어 딕셔너리로 저장됨.
# 인스턴스: 주소
# 인스턴스의 네임스페이스에 해당 변수가 존재하지 않으면 클래스의 네임스페이스에서 찾음.

# import 하면 메모리에 들어감.
#메모리는 32비트 주소값으로 이루어짐.
# import 한다고 바로 주소값 활용 가능한 건 아니고 생성자로 해서 넣으면 주소값 바인딩 됨.
# 다같이 쓰는 애. self 없는 애는 그냥 import 해서 메모리에 넣고
# self 들어간 애들은 새로운 메모리 파서 주소값에 할당

#모듈: lec08.py 같이 띄워놓고 보자.
# 모듈 = .py(확장자) 파일 : lec08_class_call.py

# dummy(5)
 # -> 그냥 불러오면 실행 안 됨.

#from 패키지(=폴더) import 모듈(.py)
# 패키지(폴더).모듈(.py)

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
# uc1=UserClass()   #__init__(self, name) 해주면 Class호출 시 (name) 넣어줘야 함.
# uc1.userSearch()
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

# ctrl 하고 가져온 함수 누르면 그 함수 def가 들어온다.

#
# print(uc1.__dir__())
#
# print(UserClass.__dict__)








#--------------------------------상속
from pkg.lec08 import MyClass  # : 이것도 가져와야됨
my=MyClass('나', 20, 'f')

my.myfunc()

my.userInfo(20)

# cd 이런짓 하지 마라.
from pkg.book.notebook import my_first_module


# ----------------------캡슐화
# print(my.__point) #에러
print(my.__dir__())
print(my._myClass__point)  ## 맹글링: 완벽한 OOP에서 캡슐하면 무슨 수를 쓰든 안 보여야 됨. 근데 접근 가능.
                           ## 파이썬이 불완전한 OOP인 이유.