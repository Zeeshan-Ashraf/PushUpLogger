import logging
from dataclasses import dataclass
from datetime import datetime

from sqlalchemy import Column, Integer, CheckConstraint, String, DateTime, ForeignKey

from database import mysqlSession, Base
from model.pushUpLog import PushUpLog
from repository.IPushUpLogRepository import IPushUpLogRepository


@dataclass
class PushUpLogTable(Base):
    __tablename__ = 'pushup_log'
    id = Column(Integer, primary_key=True, autoincrement=True)
    pushUpCount = Column(Integer, CheckConstraint("pushUpCount>0"), nullable=False)
    comment = Column(String(255))
    timestamp = Column(DateTime, default=datetime.utcnow())
    userId = Column(ForeignKey('user.id'))


# Base.metadata.create_all(mysqlEngine)


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
        try:
            result = mysqlSession.query(PushUpLogTable).all()
            print(result)
            if not result:
                raise ValueError
            return result
        except Exception as e:
            mysqlSession.rollback()
            logging.exception(e)
            raise e
