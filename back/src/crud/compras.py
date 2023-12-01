# Import system libs
from sqlalchemy.orm import Session
import datetime as _dt

# Import custom libs
from .. import models
from ..compras import schemas
from .item import Titem
from .itemcompra import Titemcompra

class Tcompras:

    # --------------------
    def get_date_today(hours:bool=False, minutes:bool=False):
        '''Calculates the current date.\n
        `hours` (bool): if true, returns date with time .\n
        return `result` (str): string with current unformed 
        date "%Y-%m-%d" by default.\n
        '''

        difference = _dt.timedelta(hours=-3)

        zone = _dt.timezone(difference)

        date = _dt.datetime.today()

        date = date.astimezone(zone)

        if (minutes):
            date_calculate = date.strftime("%Y-%m-%d %H:%M:%S")
        elif (hours):
            date_calculate = date.strftime("%Y-%m-%d %H:%M")
        else:
            date_calculate = date.strftime("%Y-%m-%d")

        return(date_calculate)
    # --------------------

    # --------------------
    def get_compras_all(db: Session):
        ''' Description \n
        `` (): \n
        return `` (): \n
        '''
        # Declare the query
        info = db.query(models.Compras).all()

        return(info)
    # --------------------

    # --------------------
    def get_compras_id(db: Session, id: int):
        ''' Description \n
        `` (): \n
        return `` (): \n
        '''
        # Declare the query
        dbq = db.query(models.Compras)

        info =  dbq.filter(models.Compras.id == id).first()

        return(info)
    # --------------------

    # --------------------
    def create_compras(db: Session, new_compras: schemas.ComprasCreate):
        ''' Description \n
        `` (): \n
        return `` (): \n
        '''
        db_compras = None
      
        db_compras = models.Compras(
            data = Tcompras.get_date_today(minutes=True),
            pago = new_compras.pago,
            estado_compra = new_compras.estado_compra,
            id_usuario = new_compras.id_usuario,
        )

        # Insert in database
        db.add(db_compras)
        db.commit()
        db.refresh(db_compras)
        
        return(db_compras)       
    # --------------------

    # --------------------
    def update_compras(db: Session, col_data: schemas.ComprasUpdate):
        ''' Description \n
        `` (): \n
        return `` (): \n
        '''
        print("valor de col_data", col_data)
        db_col = Tcompras.get_compras_id(db, col_data.id)

        db_col.id = col_data.id
        db_col.data = Tcompras.get_date_today(minutes=True)
        db_col.pago = col_data.pago
        db_col.estado_compra = col_data.estado_compra
        db_col.id_usuario = col_data.id_usuario

        db.commit()

        return (db_col)
    # --------------------

    # --------------------
    def compra_autorizada(db: Session, id_compra:int):
        ''' Description \n
        `` (): \n
        return `` (): \n
        '''
        compra_autorizada = Tcompras.get_compras_id(db, id_compra)
        if(compra_autorizada.pago == True):
            return("Esse compra já foi contada")
        else:        
            compra_autorizada.pago = True
            Tcompras.update_compras(db, compra_autorizada)

        lista_de_items = Titemcompra.get_itemcompra_compra_all(db, id_compra)

        for item in lista_de_items:
            estoque_item = Titem.get_item_id(db, item.id_item)
            estoque_item.quantidade = estoque_item.quantidade - item.quantidade
            Titem.update_item(db, estoque_item)
        
        return(compra_autorizada)
    # --------------------

    # --------------------
    def delete_compras(db: Session, id: int):
        ''' Description \n
        `` (): \n
        return `` (): \n
        '''
        
        # Declare the query
        ds = Tcompras.get_compras_id(db, id)

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
