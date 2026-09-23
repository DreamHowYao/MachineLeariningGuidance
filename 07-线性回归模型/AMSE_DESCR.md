**询问购房者描述他们梦想中的房子时**,他们可能不会从地下室天花板的高度或是否靠近东西向铁路开始说起。但这个 playground 竞赛的数据集证明,影响价格谈判的因素远不止卧室数量或白色尖桩篱笆。

该数据集包含 79 个解释变量,描述了爱荷华州艾姆斯市住宅的（几乎）各个方面,本次竞赛要求您预测每栋房屋的最终价格。

*   **MSSubClass**: 标识销售中涉及的住宅类型。
    *   20: 一层住宅 (1946年及以后,所有风格)
    *   30: 一层住宅 (1945年及以前)
    *   40: 一层带装修阁楼 (所有年代)
    *   45: 一层半 - 未装修 (所有年代)
    *   50: 一层半 - 已装修 (所有年代)
    *   60: 两层住宅 (1946年及以后)
    *   70: 两层住宅 (1945年及以前)
    *   75: 两层半住宅 (所有年代)
    *   80: 错层或多层
    *   85: 错层门厅
    *   90: 复式住宅 - 所有风格和年代
    *   120: 一层 PUD (规划单元开发) - (1946年及以后)
    *   150: 一层半 PUD - (所有年代)
    *   160: 两层 PUD - (1946年及以后)
    *   180: PUD - 多层 - 包括错层/门厅
    *   190: 双户改造 - 所有风格和年代

*   **MSZoning**: 标识销售的一般分区分类。
    *   A: 农业
    *   C: 商业
    *   FV: 浮村住宅区
    *   I: 工业
    *   RH: 住宅高密度
    *   RL: 住宅低密度
    *   RP: 住宅低密度公园
    *   RM: 住宅中等密度

*   **LotFrontage**: 与物业相连的街道线性英尺数

*   **LotArea**: 地块面积 (平方英尺)

*   **Street**: 通往物业的道路类型
    *   Grvl: 碎石
    *   Pave: 铺设

*   **Alley**: 通往物业的小巷类型
    *   Grvl: 碎石
    *   Pave: 铺设
    *   NA: 无小巷通道

*   **LotShape**: 物业的大致形状
    *   Reg: 规则
    *   IR1: 略不规则
    *   IR2: 中度不规则
    *   IR3: 不规则

*   **LandContour**: 物业的平整度
    *   Lvl: 接近平坦/水平
    *   Bnk: 倾斜 - 从街道到建筑有快速显著的上升
    *   HLS: 山坡 - 从一侧到另一侧有显著坡度
    *   Low: 洼地

*   **Utilities**: 可用的公用事业类型
    *   AllPub: 所有公共设施 (电、气、水、下水道)
    *   NoSewr: 电力、燃气和水 (化粪池)
    *   NoSeWa: 仅电力和燃气
    *   ELO: 仅电力

*   **LotConfig**: 地块配置
    *   Inside: 内部地块
    *   Corner: 转角地块
    *   CulDSac: 死胡同
    *   FR2: 临街两面
    *   FR3: 临街三面

*   **LandSlope**: 物业的坡度
    *   Gtl: 缓坡
    *   Mod: 中等坡度
    *   Sev: 陡坡

*   **Neighborhood**: 艾姆斯市内的物理位置
    *   Blmngtn: Bloomington Heights
    *   Blueste: Bluestem
    *   BrDale: Briardale
    *   BrkSide: Brookside
    *   ClearCr: Clear Creek
    *   CollgCr: College Creek
    *   Crawfor: Crawford
    *   Edwards: Edwards
    *   Gilbert: Gilbert
    *   IDOTRR: 爱荷华州交通部和铁路
    *   MeadowV: Meadow Village
    *   Mitchel: Mitchell
    *   Names: North Ames
    *   NoRidge: Northridge
    *   NPkVill: Northpark Villa
    *   NridgHt: Northridge Heights
    *   NWAmes: Northwest Ames
    *   OldTown: Old Town
    *   SWISU: 爱荷华州立大学西南部
    *   Sawyer: Sawyer
    *   SawyerW: Sawyer West
    *   Somerst: Somerset
    *   StoneBr: Stone Brook
    *   Timber: Timberland
    *   Veenker: Veenker

