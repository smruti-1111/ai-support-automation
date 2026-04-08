from pydantic import BaseModel

class TicketCreate(BaseModel):
    user_query: str

class TicketResponse(BaseModel):
    id: int
    user_query: str
    sentiment: str
    summary: str | None

    class Config:
        from_attributes = True
        