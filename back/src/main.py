from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from typing import List

# Import custom libs
from . import database
from .database import engine

from .compras import routes as compras_routes
from .compras import schemas as compras_schemas

from .item import routes as item_routes
from .item import schemas as item_schemas

from .itemcompra import routes as itemcompra_routes
from .itemcompra import schemas as itemcompra_schemas

from .usuario import routes as usuario_routes
from .usuario import schemas as usuario_schemas

from .endereco import routes as endereco_routes
from .endereco import schemas as endereco_schemas

database.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Application Routes

### usuario
app.add_api_route("/create_usuario",
    methods=["POST"], 
    response_model=usuario_schemas.Usuario,
    endpoint=usuario_routes.create_usuario)

app.add_api_route("/get_usuario_id/{id}",
    methods=["GET"], 
    response_model=usuario_schemas.Usuario,
    endpoint=usuario_routes.get_usuario_id)

app.add_api_route("/get_usuario_all",
    methods=["GET"], 
    response_model=List[usuario_schemas.Usuario],
    endpoint=usuario_routes.get_usuario_all)

app.add_api_route("/get_usuario_endereco",
    methods=["GET"], 
    response_model=List[endereco_schemas.Endereco],
    endpoint=usuario_routes.get_usuario_endereco)

app.add_api_route("/get_usuario_compras",
    methods=["GET"], 
    response_model=List[compras_schemas.Compras],
    endpoint=usuario_routes.get_usuario_compras)

app.add_api_route("/update_usuario",
    methods=["PUT"], 
    response_model=usuario_schemas.Usuario,
    endpoint=usuario_routes.update_usuario)

app.add_api_route("/delete_usuario/{id}",
    methods=["DELETE"], 
    response_model=bool,
    endpoint=usuario_routes.delete_usuario)

### endereco
app.add_api_route("/create_endereco",
    methods=["POST"], 
    response_model=endereco_schemas.Endereco,
    endpoint=endereco_routes.create_endereco)

app.add_api_route("/get_endereco_id/{id}",
    methods=["GET"], 
    response_model=endereco_schemas.Endereco,
    endpoint=endereco_routes.get_endereco_id)

app.add_api_route("/get_endereco_all",
    methods=["GET"], 
    response_model=List[endereco_schemas.Endereco],
    endpoint=endereco_routes.get_endereco_all)

app.add_api_route("/update_endereco",
    methods=["PUT"], 
    response_model=endereco_schemas.Endereco,
    endpoint=endereco_routes.update_endereco)

app.add_api_route("/delete_endereco/{id}",
    methods=["DELETE"], 
    response_model=bool,
    endpoint=endereco_routes.delete_endereco)

### Compras
app.add_api_route("/create_compras",
    methods=["POST"], 
    response_model=compras_schemas.Compras,
    endpoint=compras_routes.create_compras)

app.add_api_route("/get_compras_id/{id}",
    methods=["GET"], 
    response_model=compras_schemas.Compras,
    endpoint=compras_routes.get_compras_id)

app.add_api_route("/get_compras_all",
    methods=["GET"], 
    response_model=List[compras_schemas.Compras],
    endpoint=compras_routes.get_compras_all)

app.add_api_route("/update_compras",
    methods=["PUT"], 
    response_model=compras_schemas.Compras,
    endpoint=compras_routes.update_compras)

app.add_api_route("/compra_autorizada",
    methods=["PUT"], 
    response_model=None,
    endpoint=compras_routes.compra_autorizada)

app.add_api_route("/delete_compras/{id}",
    methods=["DELETE"], 
    response_model=bool,
    endpoint=compras_routes.delete_compras)

### item
app.add_api_route("/create_item",
    methods=["POST"], 
    response_model=item_schemas.Item,
    endpoint=item_routes.create_item)

app.add_api_route("/get_item_id/{id}",
    methods=["GET"], 
    response_model=item_schemas.Item,
    endpoint=item_routes.get_item_id)

app.add_api_route("/get_item_all",
    methods=["GET"], 
    response_model=List[item_schemas.Item],
    endpoint=item_routes.get_item_all)

app.add_api_route("/update_item",
    methods=["PUT"], 
    response_model=item_schemas.Item,
    endpoint=item_routes.update_item)

app.add_api_route("/delete_item/{id}",
    methods=["DELETE"], 
    response_model=bool,
    endpoint=item_routes.delete_item)

### itemcompra
app.add_api_route("/create_itemcompra",
    methods=["POST"], 
    response_model=itemcompra_schemas.ItemCompra,
    endpoint=itemcompra_routes.create_itemcompra)

app.add_api_route("/get_itemcompra_id/{id}",
    methods=["GET"], 
    response_model=itemcompra_schemas.ItemCompra,
    endpoint=itemcompra_routes.get_itemcompra_id)

app.add_api_route("/get_itemcompra_all",
    methods=["GET"], 
    response_model=List[itemcompra_schemas.ItemCompra],
    endpoint=itemcompra_routes.get_itemcompra_all)

app.add_api_route("/get_itemcompra_compra_all",
    methods=["GET"], 
    response_model=List[itemcompra_schemas.ItemCompra],
    endpoint=itemcompra_routes.get_itemcompra_compra_all)

app.add_api_route("/update_itemcompra",
    methods=["PUT"], 
    response_model=itemcompra_schemas.ItemCompra,
    endpoint=itemcompra_routes.update_itemcompra)

app.add_api_route("/delete_itemcompra/{id}",
    methods=["DELETE"], 
    response_model=bool,
    endpoint=itemcompra_routes.delete_itemcompra)
