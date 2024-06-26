from pydantic import BaseModel


class TagBase(BaseModel):
    name: str


class TagCreate(TagBase):
    pass


class TagUpdate(TagBase):
    pass


class TagRead(TagBase):
    id: int

    class Config:
        orm_mode: True


class TagsRead(TagBase):

    class Config:
        orm_mode: True