*   **Condition1**: 靠近各种条件/设施
    *   Artery: 毗邻主干道
    *   Feedr: 毗邻支路
    *   Norm: 正常
    *   RRNn: 在南北铁路200英尺范围内
    *   RRAn: 毗邻南北铁路
    *   PosN: 靠近积极的外部设施——公园、绿地等
    *   PosA: 毗邻积极的外部设施
    *   RRNe: 在东西铁路200英尺范围内
    *   RRAe: 毗邻东西铁路

*   **Condition2**: 靠近各种条件 (如果存在多于一个)
    *   (含义同 Condition1)

*   **BldgType**: 住宅类型
    *   1Fam: 独立单户
    *   2FmCon: 双户改造；最初建为单户住宅
    *   Duplx: 复式
    *   TwnhsE: 联排别墅端头单元
    *   TwnhsI: 联排别墅内部单元

*   **HouseStyle**: 住宅风格
    *   1Story: 一层
    *   1.5Fin: 一层半：二楼已装修
    *   1.5Unf: 一层半：二楼未装修
    *   2Story: 两层
    *   2.5Fin: 两层半：二楼已装修
    *   2.5Unf: 两层半：二楼未装修
    *   SFoyer: 错层门厅
    *   SLvl: 错层

*   **OverallQual**: 评估房屋的整体材料和装修质量
    *   10: 非常优秀
    *   9: 优秀
    *   8: 非常好
    *   7: 好
    *   6: 中上
    *   5: 平均
    *   4: 中下
    *   3: 一般
    *   2: 差
    *   1: 非常差

*   **OverallCond**: 评估房屋的整体状况
    *   (评分含义同 OverallQual)

*   **YearBuilt**: 原始建筑日期

*   **YearRemodAdd**: 翻新日期 (如果无翻新或加建,则同建筑日期)

*   **RoofStyle**: 屋顶类型
    *   Flat: 平顶
    *   Gable: 山墙
    *   Gambrel: 复折式 (谷仓式)
    *   Hip: 四坡
    *   Mansard: 孟莎
    *   Shed: 单坡

*   **RoofMatl**: 屋顶材料
    *   ClyTile: 粘土或瓦片
    *   CompShg: 标准 (复合) 木瓦
    *   Membran: 薄膜
    *   Metal: 金属
    *   Roll: 卷材
    *   Tar&Grv: 砾石及焦油
    *   WdShake: 木摇板
    *   WdShngl: 木瓦

*   **Exterior1st**: 房屋外部覆盖材料
    *   AsbShng: 石棉瓦
    *   AsphShn: 沥青瓦
    *   BrkComm: 普通砖
    *   BrkFace: 饰面砖
    *   CBlock: 煤渣砖
    *   CemntBd: 水泥板
    *   HdBoard: 硬板
    *   ImStucc: 仿灰泥
    *   MetalSd: 金属壁板
    *   Other: 其他
    *   Plywood: 胶合板
    *   PreCast: 预制
    *   Stone: 石材
    *   Stucco: 灰泥
    *   VinylSd: 乙烯基壁板
    *   Wd Sdng: 木质壁板
    *   WdShing: 木瓦

*   **Exterior2nd**: 房屋外部覆盖材料 (如果使用多于一种材料)
    *   (选项同 Exterior1st)

*   **MasVnrType**: 砌体饰面类型
    *   BrkCmn: 普通砖
    *   BrkFace: 饰面砖
    *   CBlock: 煤渣砖
    *   None: 无
    *   Stone: 石材

*   **MasVnrArea**: 砌体饰面面积 (平方英尺)

*   **ExterQual**: 评估外部材料质量
    *   Ex: 优秀
    *   Gd: 好
    *   TA: 平均/典型
    *   Fa: 一般
    *   Po: 差

