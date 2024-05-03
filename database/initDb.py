from database import Base, mysqlEngine
from database.pushUpLogRepository import PushUpLogTable
from database.userRepository import UserTable


# comment this method database.initDb.createDb() if database.userRepository.UserTable is commented
# Q: why createDb() not in database.__init__
# Ans: coz to avoid cyclic import  database.__init__ imports->UserTable and UserTable imports->database.__init__
# and also we can call this createDb from route.py.main()
def createDb():
    Base.metadata.create_all(mysqlEngine)


# Note: the command Base.metadata.create_all(mysqlEngine) must be called after the class Table(Base) & only
# imported Table(Base) classes in the file where Base.metadata.create_all(mysqlEngine) is called will be created
# in MySql. usually if models are in different files then Base.metadata.create_all(mysqlEngine) could cause cyclic
# import due to cycle of import so the best way is having a initDb file where import all Table class & run


UserTable()  # to keep from database.userRepository import UserTable otherwise it'll say unnecessary import
PushUpLogTable()  # to keep from database.pushUpLogRepository import PushUpLogTable
