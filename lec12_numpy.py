
##############################################################주피터로 옮김
# numpy
import numpy as np # 100% np로 alias 준다.
# arr= np.array( [1,2,3]) # np.array( ) 캐스팅해준다.
# print(arr, type(arr)) # 타입: numpy.ndarray : numpy의 numpy data의 array 타입이다.
#
# # pandas
# import pandas as pd # 99.9999% pd로 alias 준다.
#                     # ctrl+pandas클릭하면 __init__열린다.
#                     # pickle도 가능하게 해준다.(피클처럼 데이터 함부로 못 건들게 진공포장 시켜준다.) / read stata도 있네 하하
#                     # pandas.py (모듈)

# df=pd.DataFrame() # 생성자 만들어줘야됨. DataFrame은 클래스 부모의부모의부모의부모 정도가 넘피
                    # __init__.py가  들어가는 영역이 생긴다.
# 생성자 변수로 주로 들어가는 애들
# data=None,
# index: Axes | None = None,
# columns: Axes | None = None,
# dtype: Dtype | None = None,
# ....

#
# df=pd.DataFrame( data=[ [1,'kim',111],[2,'lee',222]] ,
#                  columns=['seq','id','pw'],
#                  # index= [11 22] 인덱스 어떻게 줄 건지 쓰는 것. 데이터 개수만큼 필요.(많으면 다 부여하기 어려워서 사실 그냥 안 쓴다.) 0번째부터 시작.
#                  # dtype= 안 쓰면 기본타입 들어감.
#                  )
# print(df.info())

####################################################### 위로 주피터로 옮기기 완료
# df.todict
#
# df.to_dict()

np.isnan