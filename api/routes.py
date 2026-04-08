from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database.db import SessionLocal
from services.ticket_service import create_ticket, get_all_tickets
from schemas.ticket import TicketCreate

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/tickets")
def create_new_ticket(ticket: TicketCreate, db: Session = Depends(get_db)):
    return create_ticket(db, ticket.user_query)

@router.get("/tickets")
def fetch_tickets(db: Session = Depends(get_db)):
    return get_all_tickets(db)
    