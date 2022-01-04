# module name: lec10_oracle_file.py


# 파일의 내용 --------------> DB에 입력
# 1번 미션: 파일의 내용 읽어서 오라클에 집어넣기.
# file name : ./lec10_oracle_file.txt

# str.split() -> str을 리스트로 만든다. ( ) 안에 있는 구분자로 끊어줘. 아무것도 안 넣으면 탭으로 끊음.
# str="010-1234-1234"
# list = str.split("-")
# print(list)

import cx_Oracle as cx

conn = cx.connect("ai", "1111", "127.0.0.1:1521/XE")

sql = """insert
                    into emp2
                    values(:1, :2, :3, :4, to_date(:5,'YYYY-MM-DD'), :6, :7, :8) """
cur=conn.cursor()  #커서 안 써도 된다. 데이터 뱉어올 거 없어서.
cur.execute(sql, [7369, 'SMITH', 'CLERK', 7902, '1980-12-17', 5800, 0, 30]) # 리스트로 바인딩 할 변수 나열해주기.
cur.close()
# 자동커밋 안 된다. -> 커넥션에서 커밋해주기.
conn.commit()
conn.close()






# def my_insert(lines) :
#     try :
#         if len(lines) ==8:
#             sql = """insert
#                     into emp2
#                     values(:1, :2, :3, :4, :5, :6, :7, :8) """ #변수 바인딩 :변수순서 (오라클 버전마다 좀 다름)
#
#         elif len(lines) ==7:
#             sql = """insert
#                     into emp2
#                     values(:1, :2, :3, :4, :5, :6, NULL, :7) """ #변수 바인딩 :변수순서 (오라클 버전마다 좀 다름)
#         else:
#             pass
#         cur=conn.cursor()  #커서 안 써도 된다. 데이터 뱉어올 거 없어서.
#         cur.execute(sql, lines) # 리스트로 바인딩 할 변수 나열해주기.
#         # 자동커밋 안 된다. -> 커넥션에서 커밋해주기.
#         cur.close()
#     except BaseException  as e:
#         print("eeeeee" , e)
#
# with open('./lec10_oracle_file.txt') as f:
#     try :
#         while True:
#             line1 = f.readline()
#             if len(line1)<=0:
#                 break
#             line1 = str.split(line1)
#             line1[0] = int(line1[0])
#             line1[3] = int(line1[3])
#             line1[5] = int(line1[5])
#             line1[6] = int(line1[6])
#             line1[7] = int(line1[7])
#             print(line1)
#
#             my_insert(line1)
#     except BaseException as e:
#         print("aaa", e, line1)
#
# conn.commit()
# conn.close()

#---------------------------------------------루프 도는 속도가 너무 빠르다...
# 닫고 열고 하는 것보다 while이 빨리 도니까 에러
#cx_Oracle.DatabaseError: ORA-01036: illegal variable name/number

# def my_insert(lines):
#     conn = cx.connect("ai", "1111", "127.0.0.1:1521/XE")
#
#     if len(lines) ==8:
#         sql = """insert
#                 into emp2
#                 values(:1, :2, :3, :4, :5, :6, :7, :8) """ #변수 바인딩 :변수순서 (오라클 버전마다 좀 다름)
#
#     elif len(lines) ==7:
#         sql = """insert
#                 into emp2
#                 values(:1, :2, :3, :4, :5, :6, NULL, :7) """ #변수 바인딩 :변수순서 (오라클 버전마다 좀 다름)
#     else:
#         pass
#     cur=conn.cursor()  #커서 안 써도 된다. 데이터 뱉어올 거 없어서.
#     cur.execute(sql, lines) # 리스트로 바인딩 할 변수 나열해주기.
#     cur.close()
#     # 자동커밋 안 된다. -> 커넥션에서 커밋해주기.
#     conn.commit()
#     conn.close()
#
#
# with open('./lec10_oracle_file.txt') as f:
#     while True:
#         line1 = f.readline()
#         line1 = str.split(line1)
#         line1[0] = int(line1[0])
#         line1[3] = int(line1[3])
#         line1[5] = int(line1[5])
#         line1[6] = int(line1[6])
#         line1[7] = int(line1[7])
#         print(line1)
#         if len(line1)<=0:
#             break
#         my_insert(line1)

#----------------------------------------------------------------------------


# DB ----------------> 파일에 입력
# 1번 미션 성공 시
# 2번 미션 -> dept 테이블 값을 읽어서 ./lec10_oracle_dept.txt에 써라.

