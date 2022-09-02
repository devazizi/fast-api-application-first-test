from fastapi import APIRouter

home_router = APIRouter(tags=['Home'])


@home_router.get('/', status_code=401)
def home_api():
    return {'status': 'unauthorized action'}