*   **ExterCond**: 评估外部材料的当前状况
    *   (评级含义同 ExterQual)

*   **Foundation**: 地基类型
    *   BrkTil: 砖瓦
    *   CBlock: 煤渣砖
    *   PConc: 现浇混凝土
    *   Slab: 板式
    *   Stone: 石材
    *   Wood: 木质

*   **BsmtQual**: 评估地下室高度
    *   Ex: 优秀 (100+ 英寸)
    *   Gd: 好 (90-99 英寸)
    *   TA: 典型 (80-89 英寸)
    *   Fa: 一般 (70-79 英寸)
    *   Po: 差 (<70 英寸)
    *   NA: 无地下室

*   **BsmtCond**: 评估地下室总体状况
    *   Ex: 优秀
    *   Gd: 好
    *   TA: 典型 - 允许轻微潮湿
    *   Fa: 一般 - 潮湿或有裂缝或沉降
    *   Po: 差 - 严重裂缝、沉降或潮湿
    *   NA: 无地下室

*   **BsmtExposure**: 指地下室或花园层墙体是否露出地面
    *   Gd: 良好采光/暴露
    *   Av: 平均采光/暴露 (错层或门厅通常为平均或以上)
    *   Mn: 最小采光/暴露
    *   No: 无采光/暴露
    *   NA: 无地下室

*   **BsmtFinType1**: 地下室已装修区域的评级
    *   GLQ: 良好居住区
    *   ALQ: 平均居住区
    *   BLQ: 低于平均的居住区
    *   Rec: 平均娱乐室
    *   LwQ: 低质量
    *   Unf: 未装修
    *   NA: 无地下室

*   **BsmtFinSF1**: 类型1的已装修平方英尺

*   **BsmtFinType2**: 地下室已装修区域的评级 (如果存在多种类型)
    *   (评级含义同 BsmtFinType1)

*   **BsmtFinSF2**: 类型2的已装修平方英尺

*   **BsmtUnfSF**: 地下室未装修的平方英尺

*   **TotalBsmtSF**: 地下室总平方英尺

*   **Heating**: 供暖类型
    *   Floor: 地板炉
    *   GasA: 燃气强制热风炉
    *   GasW: 燃气热水或蒸汽供暖
    *   Grav: 重力炉
    *   OthW: 非燃气热水或蒸汽供暖
    *   Wall: 壁炉

*   **HeatingQC**: 供暖质量和状况
    *   Ex: 优秀
    *   Gd: 好
    *   TA: 平均/典型
    *   Fa: 一般
    *   Po: 差

*   **CentralAir**: 中央空调
    *   N: 无
    *   Y: 有

*   **Electrical**: 电气系统
    *   SBrkr: 标准断路器 和 Romex 电线
    *   FuseA: 保险丝盒 (超过60安培) 和全部 Romex 电线 (平均)
    *   FuseF: 60安培保险丝盒 和 大部分 Romex 电线 (一般)
    *   FuseP: 60安培保险丝盒 和 大部分 knob-and-tube 电线 (差)
    *   Mix: 混合

*   **1stFlrSF**: 一楼平方英尺

*   **2ndFlrSF**: 二楼平方英尺

*   **LowQualFinSF**: 低质量装修平方英尺 (所有楼层)

*   **GrLivArea**: 地面以上居住面积平方英尺

*   **BsmtFullBath**: 地下室全卫数量

*   **BsmtHalfBath**: 地下室半卫数量

*   **FullBath**: 地面以上全卫数量

*   **HalfBath**: 地面以上半卫数量

*   **Bedroom**: 地面以上卧室数量 (不包括地下室卧室)

*   **Kitchen**: 地面以上厨房数量

*   **KitchenQual**: 厨房质量
    *   Ex: 优秀
    *   Gd: 好
    *   TA: 典型/平均
    *   Fa: 一般
    *   Po: 差

*   **TotRmsAbvGrd**: 地面以上房间总数 (不包括浴室)

