from pkg import lec10_module_oracle as lec

# lec.my_select()
# lec.my_select('KING')


# 한 줄 실행하고 열어둔 채로 다른 줄 실행하면 중복 때문에 에러 난다.
# 연습할 때는 인서트 한 번 하고 나면 주석 처리해서 닫아라.

# lec.my_insert('9999','aaa',40)
# lec.my_insert2('8888','bbb',30)

# my_insert_many
# emp_list = [[551,'ccc1',10],
#              [552,'ccc2',10],
#              [553,'ccc3',10],
#              [554,'ccc4',10],
#              [555,'ccc5',10]]
# lec.my_insert_many(emp_list)

# lec.my_insert3('7777','ddd',20)

# lec.my_insert3('7778','dde', 20)
#
# lec.my_update(40, 7369)

# list=[[40,7369], [40, 7499]] # many 쓸 거면 [[]]로 써야 됨.
# lec.my_update2(list)

# list=[30,7369] # 비추 문법!!!!!!!
# lec.my_update3(list)

# lec.my_delete(10)

# del_list=[7698, 7499, 7844]
# lec.my_delete2(del_list)

#executemany 하는 경우
# del_list=[[7698], [7499], [7844]]
# lec.my_delete5del_list)