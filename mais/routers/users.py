from http import HTTPStatus

from fastapi import APIRouter

from mais.schemas import UseDatabase, UserPublic, UserSchema

router = APIRouter(prefix='/users', tags=['users'])


@router.post('/', status_code=HTTPStatus.CREATED, response_model=UserPublic)
def create_user(user: UserSchema):
    return UseDatabase(**user.model_dump(), id=1)
