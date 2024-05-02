from abc import ABC, abstractmethod

from model.user import User


class IUserRepository(ABC):
    @abstractmethod
    def findUserById(self, id: int) -> User:
        pass

    @abstractmethod
    def save(self, user: User) -> None:
        pass

    @abstractmethod
    def findAllUser(self):
        pass

    @abstractmethod
    def deleteUser(self, id: int):
        pass

    @abstractmethod
    def findAllUserByGtIdDesc(self, id: int, like: str):
        pass

    def executeRaw(self, queryString: str):
        pass

    def findAllUserPaginated(self, pageNo: int, pageSize: int):
        pass
