# Import system libs
from pydantic import BaseModel

#######################################

class ComprasCreate(BaseModel):
    pago : bool
    estado_compra : str
    id_usuario: int

class ComprasUpdate(ComprasCreate):
    id: int

class Compras(ComprasUpdate):
    data : str

    class Config:
        from_attributes = True
