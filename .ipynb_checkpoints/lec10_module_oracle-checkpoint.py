# 문법 연습 여기서 하고 주피터로 옮길 것.


#import 할 때는 pip랑 다르게 언더바 오라클
import cx_Oracle as cx
# cx_Oracle 들어가면 def 하고 뭐 있을텐데 그거 없다. -> 클래스는 아니다.
# 그러면 .py라는 건데 막상 들어가면 __init__.py 가 열린다.
# new-python package하면 구멍 뚫린 모양의 패키지가 만들어진다.
# 구멍 없는 폴더== 디렉토리, 구멍 뚫린 거 == 패키지
# 패키지에는 라이브러리가 들어있다.
# __init__.py 들어있으면 패키지 폴더로 인식한다.
# 패키지 폴더에 들어있는 다양한 .py들이 실행되기 전에 필요한 사전작업들이 __init__.py에 들어간다.

# ---------아래 것들 들어있는데 이게 다 오라클에 들어있는 것(?)
# # classes
#
# from .ApiType import ApiType
# from .Binary import Binary
# from .Connection import Connection
# from .connect import connect
# from .Cursor import Cursor
# from .Error import Error
# from .DatabaseError import DatabaseError
# from .DataError import DataError
# ...
# ...

# C:\AI\pythonProject\venv\Lib\site-packages\cx_Oracle-8.3.0.dist-info 에 들어있다.

#---------------------------------------------------------
# cx.connect("데이터베이스아이디","패스워드","로컬 IP:오라클포트번호/서비스아이디") #데이터베이스 연동
#---------------------------------------------------------

#엔터프라이즈 거 쓰면 /XE가 아니라 /orcl
# localhost = 127.0.0.1  -> 양쪽 다로 쓸 수 있다.
conn=cx.connect("ai", "1111", "127.0.0.1:1521/XE")
if bool(conn):
    print("연결성공")
else:
    print("연결실패")

# 커서를 받아와야 데이터를 읽어올 수 있다.
# 커서가 데이터에 접근하여 핸들링을 해준다.

cur =conn.cursor() # 이제 이 cur가 데이터에 접근 가능한 객체가 된다.
cur.execute("select * from emp") #execute() 하면 () 안에 있는 함수가 실행된다. -> 이게 다 cur에 담김.

# 커서 cur에 있는 애들을 c로 다 꺼낸다.
# for c in cur:
#     print(c)      # () 튜플 : 수정 삭제를 못 한다. 데이터를 튜플로 가져옴. 데이터를 READING 하기 위한 용도
#                   # # c = list(c) 이렇게 하면 할 수 있긴 한데... 왜 굳이 하지 말라는 걸 하지?

# 여러 명이 들어오면 오라클 연동이 끊긴다. -> XE 버전 매뉴얼에는 최대 15개라고 했는데 실제로는 11~13개면 끊김.
# 따라서 꼭 닫아줘야 한다.

cur.close()
conn.close()

# --------------------------------------------------------
# KING만 뽑고 싶을 때.

# conn=cx.connect("ai", "1111", "127.0.0.1:1521/XE")
# if bool(conn):
#     print("연결성공")
# else:
#     print("연결실패")
#
# # 커서를 받아와야 데이터를 읽어올 수 있다.
# # 커서가 데이터에 접근하여 핸들링을 해준다.
#
# cur =conn.cursor() # 이제 이 cur가 데이터에 접근 가능한 객체가 된다.
# cur.execute("select * from emp where ename='KING' ") #execute() 하면 () 안에 있는 함수가 실행된다. -> 이게 다 cur에 담김.
#
# # 커서 cur에 있는 애들을 c로 다 꺼낸다.
# for c in cur:
#     print(c)      # () 튜플 : 수정 삭제를 못 한다. 데이터를 튜플로 가져옴. 데이터를 READING 하기 위한 용도
#                   # # c = list(c) 이렇게 하면 할 수 있긴 한데... 왜 굳이 하지 말라는 걸 하지?
#
# # 여러 명이 들어오면 오라클 연동이 끊긴다. -> XE 버전 매뉴얼에는 최대 15개라고 했는데 실제로는 11~13개면 끊김.
# # 따라서 꼭 닫아줘야 한다.
#
# cur.close()
# conn.close()


#----------------------------------
# 이러면 동일한 코드가 반복됨.
# 변수명=None 하면 줘도 그만 안 줘도 그만.
#
def my_select(ename=None):
    conn = cx.connect("ai", "1111", "127.0.0.1:1521/XE")
    if bool(conn):
        print("연결성공")
    else:
        print("연결실패")

    cur = conn.cursor()

    if bool(ename):
        sql = f"select * from emp where ename='{ename}' "
    else:
        sql = "select * from emp"

    cur.execute(sql)
    for c in cur:
        print(c)

    cur.close()
    conn.close()


# # ------------------호출--------------------
my_select()
my_select('KING')