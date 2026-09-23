import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import GridSearchCV
import numpy as np

# 1.0 获取数据集
data = pd.read_csv('./data/number.csv')
X = data.iloc[:, 1:] / 255
Y = data.iloc[:, 0]

# 1.1 划分数据集
x_train, x_test, y_train, y_test = train_test_split(X, Y, train_size=0.8, random_state=22, stratify=Y)

# 2 特征工程
# 2.1 归一化处理
# 一个像素点占8位,即0-255,所以最大值是255,最小值是0,所以可以除255进行归一化处理
x_test = x_test
x_train = x_train

# 3.网格搜索与交叉验证
estimator = KNeighborsClassifier()
param_grid = {'n_neighbors': [5, 7]}
cv = 5
estimator = GridSearchCV(estimator=estimator, param_grid=param_grid, cv=cv, n_jobs=-1)
estimator.fit(x_train, y_train)
print(f'测试集上表现最好的模型:{estimator.best_estimator_}')

# 4.测试模型(评价模型)
y_pred = estimator.predict(x_test)
print(f'模型在测试集上的表现:{estimator.score(x_test, y_test)}')

# 5.保存模型
import joblib
import matplotlib.pyplot as plt

joblib.dump(estimator, 'data/img.pth')

# 6. 模型上线测试
load_estimator = joblib.load('data/img.pth')
# 6.1加载图片文件
img_matrix = plt.imread('source/demo.png')
# 6.2 归一化处理
img_matrix = img_matrix.reshape(1, -1)
# 6.3预测数据
predict = load_estimator.predict(pd.DataFrame(img_matrix, columns=x_test.columns))
# 6.4 展示预测结果
print(predict)
