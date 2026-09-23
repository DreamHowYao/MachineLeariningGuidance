import torch
from sklearn.metrics import classification_report

from ..models.base_model import LrModel

def evaluate(save_path,data):
    model = LrModel(27,1).to('cuda')
    model.load_state_dict(torch.load(save_path))
    model.eval()

    all_preds = []
    all_labels = []
    with torch.no_grad():
        for x, y in data:
            output = model(x)  # 形状 (batch_size, num_classes)
            pred = int(output.item() > 0.5)  # 取最大概率的类别

            all_preds.extend([pred])
            all_labels.extend([int(y.item())])

    # 生成类别名称
    target_names = [f'类别{i}' for i in range(2)]

    print("\n" + "=" * 60)
    print("分类报告:")
    print("=" * 60)
    print(classification_report(all_labels, all_preds, target_names=target_names))
