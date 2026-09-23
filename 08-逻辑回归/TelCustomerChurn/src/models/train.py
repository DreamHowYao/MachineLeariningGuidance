import joblib
import pandas as pd
import matplotlib.pyplot as plt
import os
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, confusion_matrix, roc_curve, roc_auc_score,classification_report
from sklearn.model_selection import train_test_split, GridSearchCV

from ..preparation.data_preparation import data_preprocessing
from ..feature.feature_engineering import feature_engineering
SEED = 22


def get_est(x_train,y_train):
    estimator = LogisticRegression(max_iter=2000,penalty='none')

    parma_grid = {"max_iter": [50,100,300,500],
                  "solver": ['lbfgs','newton-cg']}
    # cv = 5
    # estimator = GridSearchCV(estimator=estimator, param_grid=parma_grid, cv=cv)
    estimator.fit(x_train, y_train)
    # print(f'最好的参数:{estimator.best_params_}')
    return estimator

def train(dataset_path: str, save_dir: str):
    data = pd.read_csv(os.path.join(dataset_path))

    # 1. 数据预处理
    data = data_preprocessing(data)

    # 2. 划分数据集
    X = data.iloc[: , :-1]
    Y = data.iloc[: , -1]
    Y.info()
    x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.3, random_state=SEED)


    # 3. 特征工程
    save_path = save_dir + 'std_scaler.pkl'
    x_train = feature_engineering(x_train,save_path,train=True)
    x_test = feature_engineering(x_test,save_path,train=False)

    lr_estimator = get_est(x_train,y_train)
    print("classes:", lr_estimator.classes_)
    # 5. 测试模型
    y_pred = lr_estimator.predict(x_test)
    y_pred_proba = lr_estimator.predict_proba(x_test)
    # 6.评价模型
    print(f'模型在测试集上的准确率:{accuracy_score(y_test, y_pred)}')
    print(f'模型在测试集上的精确率:{precision_score(y_test, y_pred)}')
    print(f'模型在测试集上的召回率:{recall_score(y_test, y_pred)}')

    print(f'混淆矩阵:\r\n{confusion_matrix(y_test, y_pred)}')
    fpr, tpr, thresholds = roc_curve(y_test, y_pred_proba[:, 1])
    plt.plot(fpr, tpr)
    plt.show()
    ROC_AUC_SCORE = roc_auc_score(y_test, y_pred_proba[:, 1])
    print(f'ROC_AUC_SCORE:{ROC_AUC_SCORE}')

    report = classification_report(y_test, y_pred)
    print(report)
    # 4.2 保存模型
    joblib.dump(lr_estimator, save_dir + '/lr_est.pth')




