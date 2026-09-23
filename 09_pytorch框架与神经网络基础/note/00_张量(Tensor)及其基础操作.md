# 张量(Tensor)的基本概念
张量是一个通用的多维数组,可以表示标量（0 维）、向量（1 维）、矩阵（2 维）以及更高维度的数据。张量是 PyTorch 中的核心数据结构,用于表示和操作数据。
> - 0维张量：标量(scalar)
> - 1维张量：向量(vector)
> - 2维张量：矩阵(matrix)
> - 3维张量: 矩阵的堆叠(像是一个立方体或叠起来的表格)。如一张彩色的RGB图片,可以用(颜色通道{Channel},高度{Height},宽度{Weight})来表示。
> - 高维张量: 比它低一维张量的堆叠。如一段视频就是一个四维张量(时间,颜色通道,高度,宽度),本质上是各个时间(帧)上图片的堆叠。

## 1.张量的创建



### 1.1 torch.tensor()

- 用途: 从已有数据（列表、元组、NumPy数组等，也可是空白数据）创建张量
- 特点: 一个工厂函数,每次调用都会创建新的 Tensor 对象,并且会根据原始数据**自动推断数据类型**
> 最终返回`Tensor `对象

```python
import numpy as np
import torch
# 1.根据指定数据创建张量 - torch.tensor
print('tensor 方式创建张量')

# 1.1 创建张量标量
data = torch.tensor(10)
print(f'张量标量:{data}')

# 1.2 根据 numpy数组 创建张量
data = np.random.randn(3, 2)
data = torch.tensor(data)
print(f'根据numpy数组创建张量:\r\n{data}')

# 1.3 根据 列表 创建张量
data = [[1, 0, 0], [0, 1, 0]]
data = torch.tensor(data)
print(f'根据列表创建张量:\r\n{data}')
```


### 1.2 torch.Tensor()
- 用途: 根据形状创建张量, 其也可用来创建指定数据的张量
- 特点: Python端张量的基类，其初始化方式由C实现。**使用这种初始化方式只能被初始化为<torch.float>类型的张量**

```python
import numpy as np
import torch

# 2. 根据形状创建张量 - torch.Tensor
print('Tensor 方式创建张量')
#   2.1 创建 2 行 3 列的张量 默认的dtype为 float32
data = torch.Tensor(2, 3)
print(data)

#   2.2 注意!! 如果 传递列表, 则创建包含指定元素的张量
data = torch.Tensor([10])
print(data)
```


### 1.3 torch.(Type)Tensor
 - 用途: 创建指定类型的张量
 - 特点: torch.Tensor的子类

```python
import numpy as np
import torch

# 3.创建指定类型的张量 - torch.IntTensor、torch.FloatTensor、torch.DoubleTensor
print('创建指定类型的张量-> torch.IntTensor、torch.FloatTensor、torch.DoubleTensor')
#   3.1 创建 2 行 3 列,dtype为 int32 的张量
data = torch.IntTensor(2, 3)
print(data)

#   3.2 注意!! 如果传递的类型不正确,则会进行类型转换
data = torch.IntTensor([2.5, 3.3])
print(data)
"""
其他的一些类型
class DoubleTensor(Tensor): ...
class FloatTensor(Tensor): ...
class BFloat16Tensor(Tensor): ...
class LongTensor(Tensor): ...
class IntTensor(Tensor): ...
class ShortTensor(Tensor): ...
class HalfTensor(Tensor): ...
class CharTensor(Tensor): ...
class ByteTensor(Tensor): ...
class BoolTensor(Tensor): ...
"""
  ```

#### 小结

**小写 t: 根据指定数据创建**
**大写 T: 既可以根据指定数据创建,也可以根据形状创建**

> Tensor: 不指定类型

> (Type)Tensor: 指定类型

> 推荐使用torch.tensor()来初始化张量对象，是官方推荐的做法，并且tensor方法的参数列表比类初始化的参数列表要多

---

### 1.4 创建线性张量

- torch.arange() 和 torch.linspace() 创建线性张量

