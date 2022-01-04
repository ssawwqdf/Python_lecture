##############파이썬 차원에서 데이터 형 관리하기
## DB가 뭘로 바뀌어도 돌아가게 ANSI 문법으로 쓰자. to_num이런 거 빼고 파이썬에서 캐스팅 하자
## (사실 날짜는 오라클에서 다 str으로 불러오고 대충 한 다음에 캐스팅은 오라클에서 설정하는 게 속편함)
## 데이터프레임 -> 배우면 표로 예쁘게 정리해준다.(더 간단해짐. 데이터프레임 아주 중요 모르면 교육 그만둬야됨.)
# sample =[ [111, 'kim', datetime.strptime('2020/07/18', '%Y/%m/%d')]]
#                               str->datetime      str          형태
# cx 오라클 -> 데이터프레임을 통으로 넣는 거 없다.  --> from sqlalchemy import~~~로 가능. 이거 쓸 땐 create oracle engine 해야됨.

#
# from datetime import datetime, date (폴더 이름 없으면 파이썬 내장함수) (모듈 이름과 함수 이름 같다) (저번에 할 때는 모듈을 import 했었음. 헷갈 ㄴㄴ)
# cf)))) datetime 모듈과 함수 ----------------------
# datetime이 date를 상속받는 생성자 함수로 바뀌었다.(__init__(self)  ---3.8버전--> __new__(cls) 로 바뀌었다. @classmethod 없어짐. / 클래스이름으로 접근해라.
from datetime import datetime, date #class가져온다. 내장이라 from 필요 없음. (쓰고 싶으면 from datetime) (근데 date랑 같이 하려면 from써야되는듯. 그런 모듈 없다고 나와서)
aa=date(year=20, month=1, day=8) # 클래스 안에 생성자로 넣어줘 # year= 이런 거 써주면 함수에서 정한 순서대로 안 해도 됨. 빼면 정해진 순서대로.
aa=date(2020, 1, 8)

#파이썬 날짜 type -> datetime.datetime
bb=datetime(year=20, month=1, day=8, hour=0, minute=0, second=0)
bb=datetime(2020, 1, 8, 0, 0,0)

cc='2020-01-01'

## datetime 클래스 들어가면 나오는 거.
# datetime의 부모는 date -> 년월일 받아오고 시분초 추가
# def __new__(cls, year, month=None, day=None, hour=0, minute=0, second=0,
#             microsecond=0, tzinfo=None, *, fold=0):
## 변수=0 되어있다는 건 값 안 주면 0으로 준다는 의미.
## =None 되어있다는 건 안 줘도 된다는 의미. -> 근데 가끔 day 안 주면 에러내기도 한다.(버그)

# strptime -> @classmethod(클래스로 호출해줘) /
# u1=datetime() cls 붙어있어서 둘 다 나오긴 한다. 근데 어노테이션때문에 에러남.
# u1.strptime()
# datetime.strptime() #클래스 메서드니까 이렇게 써달라.
#datetime.strptime(date_string='',format='') 형식

# datetime.strptime('1981-04-02', '%y-%m-%d')
# 시간 뺀 것도 넣기


############################강사님########################
import cx_Oracle as cx

#----------------------- 예시 -----------------
# from pkg.lec08_class import UserClass
# u1 = UserClass('kim', 64)
# u1.userInfo(22)          # 주소u1 = 인스턴스함수
# UserClass.userPrint('아무개')      # 클래스함수
# # --------------------------------------------

# from datetime.py import datetime.class
# from datetime.py import date.class
# from datetime.py import datetime.class, date.class

from datetime import datetime , date
aa = date(year=2020, month=4, day=10)
aa = date(2020,4,10)
print(aa , type(aa))

# bb = datetime().strptime('2020/07/18', '%Y/%m/%d')
bb = datetime(year=2020, month=1, day=7,   hour=0, minute=0, second=0)
bb = datetime(2020, 1, 7,1,20,33)
print(bb , type(bb))


#----------아래것만 잘 써도 성공-------------
from datetime import datetime , date
aa = date(2020,10,1)
bb = datetime(2020, 10, 1)
cc='2020-10-01'
xx= datetime.strptime(cc, '%Y-%m-%d') #시분초 안 넣으면 0시0분0초 자동으로 준다. 심지어 ms까지 필요한 경우도 있어서.
zz=date.fromisoformat(cc) #진짜 시간 필요 없고 날짜만 빼고 싶으면. / 특별한 경우. 보통은 시분초도 같이 넣음.
# 안내서 보면 oracle에 date 넣고 싶으면 cx면 datetime, pythone면 datetime이면 된다.
#------------------------------------------
print(type(aa), type(bb), type(cc), type(xx), type(zz))
print(aa, bb, cc, xx,zz)
################################################################

import cx_Oracle as cx
import datetime as dt

aa= dt.date(2020,1,10)
print(aa, type(aa))

bb=dt.datetime.strptime('2020/07/18', '%Y/%m/%d') # 원래 시분초도 필요
print(bb,type(bb))

#-------------------------------------------

#####----------

# drop table test2;
# create table test2(
# seq number,
# name varchar2(20),
# rdate  date);


## 날짜로 안 바꾸면 난 에러남...
## cx_Oracle.DatabaseError: ORA-01861: literal does not match format string

#
# def test_insert(list):
#     conn = cx.connect("ai", "1111", "localhost:1521/XE")
#     cur = conn.cursor()
#     sql = "insert into test2 values(:1,:2,:3)"
#     cur.executemany(sql, list)
#     cur.close()
#     conn.commit()
#     conn.close()
#
# list = [[3,'aa',date.fromisoformat('2022-01-01')],
#         [4,'bb',date.fromisoformat('2022-01-01')]
#        ]
# test_insert(list)

# 왠지모르겠지만 또 에러 -_-_--__-_-___-


list=[]
with open ('./lec10_oracle_file.txt') as f:
    while True:
        line=f.readline()
        if bool(line) ==False: # 더이상 읽을 게 없으면 나와라
            break
        line_list=line.split('\t')                 # ******유연한 코딩
        for i, word in enumerate(line_list):    # *********************
            line_list[i] = word.strip('\n')
            if bool(word)==False:
                line_list[i]='0'
        line_list[0] = int(line_list[0])
        line_list[3] = int(line_list[3])
        #line_list[4]= date.strptime(line_list[4],'%Y-%m-%d')
        line_list[4] = date.fromisoformat(line_list[4])
        line_list[5] = int(line_list[5])
        line_list[6] = int(line_list[6])
        line_list[7] = int(line_list[7])
        list.append(line_list)
print(list) # 날짜 이상하게 나오긴 한데 그래도 제대로 된 거다.


def test_insert(list):
    conn = cx.connect("ai", "1111", "localhost:1521/XE")
    cur = conn.cursor()
    sql = """ INSERT INTO EMP2 VALUES
            (:1,:2,:3,:4, :5,:6,:7,:8);
            """
    cur.executemany(sql, list)
    cur.close()
    conn.commit()
    conn.close()

test_insert(list)


