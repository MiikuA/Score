# README

## 项目说明

- 本项目因方便持久化数据以及快速计算成绩而诞生

- 本项目使用的是`Python`和`Sqlite3`，数据处理部分使用的`Pandas`，格式兼容部分使用的`openpyxl`

## 环境需求

> [!IMPORTANT]
> Python: 3.12+
> Pandas:`pip install pandas`
> openxls: `pip install openpyxl`

## 文件说明

### clean 模块

- clean 模块主要用于处理Excel表数据

- 详见程序本体

### db_utils 模块

- db_utils 模块用于数据库相关的操作

### script 模块

- 业务入口

### Rank.sql

- 查询视图，会按照总得分进行降序排序，同时计算平均得分
  
## LICENCE

- 详见 [LICENCE](LICENCE)文件
