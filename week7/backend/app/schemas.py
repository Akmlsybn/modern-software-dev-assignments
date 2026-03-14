from datetime import datetime

from pydantic import BaseModel, Field


class TagRead(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True


class NoteCreate(BaseModel):
    title: str = Field(..., min_length=3, description="Title must be at least 3 characters")
    content: str = Field(..., min_length=1, description="Content cannot be empty")
    tags: list[str] | None = None


class NoteRead(BaseModel):
    id: int
    title: str
    content: str
    created_at: datetime
    updated_at: datetime
    tags: list[TagRead] = []

    class Config:
        from_attributes = True


class NotePatch(BaseModel):
    title: str | None = Field(default=None, min_length=3, description="Title must be at least 3 characters")
    content: str | None = Field(default=None, min_length=1, description="Content cannot be empty")
    tags: list[str] | None = None


class ActionItemCreate(BaseModel):
    description: str = Field(..., min_length=1, description="Description cannot be empty")


class ActionItemRead(BaseModel):
    id: int
    description: str
    completed: bool
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class ActionItemPatch(BaseModel):
    description: str | None = Field(default=None, min_length=1, description="Description cannot be empty")
    completed: bool | None = None


