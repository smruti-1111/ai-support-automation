from sqlalchemy.orm import Session
from database.models import Ticket

def create_ticket(db: Session, user_query: str):
    ticket = Ticket(user_query=user_query)
    db.add(ticket)
    db.commit()
    db.refresh(ticket)
    return ticket

def get_all_tickets(db: Session):
    return db.query(Ticket).all()
