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
# my_select()
# my_select('KING')

#---------------
# 220103
# 외부 함수 불러오는 걸 API라고 한다.(???)
# API -> 파이썬에서는 패키지라고 한다.(폴더라는 뜻의 패키지랑 동음이의어)  / 일부 language는 라이브러리라고도 함.

# orveloading 문제
# 함수는 반드시 하나의 기능만 구현하게 해야함. -> 근데 위에서는 my_select 만들 때 if로 나눴다.
# 이건 사실 엄청 안 좋은 코드.(연습용)
# 이건 overloading이 안 돼서 이렇게 한 거다.

# 커서는 행별로 하나씩 읽음 -> for문을 돌아야만 한 바퀴 돈다. 데이터 많으면 너무 번거롭다.
# 커서는 close 안 하면 꽉 물고 있다.
# close 해야 데이터 받는다.!!!(혼자 쓸 때야 된다. 여러명 쓰면 첫번째 사람만 된다.)
# 안 되면 시작메뉴에서 oracle 폴더에 stop 눌러야한다.
# 데이터 연동 close 안 하면 서버 차지한다.
# 대용량 할 때 커서 대신 다른 거 하는 법 밑에서 알려주겠다.

## CRUD set 나머지를 완성해보자

# list 이용한 바인딩
def my_insert(empno,ename=None,deptno=None):
    # null이 허용되지 않는 empno 포함해서 몇 개만 불러오자.(ename, deptno는 안 넣어도 된다고 None 표기)
    # 세미콜론 넣지 마라
    conn = cx.connect("ai", "1111", "127.0.0.1:1521/XE")
    # 커넥션을 맨 위로 밖으로 빼면 안 되나? -> 그러면 동시 다발적으로 유저 들어왔을 때 한 명이 루프 돌고 있는데 다른 놈이 들어와서 닫고 나가면 원래 하던 애 멈춤.
    # 현업에서는 위에 한 번 만들고 def가 갖다 쓰고 있다. 어? 그럼 위에 설명이랑 다른데?
    # 현업에서는 커넥션 우리처럼 안 쓴다. 미리 동접 많이 가능한 커넥션 몇 천 개 만들어놓는다.(def 칠 때마다 인증 매번 하면 느려져서)
    sql = """insert
            into emp(empno, ename, deptno)
            values(:empno, :ename, :deptno) """ #변수 바인딩 :변수이름 (오라클 버전마다 좀 다름)
                                                # 변수 이름 대신 :1, :2, :3도 가능.->더 간단 (insert3)
                                                # (만약 안 되면 번호 바인딩하고 format)
    cur=conn.cursor()  #커서 for문 안 써도 된다. 데이터 뱉어올 거 없어서.
    cur.execute(sql, [empno, ename, deptno]) # 리스트로 바인딩 할 변수 나열해주기.(cur.execute는 변수 두 개 들어가는 자리기 때문)
    cur.close()
    # 자동커밋 안 된다. -> 커넥션에서 커밋해주기.
    conn.commit()
    conn.close()


# dict 이용한 바인딩
def my_insert2(empno,ename=None,deptno=None):
    # null이 허용되지 않는 empno 포함해서 몇 개만 불러오자.(ename, deptno는 안 넣어도 된다고 None 표기)
    # 세미콜론 넣지 마라
    conn = cx.connect("ai", "1111", "127.0.0.1:1521/XE")
    # 커넥션을 맨 위로 밖으로 빼면 안 되나? -> 그러면 동시 다발적으로 유저 들어왔을 때 한 명이 루프 돌고 있는데 다른 놈이 들어와서 닫고 나가면 원래 하던 애 멈춤.
    # 현업에서는 위에 한 번 만들고 def가 갖다 쓰고 있다. 어? 그럼 위에 설명이랑 다른데?
    # 현업에서는 커넥션 우리처럼 안 쓴다. 미리 동접 많이 가능한 커넥션 몇 천 개 만들어놓는다.(def 칠 때마다 인증 매번 하면 느려져서)
    sql = """insert
            into emp(empno, ename, deptno)
            values(:empno, :ename, :deptno) """ #변수 바인딩 :변수이름 (오라클 버전마다 좀 다름)
                                                # 만약 안 되면 번호 바인딩하고 format
    cur=conn.cursor()  #커서 for문 안 써도 된다. 데이터 뱉어올 거 없어서.
    cur.execute(sql, {"empno":empno, "ename":enmae, "deptno":deptno}) #dict로도 바인딩 가능(비추. 복잡해)

    cur.close()
    # 자동커밋 안 된다. -> 커넥션에서 커밋해주기.
    conn.commit()
    conn.close()

