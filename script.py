import clean
import db_utils

PATH = './Score.xlsx'
DB_PATH = './Score.db'
TABLE = 'Score_table'


def run(sheet_name: str):
    """

    业务入口
    :param sheet_name: 表名
    :return: None
    """
    contest_id = clean.get_contest_id(PATH, sheet_name)
    scores = clean.get_score(PATH, sheet_name)

    conn = db_utils.connect_db(DB_PATH)
    db_utils.create_table(conn, TABLE)
    db_utils.insert_scores(conn, scores, contest_id, TABLE)
    conn.close()

    df = clean.get_sheets(PATH)[sheet_name]
    print(df)


if __name__ == '__main__':
    sheets = clean.get_sheets(PATH)
    sheets = [k for k,_ in sheets.items()]
    for sheet in sheets:
        print(f'正在处理表:{sheet}\n')
        run(sheet)