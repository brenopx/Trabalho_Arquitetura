# Import system libs
from pydantic import BaseModel

#######################################

class UsuarioCreate(BaseModel):
    nome : str
    cpf : int
    email : str
    idade : int

class Usuario(UsuarioCreate):
    id: int

    class Config:
        from_attributes = True
