import pandas as pd

def get_score(path: str, sheet_name: str) -> dict:
    """

    获取分数字典
    :param path: 表路径
    :param sheet_name: 表名
    :return: 分数字典 {"班级_姓名" : "分数"}
    """
    # 读取指定 sheet
    df = pd.read_excel(path, sheet_name=sheet_name, header=2)

    # 过滤掉姓名为空的行
    df = df[df['姓名'].notna() & (df['姓名'].astype(str).str.strip() != '')]

    names = df['姓名']
    clss = df['班级']
    scores = df['E']

    dict_score = {f"{cls}_{name}": score for name, cls, score in zip(names, clss, scores)}

    return dict_score

def get_sheets(path : str) -> dict:
    """

    获取所有表
    :param path: 表路径
    :return: 表字典
    """
    all_sheets = pd.read_excel(path, sheet_name=None, header=2)
    return all_sheets

def get_contest_id(path: str, sheet_name: str) -> str:
    """

    获取比赛ID
    :param path: 表路径
    :param sheet_name: 表名
    :return: 比赛id
    """
    df = pd.read_excel(path, sheet_name=sheet_name, header=None, nrows=1)
    raw = str(df.iloc[0, 0])
    return raw.split(':')[-1].strip()