*   **Functional**: 家庭功能 (除非需要扣减,否则假定为典型)
    *   Typ: 典型功能
    *   Min1: 轻微扣减1
    *   Min2: 轻微扣减2
    *   Mod: 中等扣减
    *   Maj1: 主要扣减1
    *   Maj2: 主要扣减2
    *   Sev: 严重损坏
    *   Sal: 仅可回收

*   **Fireplaces**: 壁炉数量

*   **FireplaceQu**: 壁炉质量
    *   Ex: 优秀 - 卓越的砖石壁炉
    *   Gd: 好 - 主层的砖石壁炉
    *   TA: 平均 - 主生活区的预制壁炉或地下室的砖石壁炉
    *   Fa: 一般 - 地下室的预制壁炉
    *   Po: 差 - 富兰克林炉
    *   NA: 无壁炉

*   **GarageType**: 车库位置
    *   2Types: 多于一种类型的车库
    *   Attchd: 与住宅相连
    *   Basment: 地下室车库
    *   BuiltIn: 内置 (车库是房屋的一部分 - 通常车库上方有房间)
    *   CarPort: 车棚
    *   Detchd: 与住宅分离
    *   NA: 无车库

*   **GarageYrBlt**: 车库建造年份

*   **GarageFinish**: 车库内部装修
    *   Fin: 已装修
    *   RFn: 粗装修
    *   Unf: 未装修
    *   NA: 无车库

*   **GarageCars**: 车库容量 (以车位数计)

*   **GarageArea**: 车库面积 (平方英尺)

*   **GarageQual**: 车库质量
    *   Ex: 优秀
    *   Gd: 好
    *   TA: 典型/平均
    *   Fa: 一般
    *   Po: 差
    *   NA: 无车库

*   **GarageCond**: 车库状况
    *   (评级含义同 GarageQual)

*   **PavedDrive**: 铺设的车道
    *   Y: 已铺设
    *   P: 部分铺设
    *   N: 泥土/碎石

*   **WoodDeckSF**: 木质露台面积 (平方英尺)

*   **OpenPorchSF**: 开放式门廊面积 (平方英尺)

*   **EnclosedPorch**: 封闭式门廊面积 (平方英尺)

*   **3SsnPorch**: 三季门廊面积 (平方英尺)

*   **ScreenPorch**: 纱窗门廊面积 (平方英尺)

*   **PoolArea**: 游泳池面积 (平方英尺)

*   **PoolQC**: 游泳池质量
    *   Ex: 优秀
    *   Gd: 好
    *   TA: 平均/典型
    *   Fa: 一般
    *   NA: 无游泳池

*   **Fence**: 围栏质量
    *   GdPrv: 良好隐私
    *   MnPrv: 最低隐私
    *   GdWo: 良好木质
    *   MnWw: 最低木质/铁丝
    *   NA: 无围栏

*   **MiscFeature**: 其他类别未涵盖的杂项特征
    *   Elev: 电梯
    *   Gar2: 第二个车库 (如果未在车库部分描述)
    *   Othr: 其他
    *   Shed: 棚屋 (超过100平方英尺)
    *   TenC: 网球场
    *   NA: 无

*   **MiscVal**: 杂项特征的价值 (美元)

*   **MoSold**: 销售月份 (MM)

*   **YrSold**: 销售年份 (YYYY)

*   **SaleType**: 销售类型
    *   WD: 担保契约 - 常规
    *   CWD: 担保契约 - 现金
    *   VWD: 担保契约 - VA贷款
    *   New: 新建并出售的房屋
    *   COD: 法院官员契约/遗产
    *   Con: 合同,15% 首付,常规条款
    *   ConLw: 合同,低首付和低利率
    *   ConLI: 合同,低利率
    *   ConLD: 合同,低首付
    *   Oth: 其他

*   **SaleCondition**: 销售条件
    *   Normal: 正常销售
    *   Abnorml: 非正常销售 - 交易、止赎、卖空
    *   AdjLand: 毗邻土地购买
    *   Alloca: 分配 - 两个关联的物业有独立的契约,通常是带车库单元的公寓
    *   Family: 家庭成员之间的销售
    *   Partial: 上次评估时房屋未完工 (与新建房屋相关)
