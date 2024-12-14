from pydantic import BaseModel

class GlossaryItemBase(BaseModel):
    term: str
    description: str

class GlossaryItemCreate(GlossaryItemBase):
    pass

class GlossaryItemResponse(GlossaryItemBase):
    id: int

    class Config:
        orm_mode = True
