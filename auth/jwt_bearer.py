from fastapi import Request, HTTPException
from fastapi.security import OAuth2PasswordBearer
from typing import Callable

class JWTBearer(OAuth2PasswordBearer):
    def __init__(self, tokenUrl: str = "/token"):
        super().__init__(tokenUrl=tokenUrl)
        print("JWTBearer initialized with token URL:", tokenUrl)

    def __call__(self, request: Request):
        token = request.headers.get("Authorization")
        if token is None:
            print("Authorization header missing")
            raise HTTPException(status_code=403, detail="Not authenticated")
        if not self.validate_token(token):
            print("Invalid token")
            raise HTTPException(status_code=403, detail="Invalid token")
        print("Token validated successfully")
        return token

    def validate_token(self, token: str) -> bool:
        print("Validating token:", token)
        return True  
