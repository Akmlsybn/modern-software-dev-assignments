from pydantic import BaseModel, Field
from typing import Optional


class NoteCreate(BaseModel):
    content: str = Field(..., min_length=1, max_length=5000, description="Note content")


class NoteRead(BaseModel):
    id: int
    content: str
    created_at: str

    class Config:
        from_attributes = True


class ActionItemCreate(BaseModel):
    text: str = Field(..., min_length=1, max_length=500, description="Action item text")


class ActionItemRead(BaseModel):
    id: int
    note_id: Optional[int] = None
    text: str
    done: bool
    created_at: str

    class Config:
        from_attributes = True


class ActionItemUpdate(BaseModel):
    done: bool = Field(..., description="Mark item as done or not")


class ExtractRequest(BaseModel):
    text: str = Field(..., min_length=1, max_length=5000, description="Text to extract from")
    save_note: bool = Field(default=False, description="Save as note after extraction")


class ExtractResponse(BaseModel):
    note_id: Optional[int] = None
    items: list[ActionItemRead]
