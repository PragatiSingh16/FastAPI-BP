from sqlalchemy import (
    Column,
    ForeignKey,
    Integer,
    String,
)
from sqlalchemy.orm import relationship
from sqlalchemy import String
from ..core.db.database import Base

class Project(Base):
    _tablename_ = "projects"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    project_name = Column(String, index=True)
    project_desc = Column(String, index=True)
    modified_date = Column(String, index=True)
    # owner_id = Column(Integer, ForeignKey("user.uuid"))
    # owner = relationship("User", back_populates="projects")