```python
import torch
# 1. 创建线性张量
print('=' * 50 + '创建线性张量' + '=' * 50)
#   1.1 在指定区间内按照步长生成元素
data = torch.arange(0, 10, 2)
print(data)

#   1.2 在指定区间按照元素个数生成
data = torch.linspace(0, 10, 9)
print(data)
  ```
```

### 1.5 创建随机张量

- torch.random.init_seed() 和 torch.random.manual_seed() 随机种子设置

- torch.randn() 创建随机张量

```python
import torch
# 2.创建随机张量
print('=' * 50 + '创建随机张量' + '=' * 50)
#   2.1 创建一个 2 行 3列的随机张量
data = torch.randn(2, 3)
print(data)

#   2.2 设置随机数种子
#   - torch.random.init_seed
print(f'随机数种子: {torch.random.initial_seed()}')  # 25338627685600
#   - torch.random.manual_seed
torch.random.manual_seed(200)
data = torch.randn(2, 3)
print(data)
print(f'随机数种子: {torch.random.initial_seed()}')  # 100
```

### 1.6 创建0-1张量

- torch.ones 和 torch.ones_like 创建全1张量
- torch.zeros 和 torch.zeros_like 创建全0张量
- torch.full 和 torch.full_like 创建全为指定值张量

```python
import torch

# - torch.ones 和 torch.ones_like 创建全1张量
data = torch.ones(2, 3)
print(f'data:\r\n{data}')
data1 = torch.ones_like(data)
print(f'data1:\r\n{data1}')

# - torch.zeros 和 torch.zeros_like 创建全0张量
data = torch.zeros(2, 3)
print(f'data:\r\n{data}')
data1 = torch.zeros_like(data)
print(f'data1:\r\n{data1}')

# - torch.full 和 torch.full_like 创建全为指定值张量
data = torch.full([2, 3], 10, dtype=torch.float32)
print(f'data:\r\n{data}')
data1 = torch.full_like(data, 20)
print(f'data1:\r\n{data1}')
print(f'data1.dtype:{data1.dtype}')  # float32
```

## 2.张量的类型转换

#### 	张量的元素类型转换

- `data.type(torch.DoubleTensor)`
- `data.double()`

```python
import torch
# 1. data.type(torch.类型)
print('===============data.type(torch.类型)================')
data = torch.full([2, 3], 10)
print(data.dtype)

data = data.type(torch.DoubleTensor)
print(data.dtype)

# data = data.type(torch.IntTensor)
# print(data.dtype)
# data = data.type(torch.LongTensor)
# print(data.dtype)

# 2. data.double()
print('===============data.double()=================')
data = torch.full([2, 3], 20)
print(data.dtype)

data = data.double()
print(data.dtype)

# data = data.int()
# print(data.dtype)
```

### 	张量的类型转换

1. 张量转换为`Numpy`数组的方法

- 使用 `Tensor.numpy `函数可以将张量转换为 `ndarray `数组，但是共享内存，可以使用 copy 函数避免共享。

```python
import torch
import numpy as np

# 1. 张量转换为Numpy数组的方法
# - 使用 Tensor.numpy 函数可以将张量转换为 ndarray 数组，但是共享内存，可以使用 copy 函数避免共享.
print('=' * 30 + '使用 Tensor.numpy但不进行copy' + '=' * 30)
data_tensor = torch.tensor([2, 3, 4])
data_numpy = data_tensor.numpy()
print(type(data_tensor))
print(type(data_numpy))

data_numpy[0] = 100
print(data_tensor)
print(f'ndarray:{data_numpy}')

print('=' * 30 + '使用 Tensor.numpy并进行copy' + '=' * 30)
data_tensor = torch.tensor([2, 3, 4])
data_numpy = data_tensor.numpy().copy()
print(type(data_tensor))
print(type(data_numpy))

