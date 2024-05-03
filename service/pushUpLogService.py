from dataclasses import dataclass
from datetime import datetime

from database.pushUpLogRepository import PushUpLogRepository
from database.userRepository import UserRepository
from model.pushUpLog import PushUpLog
from model.user import User
from repository.IPushUpLogRepository import IPushUpLogRepository


@dataclass
class PushUpLogService:
    pushUpLogRepository: IPushUpLogRepository = PushUpLogRepository()
    userRepository: UserRepository = UserRepository()

    def getAll(self):
        try:
            return self.pushUpLogRepository.getAll()
        except Exception as e:
            raise e

    def save(self, userId: int, count: int, comment: str):
        try:
            user: User = self.userRepository.findUserById(id=userId)
            self.pushUpLogRepository.save(
                PushUpLog(pushUpCount=count, comment=comment, timestamp=datetime.utcnow(), user=user))
        except Exception as e:
            raise e
