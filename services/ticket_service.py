from sqlalchemy.orm import Session
from database.models import Ticket
from utils.mask import mask_sensitive_data
from services.llm_service import analyze_text, generate_response


def create_ticket(db: Session, user_query: str):
    # Step 1: Mask data
    masked_query = mask_sensitive_data(user_query)

    # Step 2: Analyze
    llm_output = analyze_text(masked_query)

    sentiment = llm_output.get("sentiment", "unknown")
    summary = llm_output.get("summary", "")
    category = llm_output.get("category", "general")
    priority = llm_output.get("priority", "low")

    # Step 3: Generate response
    auto_reply = generate_response(masked_query, sentiment)

    # Step 4: Decision logic
    escalation = False
    if priority == "high" or sentiment == "negative":
        escalation = True

    # Step 5: Store
    ticket = Ticket(
        user_query=masked_query,
        sentiment=sentiment,
        summary=summary,
        category=category,
        priority=priority,
        response=auto_reply
    )

    db.add(ticket)
    db.commit()
    db.refresh(ticket)

    return {
        "ticket": ticket,
        "escalation_required": escalation
    }


def get_all_tickets(db: Session):
    return db.query(Ticket).all()
    
