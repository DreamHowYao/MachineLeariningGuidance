
from src.models.train import train
## for feature exploration
from src.preparation.data_preparation import  save_conver


if __name__ == '__main__':
    DIR_PATH = 'dataset/Churn.csv'
    SAVE_DIR = 'save/'

    # save_conver(DIR_PATH)
    train(DIR_PATH,SAVE_DIR)

