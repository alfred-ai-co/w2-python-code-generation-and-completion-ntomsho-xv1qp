from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class TicketCreate(BaseModel):
    project_id: int = Field(..., description="ID of the project this ticket belongs to")
    title: str = Field(..., max_length=255, description="Title of the ticket")
    description: str = Field(..., description="Detailed description of the ticket")
    status: str = Field(..., max_length=255, description="Current status of the ticket")
    priority: str = Field(..., max_length=255, description="Priority level of the ticket")

class TicketResponse(TicketCreate):
    id: int = Field(..., description="Unique identifier of the ticket")
    project_id: int = Field(..., description="ID of the project this ticket belongs to")
    created_at: datetime = Field(..., description="Timestamp when the ticket was created")
    updated_at: datetime = Field(..., description="Timestamp when the ticket was last updated")

    class Config:
        from_attributes = True