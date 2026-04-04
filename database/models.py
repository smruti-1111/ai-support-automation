from sqlalchemy import Column, Integer, String, Text
from .db import Base

class Ticket(Base):
    __tablename__ = "tickets"

    id = Column(Integer, primary_key=True, index=True)
    user_query = Column(Text)
    sentiment = Column(String, default="neutral")
    summary = Column(Text, nullable=True)
    