data_numpy[0] = 100
print(data_tensor)
print(f'ndarray:{data_numpy}')
```

2. `Numpy`数组转换为张量的方法
   - 使用 `from_numpy `可以将 `ndarray `数组转换为` Tensor`，默认共享内存，使用 `copy `函数避免共享。
   - 使用 `torch.tensor` 可以将 `ndarray `数组转换为 `Tensor`，默认不共享内存。
  
```python
import torch
import numpy as np

# 2. Numpy数组转换为张量的方法
"""
将numpy数组转换为张量
   2.1 from_numpy 默认共享内存，使用 copy 函数避免共享。
   2.2 torch.tensor(ndarray) 默认不共享内存。
"""
# - 2.1 使用 from_numpy:会共享内存，可以使用 copy 函数避免共享。
print('=' * 30 + '使用from_numpy但不进行copy' + '=' * 30)
data_numpy = np.array([2, 3, 4])
data_tensor = torch.from_numpy(data_numpy)
data_tensor[0] = 100
print(data_tensor)
print(f'ndarray:{data_numpy}')

print('=' * 30 + '使用from_numpy且进行copy' + '=' * 30)
data_numpy = np.array([2, 3, 4])
data_tensor = torch.from_numpy(data_numpy.copy())
data_tensor[0] = 100
print(data_tensor)
print(f'ndarray:{data_numpy}')

# - 2.2 使用 torch.tensor(ndarray) 默认不共享内存。
data_numpy = np.array([2, 3, 4])
data_tensor = torch.tensor(data_numpy)

data_tensor[0] = 100
print(data_tensor)
print(f'ndarray:{data_numpy}')
```
    
3. 标量张量和数字转换方法
- 对于**只有一个元素**的张量，使用item()函数将该值从张量中提取出来
    > 官方文档解释: Returns the value of this tensor as a standard Python number.
    > This only works for tensors with one element.

```python
import torch
import numpy as np

# 3. 标量张量和数字转换方法
# - 对于只有一个元素的张量，使用item()函数将该值从张量中提取出来
data_tensor = torch.tensor([30, ])
print(data_tensor.item())

data_tensor = torch.tensor(30)
print(data_tensor.item())
```

## 3.张量数值计算

1. 张量基本运算
   - 不修改原数据
       - add、sub、mul、div、neg
   - 修改源数据
       - add_、sub_、mul_、div_、neg_（带下划线的版本会修改原数据）
    
```python
import torch
import numpy as np

# 1.张量基本运算
print('=' * 30 + '基本运算' + '=' * 30)
data = torch.randint(0, 10, [2, 3])
print(f'原数据data:\r\n{data}')

#   1.1 不修改原数据
print('=' * 10 + 'add' + '=' * 10)
new_data = data.add(10)
print(f'new_data:\r\n{new_data}')
print(f'data:\r\n{data}')

#   1.2 直接修改原数据
print('=' * 10 + 'add_' + '=' * 10)
data.add_(10)
print(f'data:\r\n{data}')

# print(data.sub(10))
# print(data.mul(10))
# print(data.div(10))
# print(data.neg())
```
    
    
2. 张量点乘运算
   - 点乘指（Hadamard积）的是两个 同维[同型]矩阵  对应位置的元素相乘，使用mul 和运算符 * 实现。
    
```python
import torch
import numpy as np
  
# 2. 张量点乘运算
print('=' * 30 + '张量点乘运算' + '=' * 30)
A = torch.tensor([[1, 2], [3, 4]])
B = torch.tensor([[5, 6], [7, 8]])
  
# - 2.1 使用 mul(A,B)
print('=' * 10 + 'mul 点乘' + '=' * 10)
res = torch.mul(A, B)
print(f'点乘后的结果:{res}')
  
# - 2.2 使用 * 运算符
print('=' * 10 + '* 点乘' + '=' * 10)
res = A * B
print(f'点乘后的结果:{res}')
```
    
3. 张量矩阵乘法运算
    - 矩阵乘法运算要求第一个矩阵 shape: (n, m)，第二个矩阵 shape: (m, p), 两个矩阵点积运算 shape 为: (n, p)。
        1. 运算符 @ 用于进行两个矩阵的乘积运算
        2. torch.matmul 对进行乘积运算的两矩阵形状没有限定.对数输入的 shape 不同的张量, 对应的**最后几个维度必须符合矩阵运算规则**

```python
import torch
import numpy as np

