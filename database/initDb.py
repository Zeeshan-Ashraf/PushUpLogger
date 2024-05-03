from database import Base, mysqlEngine
from database.pushUpLogRepository import PushUpLogTable
from database.userRepository import UserTable


# comment this method database.initDb.createDb() if database.userRepository.UserTable is commented
def createDb():
    Base.metadata.create_all(mysqlEngine)


UserTable()
PushUpLogTable()
