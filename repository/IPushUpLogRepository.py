from abc import ABC, abstractmethod

from model.pushUpLog import PushUpLog


class IPushUpLogRepository(ABC):
    @abstractmethod
    def save(self, pushUpLog: PushUpLog):
        pass

    @abstractmethod
    def getAll(self):
        pass
