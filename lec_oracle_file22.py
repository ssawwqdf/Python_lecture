##############파이썬 차원에서 데이터 형 관리하기
## DB가 뭘로 바뀌어도 돌아가게 ANSI 문법으로 쓰자. to_num이런 거 빼자
##
## 데이터프레임 -> 배우면 표로 예쁘게 정리해준다.
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




def test_insert(list):
    conn = cx.connect("ai", "1111", "localhost:1521/XE")
    cur = conn.cursor()
    sql = """ INSERT INTO EMP2 VALUES
            (:1,:2,:3,:4,:5,:6,:7,:8);
            """
    cur.executemany(sql, list)
    cur.close()
    conn.commit()
    conn.close()

test_insert(list)

