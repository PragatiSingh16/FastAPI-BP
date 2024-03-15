from pydantic import BaseModel


class ProjectBase(BaseModel):
    project_name: str
    project_desc: str | None = None
    modified_date: str | None = None
    owner_id: int

class Project(ProjectBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True


class ProjectCreate(ProjectBase):
    pass