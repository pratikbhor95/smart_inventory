from app.core.database import Base
from sqlalchemy import Column , Integer, String, Boolean , ForeignKey
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.orm import relationship
from pgvector.sqlalchemy import Vector

class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)
    location_id = Column(Integer, ForeignKey("locations.id", ondelete="CASCADE"), nullable=False)
    subLocation_id = Column(Integer, ForeignKey("sublocations.id", ondelete="CASCADE"), nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    quantity = Column(Integer, nullable=False)
    unit = Column(String, nullable=False)
    image = Column(String, nullable=True)
    embedding = Column(Vector(768), nullable=True)
    
    location = relationship("Location")
    sublocation = relationship("SubLocation")

class Location(Base):
    __tablename__ = "locations"

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, nullable=False)

    sublocations = relationship("SubLocation", backref="location")

class SubLocation(Base):
    __tablename__ = "sublocations"

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, nullable=False)
    location_id = Column(Integer, ForeignKey("locations.id", ondelete="CASCADE"), nullable=False)