# 3. 张量矩阵乘法运算
print('=' * 30 + '张量矩阵乘法运算' + '=' * 30)
A = torch.tensor([[1, 2], [3, 4], [5, 6]])
B = torch.tensor([[5, 6], [7, 8]])

#   3.1 使用 matmul(A,B)
# - torch.matmul 对进行乘积运算的两矩阵形状没有限定.对数输入的 shape 不同的张量, 对应的最后几个维度必须符合矩阵运算规则
print(f'matmul(A,B) ={torch.matmul(A, B)}')

#   3.2 使用@ 运算符
print(f'A @ B = {A @ B}')
```

## 4.张量运算函数

```python
import torch
import numpy as np
"""
- 均值
- 平方根
- 求和
- 指数计算
- 对数计算
.......
"""
import torch

data = torch.randint(0, 10, [2, 3], dtype=torch.float64)
print(data)

# 1.均值
# 注意!! tensor必须为 float 或者 Double类型
print('=' * 10 + 'mean' + '=' * 10)
print(data.mean())
print(data.mean(dim=0))  # 按列求均值
print(data.mean(dim=1))  # 按行求均值

# 2.求和
print('=' * 10 + 'sum' + '=' * 10)
print(data.sum())
print(data.sum(dim=0))
print(data.sum(dim=1))

# 3.计算平方
print('=' * 10 + 'pow' + '=' * 10)
print(torch.pow(data, 2))
print(data.pow(2))

# 4.计算平方根
print('=' * 10 + 'sqrt' + '=' * 10)
print(data.sqrt())
print(torch.sqrt(data))

# 5.指数计算 e^n 次方
print('=' * 10 + 'exp' + '=' * 10)
print(data.exp())
print(torch.exp(data))

# 6.对数计算 :以 e 为底数
print('=' * 10 + 'log' + '=' * 10)
print(data.log())
print(torch.log(data))
print(data.log2())
print(data.log10())
```

## 5.张量索引操作

1. 简单行列索引的使用
```properties
格式:data[row,col]
```
    
```python
import torch
import numpy as np
data = torch.randint(0, 10, [4, 5])
print('data->\r\n', data)

# 1. 简单行列索引的使用
print('=' * 20, '简单行列索引', '=' * 20)
print(f'data[0, 0] -> {data[0, 0]}')
print(f'data[:,0] -> {data[:, 0]}')
```

2. 列表索引的使用
```properties
格式:
    rows = [a,b,...]
    cols = [c,d...]
   访问:data[rows,cols]
含义:访问 [a,c] | [b,d]....的值
```
    
    
```python
import torch
data = torch.randint(0, 10, [4, 5])
print('data->\r\n', data)


# 2. 列表索引的使用
print('=' * 20, '列表索引', '=' * 20)
#   2.1 返回 (0, 2)、(1, 3) 两个位置的元素
rows = [0, 1]
cols = [2, 3]
print(f'data[rows,cols] ->', data[rows, cols])
#   2.2 返回行索引为 0 的第 1、2、3 列的值
print(f'data[[0],[1,2]] ->', data[[0], [1, 2]])

#   2.3 range()方式访问元素:返回 (0, 1) 和 (1, 2) 两个位置的元素
print(f'data[rows,cols] ->', data[range(2), range(1, 3)])

#   2.4 返回行索引为 0 和 1 的第 1、2、3 列的值
print(f'data[[[0], [1]], [1, 2, 3]] ->', data[[[0], [1]], [1, 2, 3]])

#   2.5 返回行索引为 0、1、2 的第 0、1、2 列的值 和 行索引为 1、2、3 的第 1、2、3 列的值
print(f'data[[[0, 1, 2], [1, 2, 3]], [[0, 1, 2], [1, 2, 3]]] ->', data[[[0, 1, 2], [1, 2, 3]], [[0, 1, 2], [1, 2, 3]]])

