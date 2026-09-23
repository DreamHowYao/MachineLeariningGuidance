import pandas as pd

from src.data.dataset import ChurnDataset
from src.data.transform import transform_data
from src.trainer.train import *
from src.evaluate.eval import evaluate
from sklearn.model_selection import train_test_split

if __name__ == '__main__':
    config = Config(config_path='src/configs/base_config.yaml')

    dataset_path:str = config.data_root +  '/' + config.dataset
    dataset,features_name = transform_data(pd.read_csv(dataset_path))
    train_data, test_data = train_test_split(dataset, train_size=config.train_split)

    device = torch.device('cuda' if config.use_cuda else 'cpu')

    train_data = ChurnDataset(train_data, features_name,device)
    test_data = ChurnDataset(test_data, features_name,device)

    # lr_model = train(config,train_data)

    evaluate('src/save/save.pth', test_data)