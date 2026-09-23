# Telco Customer Churn Dataset

## 概述

本数据集包含一家电信公司的客户信息，用于分析和预测客户流失（Churn）情况。数据集共包含 **7,043** 条客户记录，涵盖 **21** 个特征字段，可用于构建客户流失预测模型、进行客户行为分析和制定客户保留策略。

## 数据集描述

### 基本信息

- **记录数量**：7,043 条
- **特征数量**：21 个
- **数据格式**：CSV
- **目标变量**：Churn（客户是否流失）

### 变量说明

| 序号 | 字段名              | 数据类型    | 描述                                                            |
|----|------------------|---------|---------------------------------------------------------------|
| 0  | customerID       | str     | 客户唯一标识符                                                       |
| 1  | gender           | str     | 客户性别（Male/Female）                                             |
| 2  | SeniorCitizen    | int64   | 是否为老年客户（1=是，0=否）                                              |
| 3  | Partner          | str     | 是否有伴侣（Yes/No）                                                 |
| 4  | Dependents       | str     | 是否有家属（Yes/No）                                                 |
| 5  | tenure           | int64   | 客户在网时长（月）                                                     |
| 6  | PhoneService     | str     | 是否开通电话服务（Yes/No）                                              |
| 7  | MultipleLines    | str     | 是否有多条电话线路（Yes/No/No phone service）                            |
| 8  | InternetService  | str     | 互联网服务类型（DSL/Fiber optic/No）                                   |
| 9  | OnlineSecurity   | str     | 是否开通在线安全服务（Yes/No/No internet service）                        |
| 10 | OnlineBackup     | str     | 是否开通在线备份服务（Yes/No/No internet service）                        |
| 11 | DeviceProtection | str     | 是否开通设备保护服务（Yes/No/No internet service）                        |
| 12 | TechSupport      | str     | 是否开通技术支持服务（Yes/No/No internet service）                        |
| 13 | StreamingTV      | str     | 是否开通电视流媒体服务（Yes/No/No internet service）                       |
| 14 | StreamingMovies  | str     | 是否开通电影流媒体服务（Yes/No/No internet service）                       |
| 15 | Contract         | str     | 合同类型（Month-to-month/One year/Two year）                        |
| 16 | PaperlessBilling | str     | 是否使用电子账单（Yes/No）                                              |
| 17 | PaymentMethod    | str     | 支付方式（Electronic check/Mailed check/Bank transfer/Credit card） |
| 18 | MonthlyCharges   | float64 | 月均费用（美元）                                                      |
| 19 | TotalCharges     | str     | 总费用（美元）                                                       |
| 20 | Churn            | str     | 是否流失（Yes/No）                                                  |







## 引用说明
