## 1. Module类介绍

`Module`类是`pytorch`框架提供开发者的所有神经网络模块的基类。其基本用法的示例如下:

```python
# 1. 导包
import torch.nn as nn

# 2. 搭建你的网络,并继承自`nn.Module`
class Model(nn.Module):
        # init 方法用于声明并初始化你的网络中的模块以及它们的参数
        def __init__(self):
            # 继承父类的构造方法，这样pytorch框架就可以管理你的网络
            super().__init__()
            # 这里我定义了一个 `3 * 1`的权重矩阵$W_{in_features *  out_features}$和一个一维张量$b_{1* out_features}$,对于这个模块而言,其转换是线性的
            self.linear = nn.Linear(in_features=3,out_features=1)
            
            # 这里我对权重矩阵的参数进行了0-1均匀初始化
            nn.init.uniform_(self.linear.weight)
        # forward 方法负责网络的运算,你可以按照你的想法对网络的运算进行封装
        def forward(self, x):
            output = self.linear(x) # x @ W.T + bias= output
```
### 2. `nn.Module`的核心作用
当你的网络类继承`nn.Module`,并使用`super().__init__()`初始化之后,你的模型将被`pytorch`注册并管理。
简单来说，它具备以下功能:
#### 2.1 自动管理"隐藏层"和模型参数

当你初始化你的模型后,`pytorch`会自动把它们注册成模型参数,你可以通过父类的`__str__`来查看你的网络结构,也可以通过`model.parameters()`查看你的模型参数.
例如在上面的例子中
```python
model = Model()
print(f'Model():{model}')
print('model.parameters():\t')
    for p in model.parameters():
        print(f'{p}, shape: {p.shape}')
"""
## 声明,网络是根据自顶向下的机制对模块进行注册的
Model():Model(
  (linear): Linear(in_features=3, out_features=1, bias=True)
)

model.parameters():
    Parameter containing:
        tensor([[0.9323, 0.3723, 0.5625]], requires_grad=True), shape: torch.Size([1, 3])
    Parameter containing:
        tensor([0.0301], requires_grad=True), shape: torch.Size([1])
"""
```
> `model.parameters()`通过你定义的顺序递归访问模型参数并返回
> 网络的注册机制可以参考末尾文章[]

#### 2.2 帮助开发者管理网络的运算单元(GPU/CPU)
你可以直接将你整个模型迁移到GPU设备上,而不需要挨个注册。就像这样
```python
model = Model()

model.to("cuda")
```
#### 2.3 提供训练/推理模式切换
你可以通过`model.train()`和`model.eval()`来开启模型的训练/推理模式。
比较典型的应用是 你在模型的前向传播当中定义了 `dorpout`正则化。这时候你可以通过切换模型的训练和推理模式开启/关闭它。
另一个比较典型的例子是 你在网络中`BatchNorm`层归一化，同样的你可以通过切换模型的训练和推理模式开启/关闭它。

#### 2.4 提供模型参数存储和加载功能
1. `state_dict()` (存储)
   - 作用:返回`OrderedDict`类型的权重字典，将每一层可学习的参数（weight、bias）和缓冲区（running_mean 等）映射到对应的张量。
   - 特点：只存张量的数值，不存网络的结构信息（如层数、激活函数类型）。
```python
torch.save(model.state_dict(), 'model_weights.pth')
## 你可以通过下面的代码把模型结构也存储起来,但实际不推荐这么做.
# torch.save(model, 'model.pth')
# (因为torch.save()底层是通过pickle序列化实现的,如果反序列化时出现属性等层面维度不匹配会出现报错)
# 一般我们使用save函数来保存优化器，调度器等复杂状态的对象.比如
"""

optimizer = torch.optim.Adam(model.parameters(), lr=0.001)

# 保存检查点
torch.save({
    'epoch': epoch,
    'model_state_dict': model.state_dict(),
    'optimizer_state_dict': optimizer.state_dict(),
    'loss': loss,
    # 还可以加其他信息
    'scheduler_state_dict': scheduler.state_dict(),  # 如果有学习率调度器
}, 'checkpoint.pth')
"""
```
2. `load_state_dict()` (加载)
   - 作用: 将保存的字典参数，赋值到当前模型的参数中。
   - 特点:加载时必须有一个已经定义好结构的模型实例，且字典的键（Key）必须完全匹配(你可以根据`strict`参数控制键名匹配的严格程度)。
   > strict=False时允许部分匹配(只加载相同的键，忽略多余的或缺失的键)。
```python
# 加载预训练模型，但忽略最后不匹配的分类层
model = Model()  # 最后几层改了结构
pretrained_dict = torch.load('pretrained.pth')
model.load_state_dict(pretrained_dict, strict=False)  # 自动忽略不匹配的层
```
##### 参考
- [Pytorch官方文档](https://docs.pytorch.ac.cn/docs/2.13/generated/torch.nn.Module.html)
- [PyTorch 源码解读之 nn.Module：核心网络模块接口详解](https://zhuanlan.zhihu.com/p/340453841)
- [Pytorch的hook机制](https://www.cnblogs.com/shiyublog/p/11207582.html)