# print('data[[[0],[1,2,3]], [0,1,2]] ->',{data[0, 0]}) # 报错, 因为索引的维度不匹配
```
    
3. 范围索引的使用
   
    - 和`Numpy`大致相同,但不 支持反向索引
    
```python
data = torch.randint(0, 10, [4, 5])
print('data->\r\n', data)

# 3. 范围索引的使用
print('=' * 20, '范围索引', '=' * 20)
# 3.1   获取前三行前两列元素的值
print('data[:3,:2]->', data[:3, :2])

# 3.2   获取后两行后两列元素的值
print('data[-2:,-2:]->', data[-2:, -2:])

# print('data[3:1:-1,-2:]->', data[3:1:-1, -2:]) # 报错,tensor不支持反向切片
```
    
    
    
4. 布尔索引的使用

    - 和`Numpy`,`Pandas`大致相同

```python
# 4. 布尔索引的使用
print('=' * 20, '布尔索引', '=' * 20)
#   4.0 理解布尔索引的原理
bool_index = [True, False, False, True, False]
"""
注意它取元素时的方式!!!!
    第一行中满足布尔索引的拿出来,当作一行
    第二行中满足布尔索引的拿出来,当作一行
    以此类推
"""
print('data[:,bool_index] ->\r\n', data[:, bool_index])

#   4.1 获取第三行大于 5的元素
print(data[data[:, 2] > 5])

#   4.2 获取第二行大于 5的 列
print('data[:,data[1]>5] ->\r\n', data[:, data[1] > 5])
```

    

5. 多维索引的使用

    - 和`Numpy`,`Pandas`大致相同

```python
data = torch.randint(0, 10, [4, 5])
print('data->\r\n', data)

# 5. 多维索引的使用
print('=' * 20, '多维索引', '=' * 20)
data = torch.randint(0, 10, [3, 4, 5])
print('data->\r\n', data)
#   5.1 获取第一维元素
print(data[0, :, :])
#   5.2 获取第二维元素
print(data[:, 0, :])
#   5.3 获取第三维元素 # 注意它取元素的方式!!!
print(data[:, :, 0])
```

## 6.张量形状操作

1. 形状信息获取
    - 使用 shape 属性或者 size 方法都可以获得张量的形状

```python
data = torch.tensor([[10, 20, 30], [40, 50, 60]])

# 1. 使用 shape 属性或者 size 方法都可以获得张量的形状
print('使用 shape 属性或者 size 方法都可以获得张量的形状')
print(data.shape, data.shape[0], data.shape[1])
print(data.size(), data.size(0), data.size(1))
print()
```

2. reshape方式修改形状
	- reshape 函数可以在保证张量数据不变的前提下改变数据的维度，将其转换成指定的形状
    > 转换顺序:左右上下

```python
data = torch.tensor([[10, 20, 30], [40, 50, 60]])

# 2. 使用 reshape() 修改张量的形状
print('使用 reshape() 修改张量的形状')
reshape_data = data.reshape(1, data.shape[0] * data.shape[1])
print(f'reshape_data:{reshape_data}')
print(f'reshape_data:{data.reshape(1, -1)}')
print()
```

3. 升维与降维
    - squeeze() 删除形状为 1 的维度（降维）
    - unsqueeze() 添加形状为1的维度（升维）
    > 例如 unsqueeze(dim=i):在索引为i的位置添加一个形状为1的维度
    
```python
data = torch.tensor([[10, 20, 30], [40, 50, 60]])

# 3. squeeze()和unsqueeze()函数
print('squeeze()和unsqueeze()函数')
mydata1 = torch.tensor([1, 2, 3, 4, 5, 6])
print('mydata1->', mydata1.shape, mydata1)  # torch.Size([6])

mydata2 = mydata1.unsqueeze(dim=0)
print('在0维度上 扩展维度:', mydata2, mydata2.shape)  # torch.Size([1, 6])

mydata3 = mydata1.unsqueeze(dim=1)
print('在1维度上 扩展维度:\r\n', mydata3, mydata3.shape)  # torch.Size([6, 1])

