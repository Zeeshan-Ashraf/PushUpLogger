# PushUpLogger
basic python flask CRUD application which logs pushup count for every user. App also enables basic Auth

## How to run
1. install `requirements.txt` by command `pip3 install -r requirements.txt `
2. install mysql by `brew install mysql` then start mysql `brew services start mysql`
3. create database in mysql by command login: `mysql -u root` then `CREATE DATABASE data_db;`
4. 
env value: put it in terminal env or edit configration of pyCharm
MYSQL_DATABASE=data_db

MYSQL_DATABASE_HOST=127.0.0.1

MYSQL_DATABASE_PASSWORD=

MYSQL_DATABASE_PORT=3306

MYSQL_DATABASE_USERNAME=root

PYTHONUNBUFFERED=1

SQLITE_DATABASE=data.db

for pycharm edit config
MYSQL_DATABASE=data_db;MYSQL_DATABASE_HOST=127.0.0.1;MYSQL_DATABASE_PASSWORD=;MYSQL_DATABASE_PORT=3306;MYSQL_DATABASE_USERNAME=root;PYTHONUNBUFFERED=1;SQLITE_DATABASE=data.db
5. run by play button on top of intellij having script `/<path/to>/PushUpLogger/route.py`
6. check `127.0.0.1:5000` in browser