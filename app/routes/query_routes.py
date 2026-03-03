from fastapi import APIRouter
from app.controllers.query_controller import query_controller
from app.models.query_model import Query

router = APIRouter(prefix="/queries", tags=["Queries"])

# CREATE
@router.post("/create_query")
def create_query(query: Query):
    return query_controller.create_query(query)

# GET ONE
@router.get("/get_query/{id_query}", response_model=Query)
def get_query(id_query: int):
    return query_controller.get_query(id_query)

# GET ALL
@router.get("/get_queries/")
def get_queries():
    return query_controller.get_queries()

# UPDATE
@router.put("/{id_query}")
def update_query(id_query: int, query: Query):
    return query_controller.update_query(id_query, query)

# DELETE
@router.delete("/{id_query}")
def delete_query(id_query: int):
    return query_controller.delete_query(id_query)