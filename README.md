# PushUpLogger
basic python flask CRUD application which logs pushup count for every user. App also enables basic Auth

## How to run
1. install `requirements.txt` by command `pip3 install -r requirements.txt `
2. install mysql by `brew install mysql` then start mysql `brew services start mysql`
3. create database in mysql by command login: `mysql -u root` then `CREATE DATABASE data_db;`
4. run by cmd `python3 route.py`
5. check `127.0.0.1:5000` in browser