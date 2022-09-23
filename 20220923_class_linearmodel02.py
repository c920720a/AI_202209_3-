# 선형회귀의 과적합으로 인해 개선을 시켜주는 필요성
# 라소(L1), 릿지(L2)
# 예측모델 = w1 * x1 + w2 * x2 .... + b
# 라소(L1) w1,w2.... 가중치를 0에 가깝게 만든다.
# 릿지(L2)  w1,w2.... 가중치를 0에 가깝게 만든다.
# 라소, 릿지의 차이점은
#  라소는 실제로 0을 만든다. - 변수가 선택
#  릿지는 실제로 0을 만들지는 않는다. - 모든 변수가 존재.
# 이를 통해서 과대적합이 어느정도 해소된다.

import mglearn
import numpy as np
from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler, PolynomialFeatures
from sklearn.linear_model import Lasso, Ridge
import pandas as pd

# 보스턴 데이터 셋을 불러오는 또다른 3가지 방법
# data_url = "http://lib.stat.cmu.edu/datasets/boston"
# raw_df = pd.read_csv(data_url, sep="\s+", skiprows=22, header=None)

# from sklearn.datasets import fetch_california_housing
# housing = fetch_california_housing()

# from sklearn.datasets import fetch_openml
# housing = fetch_openml(name="house_prices", as_frame=True)

# 한글
import matplotlib
from matplotlib import font_manager, rc
font_loc = "C:/Windows/Fonts/malgunbd.ttf"
font_name = font_manager.FontProperties(fname=font_loc).get_name()
matplotlib.rc('font', family=font_name)
matplotlib.rcParams['axes.unicode_minus'] = False

# %matplotlib inline

### 데이터 셋 준비
boston = load_boston()  # 데이터 셋 불러오기
print(type(boston.target), type(boston.data))
print(boston.target.shape, boston.data.shape)

df_boston = pd.DataFrame(boston.data, columns=boston.feature_names)
df_boston['target'] = pd.Series(boston.target)

pd.set_option('display.max_columns', None)
print( df_boston.head() )

# 사전준비
# 입력/출력
# 0~1사이로 만들기
# 변수 확장

# 입력/출력 선택
X = df_boston.loc[ :, 'CRIM':'LSTAT' ]
y = df_boston['target']

# 0~1사이로 만들기
nor_X = MinMaxScaler().fit_transform(X) # 정규화

# 변수 확장
ex_X = PolynomialFeatures(degree=2, include_bias=False).fit_transform(nor_X)

print("전의 상태 : ", X.shape, np.min(X), np.max(X))
print("적용된 상태 : ", ex_X.shape, np.min(ex_X), np.max(ex_X))



# 01. 선형회귀 모델을 만든다.
# 02. 라쏘회귀 모델을 만든다.
# 03. 릿지회귀 모델을 만든다.
# 04. 모델을 비교해본다.