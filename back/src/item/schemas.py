# Import system libs
from pydantic import BaseModel

#######################################

class ItemCreate(BaseModel):
    nome : str
    tipo : str
    marca : str
    tamanho : str
    cor : str
    quantidade : int

class Item(ItemCreate):
    id: int

    class Config:
        from_attributes = True
