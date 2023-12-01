# Import system libs
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session

# Import custom libs
from ..database import get_db
from . import schemas
from ..crud import Tendereco

#######################################

# --------------------
def get_endereco_all(db:Session=Depends(get_db)):
    ''' Description \n
    `` (): \n
    return `` (): \n
    '''
    
    val_endereco = Tendereco.get_endereco_all(db)

    if (val_endereco is None):
        raise HTTPException(
            status_code=404, 
            detail=f"Error searching for available."
        )

    return(val_endereco)
# --------------------

# --------------------
def get_endereco_id(id: int, db:Session=Depends(get_db)):
    ''' Description \n
    `` (): \n
    return `` (): \n
    '''
    
    val_endereco = Tendereco.get_endereco_id(db, id)

    if (val_endereco is None):
        raise HTTPException(
            status_code=404, 
            detail=f"Error searching for available."
    )

    return(val_endereco)
# --------------------

# --------------------
def create_endereco(new_endereco:schemas.EnderecoCreate, db:Session=Depends(get_db)):
    ''' Description \n
    `` (): \n
    return `` (): \n
    '''

    try:
        db_endereco = Tendereco.create_endereco(db, new_endereco)
    except Exception as exc:
        msg = f"Error {exc}"
        print(msg)
        raise HTTPException(status_code=520, detail=msg)

    if (db_endereco is None):
        m_name = f"endereco data"
        raise HTTPException(status_code=404, detail=f"Error creating {m_name}.")

    return(db_endereco)
# --------------------

# --------------------
def update_endereco(update_endereco:schemas.Endereco, db:Session=Depends(get_db)):
    ''' Description \n
    `` (): \n
    return `` (): \n
    '''

    val_col = Tendereco.update_endereco(db, update_endereco)

    if (val_col is None):
        m_name = f"endereco data"
        raise HTTPException(status_code=404, detail=f"Error updating {m_name}.")

    return(val_col)
# --------------------

# --------------------
def delete_endereco(id: int, db:Session=Depends(get_db)):
    ''' Description \n
    `` (): \n
    return `` (): \n
    '''

    try:
        db_endereco = Tendereco.delete_endereco(db, id)
    except Exception as exc:
        msg = f"Error {exc}"
        raise HTTPException(status_code=520, detail=msg)

    if (db_endereco is None):
        m_name = f"endereco data"
        raise HTTPException(status_code=404, detail=f"Error delete {m_name}.")

    return(db_endereco)
# --------------------