# module name: lec10_oracle_file.py


# 파일의 내용 --------------> DB에 입력
# 1번 미션: 파일의 내용 읽어서 오라클에 집어넣기.
# file name : ./lec10_oracle_file.txt

# str.split() -> str을 리스트로 만든다. ( ) 안에 있는 구분자로 끊어줘. 아무것도 안 넣으면 탭으로 끊음.
# str="010-1234-1234"
# list = str.split("-")
# print(list)

import cx_Oracle as cx

# 완성한 거
# def my_insert(lines):
#     conn = cx.connect("ai", "1111", "127.0.0.1:1521/XE")
#
#     if len(lines) ==8:
#         sql = """insert
#                 into emp2
#                 values(to_number(:1), :2, :3, :4, to_date(:5,'YYYY-MM-DD'), to_number(:6), to_number(:7), to_number(:8))"""
#
#     elif len(lines) ==7:
#         sql = """insert
#                 into emp2
#                 values(to_number(:1), :2, :3, :4, to_date(:5,'YYYY-MM-DD'), to_number(:6), NULL, to_number(:7))"""
#     else:
#         pass
#     cur=conn.cursor()
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
#         if len(line1)<=0:         # 이게 여기 있어야 에러 안 남.(안 그러면 읽을 거 없는데 str으로 분리하고 있음.)
#             break
#         line1 = str.split(line1)
#         print(line1)
#
#         my_insert(line1)


##-----------아래는 에러 나서 시도한 것~~~
#cx_Oracle.DatabaseError: ORA-01036: illegal variable name/number
#str format error --> 왜인지는 모르겠지만 내 옵티마이저가 멍청해서 str을 자동으로 to_date 못 함.

# def my_insert(lines):
#     conn = cx.connect("ai", "1111", "127.0.0.1:1521/XE")
#
#     if len(lines) ==8:
#         sql = """insert
#                 into emp2
#                 values(to_number(:1), :2, :3, :4, to_date(:5,'YYYY-MM-DD'), to_number(:6), to_number(:7), to_number(:8)) """
#
#     elif len(lines) ==7:
#         sql = """insert
#                 into emp2
#                 values(to_number(:1), :2, :3, :4, to_date(:5,'YYYY-MM-DD'), to_number(:6), NULL, to_number(:7)) """
#     else:
#         pass
#     cur=conn.cursor()
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
#         if len(line1)<=0:         # 이게 이 위에 있어야 에러 안 남.(안 그러면 읽을 거 없는데 str으로 분리하고 있음.)
#             break
#         line1 = str.split(line1)
#         # line1[0] = int(line1[0])  # to_number 위에서 안 하려면 직접 int로 바꿔줘야 함.
#         # line1[3] = int(line1[3])
#         # line1[5] = int(line1[5])
#         # line1[6] = int(line1[6])
#         # line1[7] = int(line1[7])
#         print(line1)
#
#         my_insert(line1)

# DB ----------------> 파일에 입력
# 1번 미션 성공 시
# 2번 미션 -> dept 테이블 값을 읽어서 ./lec10_oracle_dept.txt에 써라.

# def my_select():
#     conn = cx.connect("ai", "1111", "127.0.0.1:1521/XE")
#     sql = "select * from dept"
#     cur=conn.cursor()
#     cur.execute(sql)
#     x=""
#     for c in cur:
#         c=list(c)
#         c[0]=str(c[0])
#         x = x +"\t" +c[0]
#         x = x +"\t"+ c[1]
#         x = x +"\t"+ c[2]+"\n"
#     return(x)
#     cur.close()
#     conn.close()
#
# my_select()
#
# with open('./lec10_oracle_dept.txt', 'w') as f:
#    x=my_select()
#    f.write(x)


########################################################
########################강사님###########################
########################################################
# 1. SQL문에서 직접 문제 없나 확인
# 2. sql=에 복붙해서 def만들고 하드코딩으로 확인
# 3. cursor.execute(sql, [  여기 ])에 하드코딩해서 바인딩 문제 없나 확인
# 4. if 내가 한 거 처럼 하면 컬럼 바뀔 때마다 문제 생긴다  -> 없는 거 알아서 채우게 만들어야.(유연한 코드)

#split은 다 str으로 담는다.


# 리스트의 리스트 꼴로 만들어서 읽어주자.
# .split(‘\t’)으로 하면 Null이 공백으로 나온다.
# python file \n 없애기


list=[]
with open ('./1ec0_oracle_file') as f:
    while True:
        line=f.readline()
        if bool(line) ==False: # 더이상 읽을 게 없으면 나와라
            break
        line_list=x.split('\t')                 # ******유연한 코딩
        for i, word in enumerate(line_list):    # *********************
            line_list[i] = word.strip('\n')
            if bool(word)==False:
                line_list[i]='0'
        list.append(line_list)


#to_number~~이런 건 오라클 고유 문법.

def test_insert(list):
    conn = cx.connect("ai", "1111", "localhost:1521/XE")
    cur = conn.cursor()
    sql = """ INSERT INTO EMP2 VALUES
            (to_number(:1),:2,:3,to_number(:4),to_date(:5,'yyyy-mm-dd') 
                ,to_number(:6),to_number(:7),to_number(:8));
            """
    cur.executemany(sql, list)
    cur.close()
    conn.commit()
    conn.close()

test_insert(list)
