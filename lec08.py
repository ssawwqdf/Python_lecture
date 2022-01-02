#class MyClass:
    #존재하는 모든 것 == 프로그램에 녹일 수 있는 것 ==객체
        #속성 = 값 = 변수
        #행위 = 동작 = 함수(메서드)
    #이것들을 다 담고 있는 게 class
    #class도 객체다.
# 인스턴스=self=주소

#유사한 기능끼리 묶음.
#다른 언어였으면 사실 UserClass.py 이런 식으로 하고 파일명이랑도 같게 해야 에러 안 남.
#모듈: .py(확장자) 인 파일(주피터에서 만든 인터프리터 빼고)
#-> 그래서 클래스 하려면 파이참에서 써야 한다.(주피터는 저기 있는 거 가져오기가 안 됨)
#주피터는 분석이나 시각화같은 간단한 거 할 때. 파이참 하는 건 좀더 공학적인.. 용도 다름

#객체 네 개가 담긴 class도 객체다.

#class 없이 self 쓰면 주소값으로 생각 안 한다.
def dummy(num):
    print("dummy() 함수 실행", num)


#--- self 파라미터 있는 함수는
# 반드시 생성자 만들어서 호출

# --- self 파라미터 없는 함수는
# 반드시 클래스로 호출
class UserClass:            #user관련된 게 들어오겠구나.
    # def __init__(self):    #내가 쓰지 않아도 이 부분이 기본으로 들어가 있다. 아무 내용 안 쓰면 : pass
                             #인스턴스랑 이어주는 역하.ㄹ
    #     print("생성자")     #메모리 처음 불러올 때 초기값 설정. 이렇게 쓰면 이 클래스 불러올 때마다 생성자라고 뜸.
    def __init__(self,name):   #클래스 새로 만들 때마다 그 클래스 주인 이름을 박아넣고 싶으면 이렇게 쓰면 된다.
        print(name, "생성자", self) #만약 uc1.UserClass 불러오고 (name) value 안 주면 에러.

    username = "aaa"
    userage = 0


    def userPrint(name):    #()여는 순간 self가 붙는다.
        print(f"{name}님입니다.")
    def userSearch(self):
        print(f"{self} 주소")
        pass                #아무것도 안 넣으면 에러나니까 일단 pass
    def userInsert(self):
        pass
    def userInsert2(self, name):
        print(f"{self} 주소 {name}")
    # def comparePrice(self):  ->문법상 말은 되지만 userclass라기에 뜬금
    #     pass


#class 없어도 문법 자체는 돌아간다.

#()여는 순간 self가 붙는다.
#왜일까?? self는 예약된 키워드. name처럼 막 갖다 쓰는 변수가 아니다.
#self라고 붙어있는 메서드는 해당 class를 이용해서 접근하라는 의미.
#self 안 들어간 애들은 생성자에 안 들어간다. -> 오잉 그러면 주소가 첫번째 파라미터로 들어간다는 거랑 말이 충돌하는데.

# self 들어간 애들만 메모리에 새로 파진다.
#uc.함수 하면 uc의 주소가 self에 들어간다.

#self 들어간 애들은 반드시 생성자 만들어서 넣어라
# 안 들어간 애들은 클래스에서 불러와라.

#주소값을 넣는 이유가 뭘까?
#class 내에서 변경하면 그 클래스를 쓰는 모든 생성자들이 바뀜
#이런 걸 분리하기 위해 그런 거임.
# self 넣을까말까는 이걸 다같이 쓰는 건지 유저마다 다르게 구현할 건지에 따라 결정됨.
# 설계의 문제.

#------------------------------------
# __init__ : 메모리 만들어라
# __del__ : 메모리 지워라







#----------------------------------상속
class Myclass(UserClass) :
    def __init__(self, name, age, gen) :  # 상속 받았기 때문에 name, age 안 써도 가져와진다.
        super().__init__(name, age) # super는 상속 준 class를 의미. UserClass라고 써도 된다.(u=Userclass 하고 u.__init__ ?????)
        self.gen = gen
    def myfunc(self):
        print("myfunc()..")


# from 하는 부분 강사님 코드 확인
# 패키지 > 모듈 > 클래스
#                  변수, 메서드
# import 모듈까지 하든가 클래스까지 하는 걸 제일 추천