import sqlite3 as sq

def connect_db(path : str) -> sq.Connection:
    """

    连接数据库
    :param path: 数据库路径
    :return: 数据库连接
    """
    conn = sq.connect(path)
    return conn

def create_table(conn, table_name):
    """

    建表
    :param conn: 数据库连接
    :param table_name: 表名
    :return: None
    """
    c = conn.cursor()
    c.execute(f"""
        CREATE TABLE IF NOT EXISTS {table_name} (
            class_name TEXT NOT NULL,
            contest    TEXT NOT NULL,
            score      REAL NOT NULL CHECK(score >= 0),
            PRIMARY KEY (class_name, contest)
        )
    """)
    conn.commit()

def insert_scores(conn, scores, contest_id, table_name):
    """

    插入成绩
    :param conn: 数据库连接
    :param scores: 分数字典
    :param contest_id: 比赛id
    :param table_name: 表名
    :return: None
    """
    c = conn.cursor()
    c.executemany(
        f"""INSERT INTO {table_name}(class_name, contest, score)
            VALUES (?, ?, ?)
            ON CONFLICT(class_name, contest) DO UPDATE SET score = excluded.score""",
        [(cls, contest_id, score) for cls, score in scores.items()],
    )
    conn.commit()
