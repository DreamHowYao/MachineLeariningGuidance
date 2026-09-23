import pandas as pd
import numpy as np
from os import path
from pandas import DataFrame

"""
## 数据预处理建议

在使用本数据集进行分析或建模前，建议进行以下预处理步骤：

1. **数据类型转换**：
   - 将 `TotalCharges` 从字符串类型转换为数值类型（注意处理空值或特殊字符）

2. **分类变量编码**：
   - 对二元分类变量（Yes/No）进行标签编码
   - 对多分类变量进行 One-Hot 编码或标签编码

3. **特征工程**：
   - 可考虑创建衍生特征，如平均月费、客户生命周期价值等

4. **数据平衡**：
   - 检查 Churn 变量的类别分布，若存在不平衡可考虑过采样或欠采样

5. **特征缩放**：
   - 对数值型特征（tenure, MonthlyCharges, TotalCharges）进行标准化或归一化



"""

def data_preprocessing(data: DataFrame)-> pd.DataFrame:
    """

    :param data: DataFrame data including X and Y
    :return: preprocessed data
    """
    dataset = data.copy()

    # 2. 处理 多个值为 Yes or No的列
    col2conver = ['Churn', 'Partner', 'Dependents', 'PhoneService', 'PaperlessBilling']
    dataset[col2conver] = dataset[col2conver].replace({'Yes': 1, 'No': 0}).astype(int)


    # 3. 对部分特征进行 one hot 编码
    col2one_hot = ['InternetService','Contract','PaperlessBilling','PaymentMethod']
    dataset = pd.get_dummies(dataset,columns=col2one_hot,dtype='uint8')

    # 4.类型转换和缺失值处理
    dataset['TotalCharges'] = pd.to_numeric(dataset['TotalCharges'], errors='coerce')
    dataset['TotalCharges'] = dataset['TotalCharges'].fillna(dataset['TotalCharges'].mean())
    # 5. 处理 <电话服务> 相关的特征

    dataset['PhoneServiceAtt'] = dataset['MultipleLines'].replace({'Yes': 2, 'No' : 1,'No phone service': 0})

    # 7. 处理 <互联网服务> 相关的特征
    Internet_col = ['OnlineSecurity','OnlineBackup','DeviceProtection','TechSupport','StreamingTV','StreamingMovies']
    dataset[Internet_col] = dataset[Internet_col].replace({'Yes': 2, 'No' : 1,'No internet service': 0})

    dataset.drop(['gender','PhoneService','MultipleLines','customerID',], axis=1, inplace=True)

    # 确保标签列在最后
    churn = dataset.pop('Churn')
    dataset['Churn'] = churn

    return dataset

def save_conver(file_path:str):
    data_preprocessing(pd.read_csv(file_path)).to_csv(file_path.replace('Churn.csv','churn_conver.csv'),index=False)
