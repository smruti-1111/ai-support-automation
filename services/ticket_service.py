from sqlalchemy.orm import Session
from database.models import Ticket
from utils.mask import mask_sensitive_data
from services.llm_service import analyze_text


def create_ticket(db: Session, user_query: str):
    # Step 1: Mask sensitive data
    masked_query = mask_sensitive_data(user_query)

    # Step 2: Send masked query to LLM
    llm_output = analyze_text(masked_query)

    # Step 3: Extract structured fields
    sentiment = llm_output.get("sentiment", "unknown")
    summary = llm_output.get("summary", "")

    # Step 4: Store in database
    ticket = Ticket(
        user_query=masked_query,
        sentiment=sentiment,
        summary=summary
    )

    db.add(ticket)
    db.commit()
    db.refresh(ticket)

    return ticket


def get_all_tickets(db: Session):
    return db.query(Ticket).all()
