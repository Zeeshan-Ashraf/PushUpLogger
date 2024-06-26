import logging
from dataclasses import dataclass

from overrides import overrides
from sqlalchemy import String, Column, Integer, text
from sqlalchemy.orm import Query, relationship

from database import mysqlEngine, mysqlSession, Base
from model.user import User
from repository.IUserRespository import IUserRepository

logger = logging.getLogger()
logger.setLevel(logging.INFO)

# uncomment below class Base if not using database.__init__.Base , either of them can be used but might cause issue
# while creating table (why? read NOTE in docstring)
# class Base(DeclarativeBase):
#     pass
'''
==============================================
NOTE: must use single Base for all the tables so that Base.metadata.create_all(mysqlEngine) can create tables with
dependency otherwise in case of P.K-F.K relationship you might get error that P.K user.id doesn't
exists (if Base.metadata.create_all(mysqlEngine)) not able to create primary_key table (user) before creating F.K
table (pushup_log)
==============================================
'''


@dataclass
class UserTable(Base):
    __tablename__ = 'user'
    id: Column = Column(Integer, primary_key=True, autoincrement=True)
    name: Column = Column(String(255), unique=True, nullable=False)
    email: Column = Column(String(255), name='email_id', unique=True, nullable=False)
    pushUpLogs = relationship('PushUpLogTable')  # this relationship col will not be created in DB TABLE

    # ^^^ can also use relationship(PushUpLogTable) but we used 'PushUpLogTable' to avoid cycle import

    def __repr__(self):
        return 'id={},name={},email={},pushUpLogs={}'.format(self.id, self.name, self.email, self.pushUpLogs)


'''
Note: the command Base.metadata.create_all(mysqlEngine) must be called after the class Table(Base) & only
imported Table(Base) classes in the file where Base.metadata.create_all(mysqlEngine) is called will be created
in MySql. usually if models are in different files then Base.metadata.create_all(mysqlEngine) could cause cyclic
import due to cycle of import so the best way is having a initDb file where import all Table class & run
'''


# Base.metadata.create_all(mysqlEngine)  #need to uncomment iff database.initDb.createDb() is commented

class UserRepository(IUserRepository):
    def findUserById(self, id: int) -> User:
        try:
            result: Query = mysqlSession.query(UserTable).filter(
                UserTable.id == id)  # returns Query (not the UserTable)
            # another short way: mysqlSession.get(UserTable, id) P.S: works on P.K & returns UserTable
            userData: UserTable = result.first()  # returns UserTable
            logging.info(userData)
            if userData is None:
                raise ValueError
            return User(userData.id, userData.name, userData.email)
        except Exception as e:
            mysqlSession.rollback()  # if this line not added then  ERROR:root:This Session's transaction has been rolled back due to a previous exception during flush. To begin a new transaction with this Session, first issue Session.rollback(). Original exception was: (pymysql.err.IntegrityError) (1062, "Duplicate entry 'Arsalan' for key 'user.name'")
            logging.exception(e)
            raise e

    def save(self, user: User) -> None:
        try:
            user: UserTable = UserTable(name=user.name, email=user.email)
            mysqlSession.add(user)
            mysqlSession.commit()
            logging.info(user)
        except Exception as e:
            mysqlSession.rollback()  # if this line not added then  ERROR:root:This Session's transaction has been rolled back due to a previous exception during flush. To begin a new transaction with this Session, first issue Session.rollback(). Original exception was: (pymysql.err.IntegrityError) (1062, "Duplicate entry 'Arsalan' for key 'user.name'")
            logging.exception(e)
            raise e

    def findAllUser(self):
        try:
            usersData: list[UserTable] = mysqlSession.query(UserTable).all()  # returns list[UserTable]
            logging.info(usersData)
            return [User(item.id, item.name, item.email) for item in usersData]
        except Exception as e:
            mysqlSession.rollback()
            raise e

    def findAllUserByGtIdDesc(self, id: int, like: str):
        try:
            usersData: list[UserTable] = (mysqlSession
                                          .query(UserTable)
                                          .filter(UserTable.id >= id, UserTable.name.ilike('%' + like + '%'))
                                          .order_by(UserTable.id.desc())
                                          .all())  # returns list[UserTable]

            if not usersData:
                raise ValueError

            logging.info(usersData)
            return [User(item.id, item.name, item.email) for item in usersData]
        except ValueError as e:
            raise e
        except Exception as e:
            mysqlSession.rollback()
            raise e

    def deleteUser(self, id: int):
        try:
            logging.info(mysqlSession.get(UserTable, id))  # session.get(Class, primary_key)
            mysqlSession.delete(mysqlSession.get(UserTable, id))
            mysqlSession.commit()
        except Exception as e:
            logging.exception(e)
            raise e

    @overrides
    def executeRaw(self, queryString: str):
        try:
            with mysqlEngine.connect() as executor:
                out = executor.execute(text(queryString))
                results = out.all()  # returns Sequence[Row] i.e list[Row] & Row is not jsonified
                print(list(results))
                executor.close()
                return [tuple(item) for item in results]
        except Exception as e:
            logging.exception(e)
            raise e

    @overrides()
    # note: offset will take longer if offset is way too long coz offset scan all rows
    def findAllUserPaginated(self, pageNo: int, pageSize: int = 3):  # page no starts from 1
        try:
            usersData: list[UserTable] = (mysqlSession.query(UserTable)
                                          .offset((pageNo - 1) * pageSize)
                                          .limit(pageSize)
                                          .all())  # returns list[UserTable]
            logging.info(usersData)
            return [User(item.id, item.name, item.email) for item in usersData]
        except Exception as e:
            mysqlSession.rollback()
            raise e
