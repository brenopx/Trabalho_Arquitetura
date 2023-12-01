# Import system libs
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session

# Import custom libs
from ..database import get_db
from . import schemas
from ..crud import Titemcompra

#######################################

# --------------------
def get_itemcompra_all(db:Session=Depends(get_db)):
    ''' Description \n
    `` (): \n
    return `` (): \n
    '''
    
    val_itemcompra = Titemcompra.get_itemcompra_all(db)

    if (val_itemcompra is None):
        raise HTTPException(
            status_code=404, 
            detail=f"Error searching for available."
        )

    return(val_itemcompra)
# --------------------

# --------------------
def get_itemcompra_id(id: int, db:Session=Depends(get_db)):
    ''' Description \n
    `` (): \n
    return `` (): \n
    '''
    
    val_itemcompra = Titemcompra.get_itemcompra_id(db, id)

    if (val_itemcompra is None):
        raise HTTPException(
            status_code=404, 
            detail=f"Error searching for available."
    )

    return(val_itemcompra)
# --------------------

# --------------------
def create_itemcompra(new_itemcompra:schemas.ItemCompraCreate, db:Session=Depends(get_db)):
    ''' Description \n
    `` (): \n
    return `` (): \n
    '''

    try:
        db_itemcompra = Titemcompra.create_itemcompra(db, new_itemcompra)
    except Exception as exc:
        msg = f"Error {exc}"
        print(msg)
        raise HTTPException(status_code=520, detail=msg)

    if (db_itemcompra is None):
        m_name = f"itemcompra data"
        raise HTTPException(status_code=404, detail=f"Error creating {m_name}.")

    return(db_itemcompra)
# --------------------

# --------------------
def get_itemcompra_compra_all(id_compra:int, db:Session=Depends(get_db)):
    ''' Description \n
    `` (): \n
    return `` (): \n
    '''
    
    val_itemcompra = Titemcompra.get_itemcompra_compra_all(db, id_compra)

    if (val_itemcompra is None):
        raise HTTPException(
            status_code=404, 
            detail=f"Error searching for available."
        )

    return(val_itemcompra)
# --------------------

# --------------------
def update_itemcompra(update_itemcompra:schemas.ItemCompra, db:Session=Depends(get_db)):
    ''' Description \n
    `` (): \n
    return `` (): \n
    '''

    val_col = Titemcompra.update_itemcompra(db, update_itemcompra)

    if (val_col is None):
        m_name = f"itemcompra data"
        raise HTTPException(status_code=404, detail=f"Error updating {m_name}.")

    return(val_col)
# --------------------

# --------------------
def delete_itemcompra(id: int, db:Session=Depends(get_db)):
    ''' Description \n
    `` (): \n
    return `` (): \n
    '''

    try:
        db_itemcompra = Titemcompra.delete_itemcompra(db, id)
    except Exception as exc:
        msg = f"Error {exc}"
        raise HTTPException(status_code=520, detail=msg)

    if (db_itemcompra is None):
        m_name = f"itemcompra data"
        raise HTTPException(status_code=404, detail=f"Error delete {m_name}.")

    return(db_itemcompra)
# --------------------