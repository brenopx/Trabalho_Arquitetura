# Import system libs
from sqlalchemy.orm import Session

# Import custom libs
from .. import models
from ..usuario import schemas

class Tusuario:

    # --------------------
    def get_usuario_all(db: Session):
        ''' Description \n
        `` (): \n
        return `` (): \n
        '''
        # Declare the query
        info = db.query(models.Usuario).all()

        return(info)
    # --------------------

    # --------------------
    def get_usuario_id(db: Session, id: int):
        ''' Description \n
        `` (): \n
        return `` (): \n
        '''
        # Declare the query
        dbq = db.query(models.Usuario)

        info =  dbq.filter(models.Usuario.id == id).first()

        return(info)
    # --------------------

    # --------------------
    def create_usuario(db: Session, new_Usuario: schemas.UsuarioCreate):
        ''' Description \n
        `` (): \n
        return `` (): \n
        '''
        db_Usuario = None
      
        db_Usuario = models.Usuario(
            nome=new_Usuario.nome,
            cpf=new_Usuario.cpf,
            email=new_Usuario.email,
            idade=new_Usuario.idade
        )

        # Insert in database
        db.add(db_Usuario)
        db.commit()
        db.refresh(db_Usuario)
        
        return(db_Usuario)       
    # --------------------

    # --------------------
    def update_usuario(db: Session, col_data: schemas.Usuario):
        ''' Description \n
        `` (): \n
        return `` (): \n
        '''
        
        db_col = Tusuario.get_usuario_id(db, col_data.id)

        db_col.id = col_data.id
        db_col.nome= col_data.nome
        db_col.cpf= col_data.cpf
        db_col.email= col_data.email
        db_col.idade= col_data.idade

        db.commit()

        return (db_col)
    # --------------------

    # --------------------
    def delete_usuario(db: Session, id: int):
        ''' Description \n
        `` (): \n
        return `` (): \n
        '''
        
        # Declare the query
        ds = Tusuario.get_usuario_id(db, id)

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

    # --------------------
    def get_usuario_endereco(db: Session, id_usuario: int):
        ''' Description \n
        `` (): \n
        return `` (): \n
        '''
        # Declare the query
        dbq = db.query(models.Endereco)

        info =  dbq.filter(models.Endereco.id_usuario == id_usuario).all()
        
        return(info)
    # --------------------

    # --------------------
    def get_usuario_compras(db: Session, id_usuario: int):
        ''' Description \n
        `` (): \n
        return `` (): \n
        '''
        # Declare the query
        dbq = db.query(models.Compras)

        info =  dbq.filter(models.Compras.id_usuario == id_usuario).all()

        return(info)
    # --------------------