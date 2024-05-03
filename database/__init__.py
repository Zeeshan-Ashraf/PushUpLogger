import atexit

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

from config import SQLITE_DB_CONNECT_URI, MYSQL_DB_CONNECT_URI

sqliteEngine = create_engine(SQLITE_DB_CONNECT_URI)
SqliteSession = sessionmaker(bind=sqliteEngine)
sqliteSession = SqliteSession()

mysqlEngine = create_engine(MYSQL_DB_CONNECT_URI, echo=True)
MysqlSession = sessionmaker(bind=mysqlEngine)
mysqlSession = MysqlSession()

Base = declarative_base()


def close_db_session():
    mysqlSession.close()
    sqliteSession.close()


atexit.register(close_db_session)
