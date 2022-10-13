from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date, Float

Base = declarative_base()
    

class Transaction(Base):
    __tablename__ = 'transaction'
    id = Column(Integer, primary_key=True)
    time = Column(Integer)
    amount = Column(Float(2))
    Class = Column(Integer)
    
    def __repr__(self):
        return f"<Transaction#{self.id} Amt:{self.amount} Time:{self.time} Class:{self.Class}>"