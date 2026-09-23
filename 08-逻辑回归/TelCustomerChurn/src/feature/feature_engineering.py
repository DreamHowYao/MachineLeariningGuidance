from pandas import DataFrame
import numpy as np
from sklearn.preprocessing import StandardScaler
import joblib
def feature_engineering(data: DataFrame, save_path:str,train:bool = True)-> DataFrame:
    # 1. 创建组合特征：费用 × 合同类型
    data['middle_charge_short_contract'] = (
            (data['MonthlyCharges'] > data['MonthlyCharges'].mean() - data['MonthlyCharges'].std()) &
            (data['Contract_Month-to-month'] == 1)
    ).astype(int)

    # 2. 创建互联网服务相关的组合特征
    data['weighted_services_log'] = (
        data['OnlineSecurity'] * 3 +
        data['TechSupport'] * 3 +
        data['OnlineBackup'] * 2 +
        data['DeviceProtection'] * 2 +
        data['StreamingTV'] * 1+
        data['StreamingMovies'] * 1
    ).astype(int)
    # 注入非线性特征
    data['weighted_services_log'] = np.log1p(data['weighted_services_log'])

    # # 3. 生命周期月均价值
    # data['avg_monthly_revenue'] = (
    #         data['TotalCharges'] /
    #         data['tenure'].replace(0, 1)
    # )
    # # 4. CLV (Customer Lifetime Value)
    # data['clv_basic'] = (
    #         data['MonthlyCharges'] * data['tenure']
    # )
    # 5. 对连续标签进行标准化处理
    target_columns = ['MonthlyCharges', 'TotalCharges']

    if train:
        std_scaler = StandardScaler()
        std_scaler.fit_transform(data[target_columns])
        joblib.dump(std_scaler, save_path)
    else:
        std_scaler = joblib.load(save_path)
        std_scaler.transform(data[target_columns])
    return data
