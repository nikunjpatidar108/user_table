from fastapi import APIRouter
# import sys
# sys.path.append('../../')
from configs.dbs import conn
from models.index import users
from schemas.index import User

user = APIRouter()


@user.get("/")
async def read_data():
    return conn.execute(users.select()).fetchall


@user.get("/{id}")
async def read_data(id: int):
    return conn.execute(users.select().where(users.c.id == id)).fetchall


@user.post("/")
async def write_data(user: User):
    conn.execute(users.insert().values(
        id=user.id,
        name=user.name,
        email=user.email,
        password=user.password

    ))
    return conn.execute(users.select()).fetchall


@user.put(f"/{id}")
async def update_data(id: int, user: User):
    conn.execute(users.update(
        name=user.name,
        email=user.email,
        password=user.password

    ).where(users.c.id == id))
    return conn.execute(users.select()).fetchall


@user.delete(f"/{id}")
async def delete_data(id: int):
    conn.execute(users.delete().where(users.c.id == id))
    return conn.execute(users.select()).fetchall