# ------------------------------****어려우면 ㄴㄴ for문 돌리삼
# 사원정보 여러 개 한 번에 리스트로 불러오겠다.(여러 개 할 때 추천)
# [ ] 한 덩어리가 sql문 한 개 -> sql문 여러번 돌릴 거면 리스트의 리스트 형태로 간다. [  [ ]  [  ] , [  ] ]

def my_insert_many(emp_list):
    # null이 허용되지 않는 empno 포함해서 몇 개만 불러오자.(ename, deptno는 안 넣어도 된다고 None 표기)
    # 세미콜론 넣지 마라
    conn = cx.connect("ai", "1111", "127.0.0.1:1521/XE")
    # 커넥션을 맨 위로 밖으로 빼면 안 되나? -> 그러면 동시 다발적으로 유저 들어왔을 때 한 명이 루프 돌고 있는데 다른 놈이 들어와서 닫고 나가면 원래 하던 애 멈춤.
    # 현업에서는 위에 한 번 만들고 def가 갖다 쓰고 있다. 어? 그럼 위에 설명이랑 다른데?
    # 현업에서는 커넥션 우리처럼 안 쓴다. 미리 동접 많이 가능한 커넥션 몇 천 개 만들어놓는다.(def 칠 때마다 인증 매번 하면 느려져서)
    sql = """insert
            into emp(empno, ename, deptno)
            values(:1, :2, :3) """ #리스트의 값의 순서로 숫자.(1부터 시작함에 유의) / 변수 바인딩 :변수이름 (오라클 버전마다 좀 다름)
                                   # 1에는 empno, 2에는 ename, 3에는 deptno 들어가는 거(들어가는 리스트의 개수가 아님)
    cur=conn.cursor()  #커서 for문 안 써도 된다. 데이터 뱉어올 거 없어서.
    cur.executemany(sql, emp_list)  # executemany 떼거지로 넣겠다. 리스트 개수만큼 루프 돈다.(cur.execute는 변수 두 개 들어가는 자리기 때문)
    cur.close()
    # 자동커밋 안 된다. -> 커넥션에서 커밋해주기.
    conn.commit()
    conn.close()

# ------------------------------****
# 바인딩 할 때 좀더 편한 방법.
def my_insert3(empno,ename=None,deptno=None):
    # null이 허용되지 않는 empno 포함해서 몇 개만 불러오자.(ename, deptno는 안 넣어도 된다고 None 표기)
    # 세미콜론 넣지 마라
    conn = cx.connect("ai", "1111", "127.0.0.1:1521/XE")
    # 커넥션을 맨 위로 밖으로 빼면 안 되나? -> 그러면 동시 다발적으로 유저 들어왔을 때 한 명이 루프 돌고 있는데 다른 놈이 들어와서 닫고 나가면 원래 하던 애 멈춤.
    # 커넥션을 맨 위로 밖으로 빼면 안 되나? -> 그러면 동시 다발적으로 유저 들어왔을 때 한 명이 루프 돌고 있는데 다른 놈이 들어와서 닫고 나가면 원래 하던 애 멈춤.
    # 현업에서는 위에 한 번 만들고 def가 갖다 쓰고 있다. 어? 그럼 위에 설명이랑 다른데?
    # 현업에서는 커넥션 우리처럼 안 쓴다. 미리 동접 많이 가능한 커넥션 몇 천 개 만들어놓는다.(def 칠 때마다 인증 매번 하면 느려져서)
    sql = """insert
            into emp(empno, ename, deptno)
            values(:1, :2, :3) """ #변수 바인딩 :변수순서 (오라클 버전마다 좀 다름)
    cur=conn.cursor()  #커서 for문 안 써도 된다. 데이터 뱉어올 거 없어서.
    cur.execute(sql, [empno, ename, deptno]) # 리스트로 바인딩 할 변수 나열해주기.(cur.execute는 변수 두 개 들어가는 자리기 때문)
    cur.close()
    # 자동커밋 안 된다. -> 커넥션에서 커밋해주기.
    conn.commit()
    conn.close()


