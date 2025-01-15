from sqlalchemy import Column, Integer, String, Numeric, Date, Time, Float, ARRAY, func
from database import Base

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    name = Column(String(255), nullable=False)
    height = Column(Numeric(10, 2), nullable=False)
    date = Column(Date, default=func.current_date())
    time = Column(Time, default=func.current_time())
    vector = Column(ARRAY(Float))
