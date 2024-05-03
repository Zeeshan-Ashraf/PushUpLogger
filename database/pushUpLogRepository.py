import logging
from dataclasses import dataclass
from datetime import datetime

from sqlalchemy import Column, Integer, CheckConstraint, String, DateTime, ForeignKey

from database import mysqlSession, Base
from database.userRepository import UserTable
from model.pushUpLog import PushUpLog
from model.user import User
from repository.IPushUpLogRepository import IPushUpLogRepository

'''
it is recommended to use model.user.User & model.pushUpLog.PushUpLog itself as table instead of creating 
new class PushUpLogTable, but sometimes it might be required due to we dont want to save everything in DB
also it gives lose coupling between DB & service so that DB change migration or additional DB/redis can be
utilized without affecting service, just need to implement new class of new DB/Redis for repository.IUserRepository
'''


@dataclass
class PushUpLogTable(Base):
    __tablename__ = 'pushup_log'
    id = Column(Integer, primary_key=True, autoincrement=True)
    pushUpCount = Column(Integer, CheckConstraint("pushUpCount>0"), nullable=False)
    comment = Column(String(255))
    timestamp = Column(DateTime, default=datetime.utcnow())
    userId = Column(ForeignKey('user.id'))

    def __repr__(self):
        return 'id={},pushUpCount={},comment={},timestamp={},userId={}'.format(self.id, self.pushUpCount, self.comment,
                                                                               self.timestamp, self.userId)


# Base.metadata.create_all(mysqlEngine) #need to uncomment iff database.initDb.createDb() is commented
# why use Base here read Tute in docstring of database.userRepository.UserTable & UserRepository


@dataclass
class PushUpLogRepository(IPushUpLogRepository):
    def save(self, pushUpLog: PushUpLog):
        try:
            pushUpLogData: PushUpLogTable = PushUpLogTable(pushUpCount=pushUpLog.pushUpCount,
                                                           comment=pushUpLog.comment,
                                                           timestamp=pushUpLog.timestamp,
                                                           userId=pushUpLog.user.id)
            mysqlSession.add(pushUpLogData)
            mysqlSession.commit()
        except Exception as e:
            mysqlSession.rollback()
            logging.exception(e)
            raise e

    def getAll(self):
        def userTableToUser(userTable: UserTable):
            return User(userTable.id, userTable.name, userTable.email)

        try:
            result: list[PushUpLogTable] = mysqlSession.query(PushUpLogTable).all()
            if not result:
                raise ValueError
            return [PushUpLog(id=item.id, pushUpCount=item.pushUpCount, comment=item.comment, timestamp=item.timestamp,
                              user=userTableToUser(mysqlSession.get(UserTable, item.userId)))
                    for item in result]
        except Exception as e:
            mysqlSession.rollback()
            logging.exception(e)
            raise e
