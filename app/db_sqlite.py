import databases
from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable, SQLAlchemyUserDatabase, SQLAlchemyBaseOAuthAccountTable
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, DeclarativeMeta

from authentication.Models import UserDB

SQLITE_DB = "sqlite://./postgres.db"

engine = create_engine(SQLITE_DB, connetion_args={"check_same_thread": "False"})

# session_local = sessionmaker(engine, autoflush=False, autocommit=False)
database = databases.Database(SQLITE_DB)
Base: DeclarativeMeta = declarative_base()

Base.metadata.create_all(engine)


class UserTable(Base, SQLAlchemyBaseUserTable):
    pass


class OAuthAccount(Base, SQLAlchemyBaseOAuthAccountTable):
    pass


users = UserTable.__table__
oauth_accounts = OAuthAccount.__table__


def get_user_db():
    yield SQLAlchemyUserDatabase(UserDB, database, users, oauth_accounts)
