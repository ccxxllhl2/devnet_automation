from create_db import create_db
from ops_func import *

db_name="NETWORK_OPS"
table_name="DB_NETOPS"
excel_path="excel/ops_info.xlsx"

def main():
    if not os.path.exists(db_name):
        create_db(db_name, table_name, excel_path)
    backup()
    
if __name__ == "__main__":
    main()