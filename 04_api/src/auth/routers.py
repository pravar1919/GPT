from fastapi import APIRouter, Request
from starlette.status import HTTP_400_BAD_REQUEST


auth_router = APIRouter()

@auth_router.post("/save-user")
async def register_login(request: Request):
    data = await request.json()
    print(data)
    return "Success"