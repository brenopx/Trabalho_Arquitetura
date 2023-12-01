# Import system libs
from pydantic import BaseModel

#######################################

class ItemCompraCreate(BaseModel):
    quantidade : int
    id_compra : int
    id_item : int

class ItemCompra(ItemCompraCreate):
    id: int

    class Config:
        from_attributes = True
