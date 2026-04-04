from sqlalchemy.orm import Session
from database.models import Ticket
from utils.mask import mask_sensitive_data   # ✅ NEW IMPORT

def create_ticket(db: Session, user_query: str):
    masked_query = mask_sensitive_data(user_query)   # ✅ NEW LINE

    ticket = Ticket(user_query=masked_query)         # ✅ MODIFIED
    db.add(ticket)
    db.commit()
    db.refresh(ticket)
    return ticket

def get_all_tickets(db: Session):
    return db.query(Ticket).all()
