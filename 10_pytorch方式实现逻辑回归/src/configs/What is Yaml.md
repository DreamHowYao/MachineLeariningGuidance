YAML 是一种对人类非常友好的数据序列化格式，主要用来写配置文件。

### What is Yaml

YAML 是 "YAML Ain't Markup Language" 的递归缩写，强调它是**用于数据，而不是文档**的。它有几个很鲜明的特点：

*   **极致可读性**：它依赖**缩进**（用空格，不能用制表符）来表示层级关系，这让结构一目了然。
*   **简洁的语法**：用 `#` 来写注释，用 `---` 来分隔一个YAML文件中的多个文档。

#### Example

```yaml
# 应用配置
app:
  name: "My Application"
  version: 1.2.3
  ports:
    - 8000
    - 8001

database:
  host: "localhost"
  port: 5432
  credentials:
    username: "admin"
    password: "secret"
```

> `ports` 下的 `- 8000` 表示这是一个列表。

### 使用Python解析 YAML

#### 第一步：安装 PyYAML

在终端里执行以下命令即可安装：

```bash
pip install pyyaml
```

#### 第二步：读取和解析

最核心的用法是 `yaml.safe_load()`。这个方法会读取 YAML 文件并将其内容转换为 Python 原生的数据结构（字典、列表等）。

```python
import yaml

# 打开并安全地加载 YAML 文件
with open('config.yaml', 'r', encoding='utf-8') as file:
    config = yaml.safe_load(file)

# 现在 'config' 就是一个 Python 字典，可以像访问字典一样获取数据
app_name = config['app']['name']
first_port = config['app']['ports'][0]

print(f"应用名称: {app_name}")   # 输出: 应用名称: My Application
print(f"第一个端口: {first_port}") # 输出: 第一个端口: 8000
```

#### 关键函数及对比

在 PyYAML 中，有几个核心函数需要区分开：

| 函数                     | 用途                                 |
|:-----------------------|:-----------------------------------|
| **`yaml.safe_load()`** | 将 YAML 文档安全地解析为 Python 对象。         |
| `yaml.load()`          | 可以执行 YAML 中的任意代码，存在安全风险。           | 
| **`yaml.safe_dump()`** | 将 Python 对象安全地序列化为 YAML 格式的字符串或文件。 | 
| `yaml.dump()`          | 将 Python 对象序列化为 YAML，可能包含不安全的结构。   |
