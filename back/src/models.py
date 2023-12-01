from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base

class Usuario(Base):
    __tablename__ = "usuario"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    cpf = Column(Integer)
    email = Column(String)
    idade = Column(Integer)

    # Other tables
    endereco = relationship("Endereco", back_populates="usuario")
    compras = relationship("Compras", back_populates="usuario")


class Endereco(Base):
    __tablename__ = "endereco"

    id = Column(Integer, primary_key=True, index=True)
    endereco = Column(String)
    numero = Column(Integer)
    complemento = Column(String)
    estado = Column(String)
    pais = Column(String)

    # Other tables
    usuario = relationship("Usuario", back_populates="endereco")
    id_usuario = Column(Integer, ForeignKey("usuario.id"))


class Item(Base):
    __tablename__ = "item"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    tipo = Column(String)
    marca = Column(String)
    tamanho = Column(String)
    cor = Column(String)
    quantidade = Column(Integer)

    # Other tables
    itemcompra = relationship("ItemCompra", back_populates="item")


class Compras(Base):
    __tablename__ = "compras"

    id = Column(Integer, primary_key=True, index=True)
    data = Column(String)
    pago = Column(Boolean)
    estado_compra = Column(String)

    # Other tables
    usuario = relationship("Usuario", back_populates="compras")
    id_usuario = Column(Integer, ForeignKey("usuario.id"))

    itemcompra = relationship("ItemCompra", back_populates="compras")

class ItemCompra(Base):
    __tablename__ = "itemcompra"

    id = Column(Integer, primary_key=True, index=True)
    quantidade = Column(Integer)
    
    # Other tables
    compras = relationship("Compras", back_populates="itemcompra")
    id_compra = Column(Integer, ForeignKey("compras.id"))
    
    item = relationship("Item", back_populates="itemcompra")
    id_item = Column(Integer, ForeignKey("item.id"))
    