# -> many랑 insert3 방법 추천
# 백지타이핑 어렵다 원리를 이해해라!!!-> cx_oracle 원시코드 깃허브에 있다. 여기 API 참고해라.

# sal increase도 담으려다 실패!!
# 숫자로 바인딩 시괄호 필요 없다! (바인딩 숫자 순서는 execute에 있는 리스트 순서로! 변수 순서 아님)

# update로 수정 가능하다. -> 튜플이라 하지 않았나?
# 이건 직접 데이터 가져와서 하는 거라 가능.

# def my_update(empno, salinc, deptno):
#     conn = cx.connect("ai", "1111", "127.0.0.1:1521/XE")
#     sql = """update emp
#             set sal = nvl(sal) + :2, deptno = :3
#             where empno = :1"""
#     cur=conn.cursor()  #커서 for문 안 써도 된다. 데이터 뱉어올 거 없어서.
#     cur.execute(sql, [empno, salinc, deptno])
#     cur.close()
#     # 자동커밋 안 된다. -> 커넥션에서 커밋해주기.
#     conn.commit()
#     conn.close()

def my_update22(empno):
    conn = cx.connect("ai", "1111", "127.0.0.1:1521/XE")
    sql = """update emp
            set sal = nvl(sal,0) + 1000, deptno =40 
            where empno = (:1)"""
    cur=conn.cursor()  #커서 for문 안 써도 된다. 데이터 뱉어올 거 없어서.
    cur.execute(sql, [empno])
    cur.close()
    # 자동커밋 안 된다. -> 커넥션에서 커밋해주기.
    conn.commit()
    conn.close()

# 강사님
# execute(str, *args: 떼거지로(리스트)) 설명 이렇게 되어 있다.

def my_update( deptno, empno,):
    conn = cx.connect("ai", "1111", "127.0.0.1:1521/XE")
    sql = """update emp
            set sal = nvl(sal,0) + 1000, deptno = :1 
            where empno = :2"""
    cur=conn.cursor()  #커서 for문 안 써도 된다. 데이터 뱉어올 거 없어서.
    cur.execute(sql, [deptno,empno])
    cur.close()
    # 자동커밋 안 된다. -> 커넥션에서 커밋해주기.
    conn.commit()
    conn.close()

### 리스트로 불러올 때 : 여러 개 불러오기.
def my_update2( list2,):
    conn = cx.connect("ai", "1111", "127.0.0.1:1521/XE")
    sql = """update emp
            set sal = nvl(sal,0) + 1000, deptno = :1 
            where empno = :2"""
    cur=conn.cursor()  #커서 for문 안 써도 된다. 데이터 뱉어올 거 없어서.
    cur.executemany(sql, list2) #리스트에 리스트로 데이터가 들어와야 한다. [[]]
    cur.close()
    # 자동커밋 안 된다. -> 커넥션에서 커밋해주기.
    conn.commit()
    conn.close()

### 리스트로 불러올 때 : 한 사람 것만 불러오기.(굳이...?????? 한 사람 할 거면 그냥 1 방법으로 해라 왜 굳이 리스트에 담아서 순서 넣냐)
def my_update3( list2):
    conn = cx.connect("ai", "1111", "127.0.0.1:1521/XE")
    sql = """update emp
            set sal = nvl(sal,0) + 1000, deptno = :1 
            where empno = :2"""
    cur=conn.cursor()  #커서 for문 안 써도 된다. 데이터 뱉어올 거 없어서.
    cur.execute(sql, [list2[0],list2[1]]) # [1,2,3] 개별값으로 넣어야함.
    # cur.execute(sql, [list2]) #이렇게 하면 에러!!! 이렇게 할 거면 excutemany로 써야됨.
                                # execute 할 거면 그냥 [0], [1] 빼고 list2 쓰던가
    cur.close()
    # 자동커밋 안 된다. -> 커넥션에서 커밋해주기.
    conn.commit()
    conn.close()