mydata4 = mydata1.unsqueeze(dim=-1)
print('在-1维度上 扩展维度:\r\n', mydata3, mydata3.shape)  # torch.Size([6, 1])

mydata5 = mydata4.squeeze()
print('压缩维度:', mydata5, mydata5.shape)  # torch.Size([6])
print()
```
    
4. 修改形状
    - transpose()
    - permute()
    > transpose 函数可以实现交换张量形状的指定维度, 例如: 一个张量的形状为 (2, 3, 4) 可以通过 transpose 函数把 3 和 4进行交换, 将张量的形状变为 (2, 4, 3) 。
    > 
    > permute 函数可以一次交换更多的维度。
        
```python
data = torch.tensor([[10, 20, 30], [40, 50, 60]])

# 4.transpose() 和 permute()
print('transpose() 和 permute()')
data = torch.tensor(np.random.randint(0, 10, [2, 3, 3]))
print(f'data shape:{data.size()}')
print(data)
#   4.1 交换1 和 2维度
data_transpose = torch.transpose(data, 1, 2)
print(f'data_transpose shape:{data_transpose.size()}')

#   4.2 将data 的形状修改为 (4, 5, 3), 需要变换多次
data_transpose1 = torch.transpose(data, 0, 1)
print(data_transpose1)
data_transpose1 = torch.transpose(data_transpose1, 1, 2)
print(f'data_transpose1 shape:{data_transpose1.size()}')

#   4.3 使用 permute 函数将形状修改为 (4, 5, 3)
data_transpose2 = torch.permute(data, (1, 2, 0))
print(f'data_transpose1 shape:{data_transpose2.size()}')
```
        
    - view()
        > view 函数也可以用于修改张量的形状，只能用于存储在整块内存中的张量。
        > 在 PyTorch 中，有些张量是由不同的数据块组成的，它们并没有存储在整块的内存中，view 函数无法对这样的张量进行变形处理.
        > 例如: 一个张量经过了transpose 或者 permute 函数的处理之后，就无法使用 view 函数进行形状操作。
        
    - contiguous()
        > 若要使用view函数, 需要使用contiguous() 变成连续以后再使用view函数
        > is_contiguous() 判断是否 连续存储

```python
data = torch.tensor([[10, 20, 30], [40, 50, 60]])

# 5.view()和contiguous()函数

"""
1. 一个张量经过了 transpose 或者 permute 函数的处理之后，就无法使用view 函数进行形状操作若要使用view函数, 需要使用contiguous() 变成连续以后再使用view函数
2. 判断张量是否使用整块内存 is_contiguous
"""
print('view()和is_contiguous()函数')
data = torch.tensor([[10, 20, 30], [40, 50, 60]])
print('data--->', data, data.shape)

# 5.1 判断是否使用整块内存
print(data.is_contiguous())  # True

# 5.2 view
data_view = data.view(3, 2)
print('data_view ->', data_view, data_view.shape)

# 5.3 判断是否使用整块内存
print('data_view.is_contiguous->', data_view.is_contiguous())
print()

