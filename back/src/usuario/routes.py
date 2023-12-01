# Import system libs
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session

# Import custom libs
from ..database import get_db
from . import schemas
from ..crud import Tusuario

#######################################

# --------------------
def get_usuario_all(db:Session=Depends(get_db)):
    ''' Description \n
    `` (): \n
    return `` (): \n
    '''
    
    val_usuario = Tusuario.get_usuario_all(db)

    if (val_usuario is None):
        raise HTTPException(
            status_code=404, 
            detail=f"Error searching for available."
        )

    return(val_usuario)
# --------------------

# --------------------
def get_usuario_id(id: int, db:Session=Depends(get_db)):
    ''' Description \n
    `` (): \n
    return `` (): \n
    '''
    
    val_usuario = Tusuario.get_usuario_id(db, id)

    if (val_usuario is None):
        raise HTTPException(
            status_code=404, 
            detail=f"Error searching for available."
    )

    return(val_usuario)
# --------------------

# --------------------
def create_usuario(new_usuario:schemas.UsuarioCreate, db:Session=Depends(get_db)):
    ''' Description \n
    `` (): \n
    return `` (): \n
    '''

    try:
        db_usuario = Tusuario.create_usuario(db, new_usuario)
    except Exception as exc:
        msg = f"Error {exc}"
        print(msg)
        raise HTTPException(status_code=520, detail=msg)

    if (db_usuario is None):
        m_name = f"usuario data"
        raise HTTPException(status_code=404, detail=f"Error creating {m_name}.")

    return(db_usuario)
# --------------------

# --------------------
def update_usuario(update_usuario:schemas.Usuario, db:Session=Depends(get_db)):
    ''' Description \n
    `` (): \n
    return `` (): \n
    '''

    val_col = Tusuario.update_usuario(db, update_usuario)

    if (val_col is None):
        m_name = f"usuario data"
        raise HTTPException(status_code=404, detail=f"Error updating {m_name}.")

    return(val_col)
# --------------------

# --------------------
def get_usuario_endereco(id_usuario: int, db:Session=Depends(get_db) ):
    ''' Description \n
    `` (): \n
    return `` (): \n
    '''
    val_col = Tusuario.get_usuario_endereco(db, id_usuario)

    if (val_col is None):
        m_name = f"compras data"
        raise HTTPException(status_code=404, detail=f"Error updating {m_name}.")

    return(val_col)
# --------------------

# --------------------
def get_usuario_compras(id_usuario: int, db:Session=Depends(get_db) ):
    ''' Description \n
    `` (): \n
    return `` (): \n
    '''
    val_col = Tusuario.get_usuario_compras(db, id_usuario)

    if (val_col is None):
        m_name = f"compras data"
        raise HTTPException(status_code=404, detail=f"Error updating {m_name}.")

    return(val_col)
# --------------------

# --------------------
def delete_usuario(id: int, db:Session=Depends(get_db)):
    ''' Description \n
    `` (): \n
    return `` (): \n
    '''

    try:
        db_usuario = Tusuario.delete_usuario(db, id)
    except Exception as exc:
        msg = f"Error {exc}"
        raise HTTPException(status_code=520, detail=msg)

    if (db_usuario is None):
        m_name = f"usuario data"
        raise HTTPException(status_code=404, detail=f"Error delete {m_name}.")

    return(db_usuario)
# --------------------