# Import system libs
from pydantic import BaseModel

#######################################

class EnderecoCreate(BaseModel):
    endereco : str
    numero : int
    complemento : str
    estado : str
    pais : str
    id_usuario : int


class Endereco(EnderecoCreate):
    id: int

    class Config:
        from_attributes = True


