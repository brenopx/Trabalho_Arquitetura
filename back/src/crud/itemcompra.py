# Import system libs
from sqlalchemy.orm import Session

# Import custom libs
from .. import models
from ..itemcompra import schemas


class Titemcompra:

    # --------------------
    def get_itemcompra_all(db: Session):
        ''' Description \n
        `` (): \n
        return `` (): \n
        '''
        # Declare the query
        info = db.query(models.ItemCompra).all()

        return(info)
    # --------------------

    # --------------------
    def get_itemcompra_id(db: Session, id: int):
        ''' Description \n
        `` (): \n
        return `` (): \n
        '''
        # Declare the query
        dbq = db.query(models.ItemCompra)

        info =  dbq.filter(models.ItemCompra.id == id).first()

        return(info)
    # --------------------

    # --------------------
    def create_itemcompra(db: Session, new_itemcompra: schemas.ItemCompraCreate):
        ''' Description \n
        `` (): \n
        return `` (): \n
        '''
        db_ItemCompra = None
      
        db_ItemCompra = models.ItemCompra(
            quantidade = new_itemcompra.quantidade,
            id_compra = new_itemcompra.id_compra,
            id_item = new_itemcompra.id_item
        )

        # Insert in database
        db.add(db_ItemCompra)
        db.commit()
        db.refresh(db_ItemCompra)
        
        return(db_ItemCompra)       
    # --------------------

    # --------------------
    def update_itemcompra(db: Session, col_data: schemas.ItemCompra):
        ''' Description \n
        `` (): \n
        return `` (): \n
        '''
        
        db_col = Titemcompra.get_itemcompra_id(db, col_data.id)

        db_col.id = col_data.id
        db_col.quantidade = col_data.quantidade
        db_col.id_compra = col_data.id_compra
        db_col.id_item = col_data.id_item

        db.commit()

        return (db_col)
    # --------------------

    # --------------------
    def get_itemcompra_compra_all(db: Session, id_compra: int):
        ''' Description \n
        `` (): \n
        return `` (): \n
        '''
            # Declare the query
        dbq = db.query(models.ItemCompra)

        info =  dbq.filter(models.ItemCompra.id_compra == id_compra).all()

        return(info)
    # --------------------

    # --------------------
    def delete_itemcompra(db: Session, id: int):
        ''' Description \n
        `` (): \n
        return `` (): \n
        '''
        
        # Declare the query
        ds = Titemcompra.get_itemcompra_id(db, id)

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