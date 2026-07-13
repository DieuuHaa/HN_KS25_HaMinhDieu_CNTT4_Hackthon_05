from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class LibraryModel(Base):
    __tablename__ = "teams"
    id = Column(Integer, primary_key=True, autoincrement= True)
    title = Column(String, nullable=False)
    author = Column(String, nullable=False)
    category = Column(String, nullable=False)
    quantity = Column(String, nullable= False)
    