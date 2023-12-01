# Import system libs
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session

# Import custom libs
from ..database import get_db
from . import schemas
from ..crud import Tcompras

#######################################

# --------------------
def get_compras_all(db:Session=Depends(get_db)):
    ''' Description \n
    `` (): \n
    return `` (): \n
    '''
    
    val_compras = Tcompras.get_compras_all(db)

    if (val_compras is None):
        raise HTTPException(
            status_code=404, 
            detail=f"Error searching for available."
        )

    return(val_compras)
# --------------------

# --------------------
def get_compras_id(id: int, db:Session=Depends(get_db)):
    ''' Description \n
    `` (): \n
    return `` (): \n
    '''
    
    val_compras = Tcompras.get_compras_id(db, id)

    if (val_compras is None):
        raise HTTPException(
            status_code=404, 
            detail=f"Error searching for available."
    )

    return(val_compras)
# --------------------

# --------------------
def create_compras(new_compras:schemas.ComprasCreate, db:Session=Depends(get_db)):
    ''' Description \n
    `` (): \n
    return `` (): \n
    '''

    try:
        db_compras = Tcompras.create_compras(db, new_compras)
    except Exception as exc:
        msg = f"Error {exc}"
        print(msg)
        raise HTTPException(status_code=520, detail=msg)

    if (db_compras is None):
        m_name = f"compras data"
        raise HTTPException(status_code=404, detail=f"Error creating {m_name}.")

    return(db_compras)
# --------------------

# --------------------
def update_compras(update_compras:schemas.ComprasUpdate, db:Session=Depends(get_db)):
    ''' Description \n
    `` (): \n
    return `` (): \n
    '''
    val_col = Tcompras.update_compras(db, update_compras)

    if (val_col is None):
        m_name = f"compras data"
        raise HTTPException(status_code=404, detail=f"Error updating {m_name}.")

    return(val_col)
# --------------------

# --------------------
def compra_autorizada(id_compra:int, db:Session=Depends(get_db)):
    ''' Description \n
    `` (): \n
    return `` (): \n
    '''
    
    val_col = Tcompras.compra_autorizada(db, id_compra)

    if (val_col is None):
        m_name = f"compras data"
        raise HTTPException(status_code=404, detail=f"Error updating {m_name}.")

    return(val_col)
# --------------------

# --------------------
def delete_compras(id: int, db:Session=Depends(get_db)):
    ''' Description \n
    `` (): \n
    return `` (): \n
    '''

    try:
        db_compras = Tcompras.delete_compras(db, id)
    except Exception as exc:
        msg = f"Error {exc}"
        raise HTTPException(status_code=520, detail=msg)

    if (db_compras is None):
        m_name = f"compras data"
        raise HTTPException(status_code=404, detail=f"Error delete {m_name}.")

    return(db_compras)
# --------------------