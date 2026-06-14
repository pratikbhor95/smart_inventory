from pydantic import BaseModel, ConfigDict
from typing import Optional

# Base schema for creating items
class ItemCreate(BaseModel):
    name: str
    description: str
    location_id: int
    subLocation_id: int
    quantity: float
    unit: str
    image: Optional[str] = "placeholder.jpg"
    embedding: Optional[list[float]] = None

# Response schema that includes ORM compatibility
class ItemResponse(ItemCreate):
    id: int
    
    model_config = ConfigDict(from_attributes=True)