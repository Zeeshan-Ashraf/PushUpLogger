from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from config import SQLITE_DB_CONNECT_URI, MYSQL_DB_CONNECT_URI

sqliteEngine = create_engine(SQLITE_DB_CONNECT_URI)
SqliteSession = sessionmaker(bind=sqliteEngine)
sqliteSession = SqliteSession()

mysqlEngine = create_engine(MYSQL_DB_CONNECT_URI)

# createDBStr = "CREATE DATABASE IF NOT EXISTS {};".format(MYSQL_DATABASE)
# print("Execution of DB START++++++++++++++++++++++++++++++++++++++++++++++")
# print(createDBStr)
# try:
#     with mysqlEngine.begin() as conn:
#         result = conn.execute(text(createDBStr), )
#         result.fetchall()
# except Exception as e:
#     print(e.__repr__())
# print("Execution of DB DONE===============================================")

MysqlSession = sessionmaker(bind=mysqlEngine)
mysqlSession = MysqlSession()