# 오라클에서 연습하고 commit이나 rollback 안 하고 여기서 commit 하면 에러 난다.
# (오라클에서 열려 있는 상태가lock걸림)


# 10번부서 사람들 삭제
def my_delete(deptno):
    conn = cx.connect("ai", "1111", "127.0.0.1:1521/XE")
    sql = """delete from emp
            where deptno= :1
            """
    cur=conn.cursor()  #커서 for문 안 써도 된다. 데이터 뱉어올 거 없어서.
    cur.execute(sql, [deptno])  # 리스트 항목 하나일 때 구버전은 뒤에 , 곡 붙여줬어야 됐다. [deptno,]
    cur.close()
    # 자동커밋 안 된다. -> 커넥션에서 커밋해주기.
    conn.commit() # 안 하면 연결 아직 열려있는 상태라 오라클에 적용이 안 되는듯.
    conn.close()

 # 사번 7698 7499 7844 삭제
def my_delete2(empno_list):
    conn = cx.connect("ai", "1111", "127.0.0.1:1521/XE")
    sql = """delete from emp
            where empno in (:1, :2, :3)
                        """
    cur=conn.cursor()  #커서 for문 안 써도 된다. 데이터 뱉어올 거 없어서.
    cur.execute(sql, empno_list) # [7698, 7499, 7844]

    cur.close()
    # 자동커밋 안 된다. -> 커넥션에서 커밋해주기.
    conn.commit()
    conn.close()


# 개별 변수로 받는 경우(강사님)
def my_delete3(empno1, empno2, empno3):
    conn = cx.connect("ai", "1111", "127.0.0.1:1521/XE")
    sql = """delete from emp
            where empno in (:1, :2, :3)
                        """
    cur = conn.cursor()  #커서 for문 안 써도 된다. 데이터 뱉어올 거 없어서.
    cur.execute(sql, [empno1, empno2, empno3])  # [7698, 7499, 7844]
    cur.close()
    # 자동커밋 안 된다. -> 커넥션에서 커밋해주기.
    conn.commit()
    conn.close()

# 리스트로 받는 경우(강사님) ->>> 비추비추비추!!!!!
def my_delete4(empno_list):
    conn = cx.connect("ai", "1111", "127.0.0.1:1521/XE")
    sql = """delete from emp
            where empno in (:1, :2, :3)
                        """
    cur = conn.cursor()  #커서 for문 안 써도 된다. 데이터 뱉어올 거 없어서.
    cur.execute(sql, [empno_list[0], empno_list[1], empno_list[2]])  # [7698, 7499, 7844]
    cur.close()
    # 자동커밋 안 된다. -> 커넥션에서 커밋해주기.
    conn.commit()
    conn.close()


#-------------executemany 하는 경우!!!!!
def my_delete5(empno_list):
    conn = cx.connect("ai", "1111", "127.0.0.1:1521/XE")
    sql = """delete from emp
            where empno = :1
                        """
    cur = conn.cursor()  #커서 for문 안 써도 된다. 데이터 뱉어올 거 없어서.
    cur.executemany(sql, empno_list)  # executemany -> 리스트의 리스트를 통째로 넣음. 리스트의 리스트를 만들어서 [ [7698, 7499, 7844] ] 돌면서 넣는다.
    cur.close()
    # 자동커밋 안 된다. -> 커넥션에서 커밋해주기.
    conn.commit()
    conn.close()
# ----------------------------------------------------
# 총정리

# 강사님 거 확인




# ---------------------커서의 대안: 대용량에서
# 대용량 할 때 커서 대신 다른 거 하는 법 알려주겠다.

