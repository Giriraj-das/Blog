from pydantic import BaseModel


class AuthorBase(BaseModel):
    name: str
    email: str


class AuthorCreate(AuthorBase):
    pass


class AuthorUpdate(AuthorBase):
    pass


class AuthorRead(AuthorBase):
    id: int

    class Config:
        orm_mode: True


class AuthorsRead(BaseModel):
    name: str

    class Config:
        orm_mode: True
