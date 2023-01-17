from database import Base
from sqlalchemy import Column,String,Integer,ForeignKey
from sqlalchemy.orm import relationship


class Banks(Base):
    __tablename__ = 'banks'
    id = Column(Integer,primary_key=True,index=True)
    bank_id = Column(Integer)
    code = Column(String)
    name = Column(String)


class Customer(Base):
    __tablename__ = "customers"
    id = Column(Integer,primary_key=True,index=True)
    user_id = Column(Integer,ForeignKey('Users.id'))
    customer_id = Column(String)


class AccountRef(Base):
    __tablename__ = 'account_ref'
    id = Column(Integer,primary_key=True,index=True)
    user_id = Column(Integer,ForeignKey('Users.id'))
    accountReference = Column(String)


class UserReservedAccount(Base):
    __tablename__ = "user_accounts"
    id = Column(Integer,primary_key=True,index=True)
    user_id = Column(Integer,ForeignKey('Users.id'))
    bank_code = Column(String)
    bank_name = Column(String)
    AccountNumber = Column(String)
    AccountName = Column(String)






