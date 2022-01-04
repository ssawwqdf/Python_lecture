
import sqlalchemy as sa
import cx_Oracle
import pandas as pd
import numpy as np


#ref:https://www.daleseo.com/?tag=Python
from datetime import datetime, date
print("date(2019, 12, 25):\t\t", date(2019, 12, 25))
print("date.today():\t\t\t", date.today() )
print("date.today().isoformat() date->str:",  date.today().isoformat())
print("date.today().strftime('%Y/%m/%d') date->str:", date.today().strftime('%Y/%m/%d'))
print("date.fromisoformat('2020-07-18') str->date:",  date.fromisoformat('2020-07-18'))
print("datetime.strptime('2020/07/18', '%Y/%m/%d') str->datetime64[ns]:", datetime.strptime('2020/07/18', '%Y/%m/%d') )

'''
https://www.fun-coding.org/mysql_advanced2.html
----------------------------------------------------------------------------------------------
oracle	                    cx_Oracle	                sqlalchemy              python  
----------------------------------------------------------------------------------------------
varchar2, nvarchar2,long	cx_Oracle.STRING	        types.String(20)        str
char	                    cx_Oracle.fixed_char	                            str
number	                    cx_Oracle.number	        types.Numeric(10)       int
float	                    cx_Oracle.number	                                float
date	                    cx_Oracle.datetime	        types.Date()            datetime.datetime
timestamp	                cx_Oracle.timestamp	                                datetime.datetime
clob	                    cx_Oracle.clob	                                    object
blob	                    cx_Oracle.blob	                                    raw
'''


'''
create table news(seq number, title varchar2(20), regdate date);
insert into news values(1,'ddd',sysdate);
commit;
select * from news;
'''

''' -----------------------------------------------
MySQL Connect
----------------------------------------------- '''
# import pymysql
# conn = pymysql.connect(host='localhost', user='tester', password='7890',
#                        db='testdb', charset='utf8')


''' -----------------------------------------------
INSERT : one-rows
----------------------------------------------- '''
# sql = """insert into customer(name,category,region)
#          values (:1, :2, :3)"""
# cursor = conn.cursor()
# cursor.execute(sql, ['홍길동', 1, '서울'])
# cursor.execute(sql, ['이연수', 2, '서울'])
# conn.commit()
# conn.close()

''' -----------------------------------------------
INSERT : multi-rows
----------------------------------------------- '''
# data_list = (
#     ('홍진우', 1, '서울'),
#     ('강지수', 2, '부산'),
#     ('김청진', 1, '서울'),
# )
# sql = """insert into customer(name,category,region)
#          values (:1, :2, :3)"""
# cursor = conn.cursor()
# curs.executemany(sql, data_list)
# conn.commit()

''' -----------------------------------------------
try: ~ with: ~ finally:
----------------------------------------------- '''
# try:
#     # INSERT
#     with conn.cursor() as curs:
#         sql = "insert into customer(name,category,region) values (%s, %s, %s)"
#         curs.execute(sql, ('이광수', 1, '서울'))
#     conn.commit()
#
#     # SELECT
#     with conn.cursor() as curs:
#         sql = "select * FROM customer"
#         curs.execute(sql)
#         rs = curs.fetchall()
#         for row in rs:
#             print(row)
# finally:
#     conn.close()


''' -----------------------------------------------
Oracle SQL execute result --> Dataframe  
                    df = pd.read_sql(SQL, conn)
----------------------------------------------- '''
# import cx_Oracle
# conn = cx_Oracle.connect("hi/0000@localhost:1521/xe")
# df = pd.read_sql("select * from news", conn)
# print(df.info())
# # 0   SEQ      1 non-null      int64
# # 1   TITLE    1 non-null      object
# # 2   REGDATE  1 non-null      datetime64[ns]



''' -----------------------------------------------
Dataframe --> Oracle insert
              test_df.to_sql(table_name, conn, ... , dtype={})
----------------------------------------------- '''
# # sample =[ [111, 'kim', datetime.strptime('2020/07/18', '%Y/%m/%d')]]
# sample =[ [111, 'kim', '2020/07/18']]
# test_df = pd.DataFrame(data=sample,  columns=['mpw','mid','regdate'])
# print(test_df.info())
# #     mpw   mid    regdate
# # 0  111  kim 2020-07-18
# '''
#  0   mpw       1 non-null      int64
#  1   mid       1 non-null      object            <---- Object  일 경우 오라클 타입은 CLOB이다. --> types.String(20) 또는 "regdate":types.Date()
#  2   regdate   1 non-null      datetime64[ns]    <---- datetime일 경우 오라클 타입은 Date이다.
#  dtypes: datetime64[ns](1), object(1), int64(1)
# '''
#
# from sqlalchemy import types, create_engine
# oracle_engine = create_engine('oracle://hi:0000@localhost:1521/XE')
# # conn2 = oracle_engine.connect()
# test_df.to_sql('table_sdf', oracle_engine, if_exists='replace', index=False
#                ,dtype={"mpw":types.Numeric(10), "mid":types.String(20), "regdate":types.Date()}
#                )


import sqlalchemy as sa
# engine = sa.create_engine('oracle://hi:0000@localhost:1521/xe')
# engine = sa.create_engine('sqlite:///:memory:', echo=True)
engine = sa.create_engine('sqlite://', echo=True)
conn = engine.connect('mydb.db')

#---------------------------------------------------------------------------********
# ----- 데이블 생성, 레코드생성 및 조회
# conn.execute('''CREATE TABLE emp2(regdate int)''')
# conn.execute("insert into emp2 values(99)")  # 'duck', 10, 0.0)
# #ins = 'INSERT INTO zoo (critter, count, damages) VALUES(?, ?, ?)'
# curs = conn.cursor()
# rows = curs.execute("select * from emp")
# print(rows)

# ----- 데이블 생성 및 조회
# df = pd.DataFrame({"regdate":['2000-01-01','2000-01-02']})
# df.to_sql('emp', conn,  if_exists='append', index=False)  #schema='schema_name',
# df = pd.read_sql("SELECT * FROM sqlite_master WHERE type='table'", conn)
# print(df.head())

# ----- 조회결과 프레임화
# df = pd.read_sql("select * from emp", conn)
# print(df.head())
# with conn.cursor() as cursor:
#     cursor.execute("select * from emp")
#---------------------------------------------------------------------------********




''' -----------------------------------------------
SQL --> Oracle insert  --> binding(:x)
        cursor.execute('INSERT INTO table_name (col_name) values (:0)', (x,))
----------------------------------------------- '''

conn = cx_Oracle.connect("hi/0000@localhost:1521/xe")
cursor = conn.cursor()
data_list =[ [11, '2020/07/18'], [22, '2020/07/18']]
for data in data_list:
    cursor.execute('INSERT INTO news(seq, regdate) values (:0, :1)', (data[0],  datetime.strptime(data[1], '%Y/%m/%d') ))
conn.commit()



# cursor = conn.cursor()
# sql = "insert into my_table (my_column) values (:1)"
# my_row = ('some_string',)
# my_row_list = [my_row]
# cursor.executemany(sql, my_row_list)


# cursor = conn.cursor()
# row = (a,) + (b,)
# print(row)
# sql='insert into test(a,b) values (:1, :2)'
# cursor.execute(sql,row)

print("==done==")




#
#
#
# # data = [[2017,5],[2018,8],[2019,7]]
# data_list = []
# for idx in df.index:
#     item_list = []
#     item_list.append(df.loc[idx].values[0])
#     item_list.append(df.loc[idx].values[1])
#     data_list.append(item_list)
# #print(data_list)
