import sqlite3 as sql
import pandas as pd


def create_db(db_name, table_name, excel_path):
    DB = sql.connect(db_name)
    CURSOR = DB.cursor()
    init_sql = f'''CREATE TABLE IF NOT EXISTS {table_name} (id INTEGER PRIMARY KEY,设备类型 TEXT,设备IP TEXT, 登入用户名 TEXT, 登入密码 TEXT)'''
    CURSOR.execute(init_sql)
    # 读入excel数据
    datas = pd.read_excel(excel_path)
    # 完成数据迁移
    for line_num in range(datas.shape[0]):
        db_line = list(datas.values[line_num])
        db_line.insert(0,line_num+1)
        CURSOR.execute(f"INSERT INTO {table_name} VALUES(?,?,?,?,?)", db_line)
    # 验证DB
    CURSOR.execute(f"SELECT * FROM {table_name}")
    print(CURSOR.fetchall())
    # 确认DB
    DB.commit()