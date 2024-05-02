import logging
from dataclasses import dataclass

from database.userRepository import UserRepository
from model.user import User

logger = logging.getLogger()
logger.setLevel(logging.INFO)


@dataclass
class UserService:
    userRepository: UserRepository = UserRepository()

    def getUser(self, id: int) -> User:
        try:
            user: User = self.userRepository.findUserById(id)
            return user
        except Exception as e:
            logger.exception(e)
            raise e

    def save(self, user: User) -> None:
        try:
            self.userRepository.save(user)
        except Exception as e:
            logging.exception(e)
            raise e

    def getAllUsers(self):
        try:
            users: list[User] = self.userRepository.findAllUser()
            return users
        except Exception as e:
            logging.exception(e)
            raise e

    def deleteUser(self, id: int):
        try:
            self.userRepository.deleteUser(id)
        except Exception as e:
            raise e

    def searchUser(self, minId: int, like: str):
        try:
            return self.userRepository.findAllUserByGtIdDesc(minId, like)
        except Exception as e:
            raise e

    def rawUserQuery(self, queryString):
        try:
            return self.userRepository.executeRaw(queryString)
        except Exception as e:
            raise e

    def allUserPaginated(self, pageNo: int, pageSize: int):
        try:
            if pageSize:
                return self.userRepository.findAllUserPaginated(pageNo, pageSize)
            else:
                return self.userRepository.findAllUserPaginated(pageNo)
        except Exception as e:
            raise e
