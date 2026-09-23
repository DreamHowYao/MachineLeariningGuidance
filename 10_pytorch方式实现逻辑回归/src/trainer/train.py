import torch
import torch.optim as optim
import torch.nn as nn
from torch.utils.data import DataLoader

from ..utils.config import Config
from ..models.base_model import LrModel

def train(config:Config,dataset):
    # gpu_ids: list[int] = config.gpu_ids
    # os.environ['CUDA_VISIBLE_DEVICES'] = ','.join(map(str, gpu_ids))

    device = torch.device('cuda' if config.use_cuda else 'cpu')

    lr_model = LrModel(input_dim=len(dataset.features_name) - 1, out_features=1).to(device)

    loss_fn = nn.BCEWithLogitsLoss()
    optimizer = optim.Adam(lr_model.parameters(),lr=0.01,betas=(0.9,0.999),eps=1e-08)

    dataloader = DataLoader(
        dataset, batch_size=config.batch_size,
        shuffle=config.shuffle
    )
    epochs = config.epochs
    for e in range(epochs):
        for _, (x,y) in enumerate(dataloader):

            output = lr_model(x)
            loss = loss_fn(output, y.reshape(-1,1))
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

    torch.save(lr_model.state_dict(), config.save_path +  '.pt')

    return lr_model