# 5.4 使用 transpose 函数修改形状
print('view()和contiguous()函数')
data_transpose = data.transpose(0, 1)
print('data_transpose->', data_transpose, data_transpose.shape)
print('data_transpose.is_contiguous->', data_transpose.is_contiguous())
print(data_transpose.contiguous().is_contiguous())
data_view = data_transpose.contiguous().view(2, 3)
print('data_view->', data_view.shape, data_view)
print('')
```

## 7.张量拼接操作

张量拼接（Concatenation）是将多个张量按指定的维度连接起来的操作。
- torch.cat()
    * torch.cat 是按指定维度将多个张量连接起来，拼接后的维度大小会变化，但总维数保持不变。
    
    * 使用时,所有张量在指定的拼接维度上必须形状一致。
    
      ```python
      # 1. torch.cat()
      print('================cat 方式拼接=====================')
      data1 = torch.randint(0, 10, [1, 2, 3])
      data2 = torch.randint(0, 10, [1, 2, 3])
      print(f'data1:{data1}')
      print(f'data2:{data2}')
      print()
      #   1.1 按 0维拼接
      new_data = torch.cat([data1, data2], dim=0)
      print('按 0维 拼接->', new_data, new_data.size())
      
      #   1.2 按 1维拼接
      new_data = torch.cat([data1, data2], dim=1)
      print('按 1维 拼接->', new_data, new_data.size())
      
      #   1.3 按 2维拼接
      new_data = torch.cat([data1, data2], dim=2)
      print('按 2维 拼接->', new_data, new_data.size())
      print()
      ```
    
- torch.stack() [了解]
    * torch.stack 是在新维度上将多个张量连接起来，拼接后的总维数会增加 1。
    
    * 使用时,所有张量的形状必须完全一致。
    
      ```python
      # 2.stack
      print('================stack 方式拼接=====================')
      data1 = torch.randint(0, 10, [1, 2, 3])
      data2 = torch.randint(0, 10, [1, 2, 3])
      print(f'data1:{data1}')
      print(f'data2:{data2}')
      
      #   2.1 按 0维连接
      new_data = torch.stack([data1, data2], dim=0)
      print('按 0维 连接->', new_data, new_data.size())
      
      #   2.2 按 1维连接
      new_data = torch.stack([data1, data2], dim=1)
      print('按 1维 连接->', new_data, new_data.size())
      
      
      #   2.3 按 2维连接
      new_data = torch.stack([data1, data2], dim=2)
      print('按 2维 连接->', new_data, new_data.size())
      print()
      ```

#### `torch.cat` 与 `torch.stack` 的区别

| **q特性**      | **torch.cat**    | **torch.stack**          |
| -------------- | ---------------- | ------------------------ |
| **总维数变化** | 不增加维数       | 增加 1 个维数            |
| **形状要求**   | 指定维度一致     | 所有维度必须完全一致     |
| **典型应用**   | 沿某个轴扩展数据 | 创建新的批量或时间步维度 |



## 8.自动微分模块

### 8.1 反向传播算法
```properties
在该算法中，参数（模型权重）会根据损失函数关于对应参数的梯度进行调整。
为了计算这些梯度，PyTorch内置了名为 torch.autograd 的微分引擎。
它支持任意计算图的自动梯度计算, 使用 backward 方法、grad 属性来实现梯度的计算和访问.
```



示例:

```python
# 1. 当X为标量时梯度的计算
def scaler_grad_compute():
    x = torch.tensor(5)
    # 目标值: label
    y = torch.tensor(0.)

    # 设置要更新的权重和偏置的初始值
    w = torch.tensor(1, requires_grad=True, dtype=torch.float32)
    b = torch.tensor(3, requires_grad=True, dtype=torch.float32)

    # 设置网络的输出值
    z = w * x + b  # 矩阵乘法?

    # 设置损失函数,并进行损失的计算
    loss = torch.nn.MSELoss()
    loss = loss(z, y)

    # 自动微分
    loss.backward()
    # 打印 w,b 变量的梯度
    # backward 函数计算的梯度值会存储在张量的 grad 变量中
    print(f'w->{w.grad}')
    print(f'b->{b.grad}')
# 2.非标量下时梯度的计算
def grad_compute():
    # 输入张量(2,5)
    x = torch.ones(2, 5)
    # 输出张量(2,3)
    y = torch.zeros(2, 3)
    # 设置要更新的权重和偏置的初始值
    w = torch.randn(5, 3, requires_grad=True)
    b = torch.randn(3, requires_grad=True)

    # 设置神经网络的输出值
    z = torch.matmul(x, w) + b
    # 设置损失函数,并进行损失的计算
    loss = torch.nn.MSELoss()
    loss = loss(z, y)  # 底层实现了__call__()方法
    print(y)
    # 自动微分
    loss.backward()
    # 打印 w,b 变量的梯度
    # backward 函数计算的梯度值会存储在张量的 grad 变量中
    print("W的梯度:", w.grad)
    print("b的梯度", b.grad)
```