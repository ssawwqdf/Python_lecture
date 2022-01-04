#-------------------220104---------------------------

import cx_Oracle as cx

# SQL 열어서 우선 해라!!-> 그러면 잘못 했을 때 롤백하기 편할듯

#=============================================
#                   insert
#=============================================
# 다음 두건의 데이터 동시 입력
# [1,'aa','111']
# [2,'bb','222']
# test_insert(list)

def test_insert(emp_list):
    conn = cx.connect("ai", "1111", "127.0.0.1:1521/XE")
    sql = """insert
            into test(seq, name, pw)
            values(:1, :2, :3) """
    cur=conn.cursor()
    cur.executemany(sql, emp_list)
    cur.close()
    conn.commit()
    conn.close()

insert_list=[ [1,'aa','111'],
              [2,'bb','222']
              ]
test_insert(insert_list)

#=============================================
#                   select
#=============================================
# aa 정보 출력 --> [1,'aa','111']
# test_select(name)

def test_select(name):
    conn = cx.connect("ai", "1111", "127.0.0.1:1521/XE")
    cur = conn.cursor()
    sql = f"select * from test where name='{name}' "
    cur.execute(sql)
    for c in cur:
        print(c)
    cur.close()
    conn.close()

# test_select('aa')

#=============================================
#                   update
#=============================================
# aa 비번 333로 변경
# bb 비번 444로 변경 --> [1,'aa','333']  [2,'bb','444']
# test_update()

## 리스트로 불러올 때 : 여러 개 불러오기.
def test_update(name,pw):
    conn = cx.connect("ai", "1111", "127.0.0.1:1521/XE")
    sql = f"""update test
            set pw= {pw}
            where name='{name}'
            """
    cur=conn.cursor()
    cur.execute(sql)
    cur.close()
    conn.commit()
    conn.close()

# test_update('aa',333)
# test_update('bb',333)

#=============================================
#                   delete
#=============================================
# --> aa만 삭제
# test_delete()

def test_delete(name):
    conn = cx.connect("ai", "1111", "127.0.0.1:1521/XE")
    sql = f"""delete from test
            where name = '{name}'
            """
    cur=conn.cursor()
    cur.execute(sql)
    cur.close()
    conn.commit()
    conn.close()

# test_delete('bb')