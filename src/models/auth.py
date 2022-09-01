from pydantic import BaseModel, Field
# from typing import Optional


class LoginRequest(BaseModel):
    email: str
    password: str
