from os import getenv

MYSQL_DATABASE_USERNAME = getenv("MYSQL_DATABASE_USERNAME")
MYSQL_DATABASE_PASSWORD = getenv("MYSQL_DATABASE_PASSWORD")
MYSQL_DATABASE_HOST = getenv("MYSQL_DATABASE_HOST")
MYSQL_DATABASE_PORT = getenv("MYSQL_DATABASE_PORT")
MYSQL_DATABASE = getenv("MYSQL_DATABASE")  # check of DB exists in mysql server

MYSQL_DB_CONNECT_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8mb4'.format(MYSQL_DATABASE_USERNAME,
                                                                               MYSQL_DATABASE_PASSWORD,
                                                                               MYSQL_DATABASE_HOST,
                                                                               MYSQL_DATABASE_PORT,
                                                                               MYSQL_DATABASE)
SQLITE_DATABASE = getenv("SQLITE_DATABASE")
SQLITE_DB_CONNECT_URI = 'sqlite:///{}'.format(SQLITE_DATABASE)  # sqlite:/// for relative path & sqlite://// for
# absoulte path of db file


# ENVIRONMENT VALUES : put it in terminal env or edit configration of pyCharm
# MYSQL_DATABASE=data_db
# MYSQL_DATABASE_HOST=127.0.0.1
# MYSQL_DATABASE_PASSWORD=
# MYSQL_DATABASE_PORT=3306
# MYSQL_DATABASE_USERNAME=root
# PYTHONUNBUFFERED=1
# SQLITE_DATABASE=data.db

# for pycharm edit config
# MYSQL_DATABASE=data_db;MYSQL_DATABASE_HOST=127.0.0.1;MYSQL_DATABASE_PASSWORD=;MYSQL_DATABASE_PORT=3306;MYSQL_DATABASE_USERNAME=root;PYTHONUNBUFFERED=1;SQLITE_DATABASE=data.db
