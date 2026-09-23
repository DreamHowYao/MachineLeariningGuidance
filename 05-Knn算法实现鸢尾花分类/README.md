# 鸢尾花（Iris）数据集

## 1. 数据集简介

**鸢尾花（Iris）数据集**是机器学习领域最经典的入门数据集之一,由统计学家 Ronald Fisher 在 1936 年引入。

该数据集包含了 **3 个品种** 的鸢尾花各 **50 个样本**,共计 **150 个样本**。每个样本有 **4 个特征**（花萼和花瓣的长度与宽度）,以及对应的品种标签。

### 三种鸢尾花品种：
- **Setosa**（山鸢尾）
- **Versicolor**（变色鸢尾）
- **Virginica**（维吉尼亚鸢尾）

### 四个特征（单位：厘米）：
- **Sepal Length**（花萼长度）
- **Sepal Width**（花萼宽度）
- **Petal Length**（花瓣长度）
- **Petal Width**（花瓣宽度）

---

## 2. 数据集加载（使用 scikit-learn）

```python
from sklearn.datasets import load_iris

iris = load_iris()
```

---

## 3. 常用属性

| 属性 | 说明 | 示例 |
|------|------|------|
| `iris.data` | 特征数据,形状为 (150, 4) 的二维数组 | `iris.data.shape` → (150, 4) |
| `iris.target` | 标签数据,0、1、2 分别代表三个品种 | `iris.target` → array([0,0,...,1,1,...,2,2,...]) |
| `iris.target_names` | 标签对应的品种名称 | `array(['setosa', 'versicolor', 'virginica'], dtype='<U10')` |
| `iris.feature_names` | 四个特征的名称列表 | `['sepal length (cm)', 'sepal width (cm)', ...]` |
| `iris.filename` | 数据文件路径（部分版本支持） | - |
| `iris.DESCR` | 数据集的完整描述文档 | `print(iris.DESCR)` |

---

## 4. 常用方法

| 方法 | 说明 | 示例 |
|------|------|------|
| `load_iris(return_X_y=True)` | 返回 (data, target) 元组 | `X, y = load_iris(return_X_y=True)` |
| `pd.DataFrame(iris.data, columns=iris.feature_names)` | 转为 Pandas DataFrame | 便于数据分析与可视化 |

---

## 5. 快速示例：查看数据

```python
from sklearn.datasets import load_iris
import pandas as pd

iris = load_iris()

# 查看特征名称和标签名称
print("特征名称:", iris.feature_names)
print("标签名称:", iris.target_names)

# 转为 DataFrame 查看前 5 行
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['species'] = iris.target
print(df.head())

# 查看数据统计描述
print(df.describe())

# 查看各类别样本数量
print(df['species'].value_counts())
```

---

## 6. 适用场景

该数据集常用于：
- 分类算法入门（KNN、决策树、逻辑回归、SVM 等）
- 数据可视化练习（散点图、配对图）
- 特征工程与降维（PCA）演示
- 聚类算法（K-Means）对比实验

---

## 7. 注意事项

- 该数据集**非常干净**,无缺失值,无需额外预处理（但标准化/归一化可用于某些算法）。
- 三个类别在特征空间中**线性可分程度不同**（Setosa 易分,Versicolor 和 Virginica 有一定重叠）。
