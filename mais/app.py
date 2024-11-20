from http import HTTPStatus

from fastapi import FastAPI

from mais.routers import users
from mais.schemas import Message

app = FastAPI()

app.include_router(users.router)


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def hello():
    return Message(message='Hello World')
