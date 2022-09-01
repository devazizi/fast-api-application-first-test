from fastapi import APIRouter
from src.models.auth import LoginRequest
from src.infrastructure.db import session
from src.models.user import User

router = APIRouter(
    prefix="/api/v1/auth",
    tags=["Auth"],
    responses={404: {"description": "Not found"}},
)


@router.post('/login')
def login(login_request: LoginRequest):
    user = User()
    user.name = "reza"
    user.national_code = '0132523432'
    user.email = 'devz.azizail@gmail.com'
    user.cell_number = '09914324584'

    session.add(user)
    session.commit()

    response = session.query(User).all()
    data = list()
    for row in response:
        data.append({
            'id': row.id,
            'name': row.name,
            'email': row.email,
            'national_code': row.national_code,
        })
    return {
        "description": "Ok",
        'data': data
    }