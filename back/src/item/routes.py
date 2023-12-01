# Import system libs
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session

# Import custom libs
from ..database import get_db
from . import schemas
from ..crud import Titem

#######################################

# --------------------
def get_item_all(db:Session=Depends(get_db)):
    ''' Description \n
    `` (): \n
    return `` (): \n
    '''
    
    val_item = Titem.get_item_all(db)

    if (val_item is None):
        raise HTTPException(
            status_code=404, 
            detail=f"Error searching for available."
        )

    return(val_item)
# --------------------

# --------------------
def get_item_id(id: int, db:Session=Depends(get_db)):
    ''' Description \n
    `` (): \n
    return `` (): \n
    '''
    
    val_item = Titem.get_item_id(db, id)

    if (val_item is None):
        raise HTTPException(
            status_code=404, 
            detail=f"Error searching for available."
    )

    return(val_item)
# --------------------

# --------------------
def create_item(new_item:schemas.ItemCreate, db:Session=Depends(get_db)):
    ''' Description \n
    `` (): \n
    return `` (): \n
    '''

    try:
        db_item = Titem.create_item(db, new_item)
    except Exception as exc:
        msg = f"Error {exc}"
        print(msg)
        raise HTTPException(status_code=520, detail=msg)

    if (db_item is None):
        m_name = f"item data"
        raise HTTPException(status_code=404, detail=f"Error creating {m_name}.")

    return(db_item)
# --------------------

# --------------------
def update_item(update_item:schemas.Item, db:Session=Depends(get_db)):
    ''' Description \n
    `` (): \n
    return `` (): \n
    '''

    val_col = Titem.update_item(db, update_item)

    if (val_col is None):
        m_name = f"item data"
        raise HTTPException(status_code=404, detail=f"Error updating {m_name}.")

    return(val_col)
# --------------------

# --------------------
def delete_item(id: int, db:Session=Depends(get_db)):
    ''' Description \n
    `` (): \n
    return `` (): \n
    '''

    try:
        db_item = Titem.delete_item(db, id)
    except Exception as exc:
        msg = f"Error {exc}"
        raise HTTPException(status_code=520, detail=msg)

    if (db_item is None):
        m_name = f"item data"
        raise HTTPException(status_code=404, detail=f"Error delete {m_name}.")

    return(db_item)
# --------------------