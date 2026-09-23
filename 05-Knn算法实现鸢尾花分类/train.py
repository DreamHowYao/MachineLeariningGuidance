import matplotlib.pyplot as plt
import pandas as pd
from sklearn.datasets import load_iris
import seaborn
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# 2.加载数据
iris = load_iris()
# print("X:",iris.data)
# print("Y",iris.target)
# print(iris.feature_names)
# print(iris.target_names)

# 3.数据分析
iris_data = pd.DataFrame(iris.data, columns=iris.feature_names)
iris_data['label'] = iris.target
# print(iris_data)
seaborn.lmplot(x='sepal length (cm)', y='petal length (cm)', data=iris_data, hue='label', fit_reg=False)
plt.show()

# 4.划分数据集
X = iris.data
Y = iris.target
"""
train_test_split(
    *arrays:x和y数组,
    train_size:训练集比例,和test_size互补 ,
    test_size:训练集比例,
    random_state:随机数种子,方便复现,
    stratify: 分层抽样 ,一般传y,解决类别不均衡的场景 。也可以按照特征标签进行分层,如性别,年龄段,时间段... 不可以和shuffle一起用,
    shuffle: 是否随机抽样 
    )
"""
x_train, x_test, y_train, y_test = train_test_split(X, Y, train_size=0.9, random_state=22, stratify=Y)

# 5.特征工程
transformer = StandardScaler()
x_train = transformer.fit_transform(x_train)
# 测试集不要再fit了
x_test = transformer.transform(x_test)

# 6.1 训练模型
estimator = KNeighborsClassifier(n_neighbors=5)
estimator.fit(x_train, y_train)

# 6.2 使用模型预测数据
y_pred = estimator.predict(x_test)
print(f'真实结果:{y_test}\r\n 预测结果:{y_pred}')

# 7.评价模型
print(f'模型准确率:{estimator.score(x_test, y_test)}')
print(f'准确率:{accuracy_score(y_test, y_pred)}')