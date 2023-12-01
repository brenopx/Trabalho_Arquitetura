# Import system libs
from sqlalchemy.orm import Session

# Import custom libs
from .. import models
from ..item import schemas


class Titem:

    # --------------------
    def get_item_all(db: Session):
        ''' Description \n
        `` (): \n
        return `` (): \n
        '''
        # Declare the query
        info = db.query(models.Item).all()

        return(info)
    # --------------------

    # --------------------
    def get_item_id(db: Session, id: int):
        ''' Description \n
        `` (): \n
        return `` (): \n
        '''
        # Declare the query
        dbq = db.query(models.Item)

        info =  dbq.filter(models.Item.id == id).first()

        return(info)
    # --------------------

    # --------------------
    def create_item(db: Session, new_item: schemas.ItemCreate):
        ''' Description \n
        `` (): \n
        return `` (): \n
        '''
        db_item = None
      
        db_item = models.Item(
            nome=new_item.nome,
            tipo=new_item.tipo,
            marca=new_item.marca,
            tamanho=new_item.tamanho,
            cor=new_item.cor,
            quantidade=new_item.quantidade
        )

        # Insert in database
        db.add(db_item)
        db.commit()
        db.refresh(db_item)
        
        return(db_item)       
    # --------------------

    # --------------------
    def update_item(db: Session, col_data: schemas.Item):
        ''' Description \n
        `` (): \n
        return `` (): \n
        '''
        
        db_col = Titem.get_item_id(db, col_data.id)

        db_col.id = col_data.id
        db_col.nome=col_data.nome
        db_col.tipo=col_data.tipo
        db_col.marca=col_data.marca
        db_col.tamanho=col_data.tamanho
        db_col.cor=col_data.cor
        db_col.quantidade=col_data.quantidade

        db.commit()

        return (db_col)
    # --------------------

    # --------------------
    def delete_item(db: Session, id: int):
        ''' Description \n
        `` (): \n
        return `` (): \n
        '''
        
        # Declare the query
        ds = Titem.get_item_id(db, id)

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