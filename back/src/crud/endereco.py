# Import system libs
from sqlalchemy.orm import Session

# Import custom libs
from .. import models
from ..endereco import schemas


class Tendereco:

    # --------------------
    def get_endereco_all(db: Session):
        ''' Description \n
        `` (): \n
        return `` (): \n
        '''
        # Declare the query
        info = db.query(models.Endereco).all()

        return(info)
    # --------------------

    # --------------------
    def get_endereco_id(db: Session, id: int):
        ''' Description \n
        `` (): \n
        return `` (): \n
        '''
        # Declare the query
        dbq = db.query(models.Endereco)

        info =  dbq.filter(models.Endereco.id == id).first()

        return(info)
    # --------------------

    # --------------------
    def create_endereco(db: Session, new_endereco: schemas.EnderecoCreate):
        ''' Description \n
        `` (): \n
        return `` (): \n
        '''
        db_endereco = None
      
        db_endereco = models.Endereco(
            endereco=new_endereco.endereco,
            numero=new_endereco.numero,
            complemento=new_endereco.complemento,
            estado=new_endereco.estado,
            pais=new_endereco.pais,
            id_usuario=new_endereco.id_usuario
        )

        # Insert in database
        db.add(db_endereco)
        db.commit()
        db.refresh(db_endereco)
        
        return(db_endereco)       
    # --------------------

    # --------------------
    def update_endereco(db: Session, col_data: schemas.Endereco):
        ''' Description \n
        `` (): \n
        return `` (): \n
        '''
        
        db_col = Tendereco.get_endereco_id(db, col_data.id)

        db_col.id = col_data.id
        db_col.endereco=col_data.endereco
        db_col.numero=col_data.numero
        db_col.complemento=col_data.complemento
        db_col.estado=col_data.estado
        db_col.pais=col_data.pais
        db_col.id_usuario=col_data.id_usuario

        db.commit()

        return (db_col)
    # --------------------

    # --------------------
    def delete_endereco(db: Session, id: int):
        ''' Description \n
        `` (): \n
        return `` (): \n
        '''
        
        # Declare the query
        ds = Tendereco.get_endereco_id(db, id)

        if (ds is not None):
            # Remove from database
            db.delete(ds)
            db.commit()
            # Parse data
            ds_answer = True
        else:
            ds_answer = False
        
        return (ds_answer)
    # --------------------