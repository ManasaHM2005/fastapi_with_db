from pydantic import BaseModel

class UserSchemas(BaseModel):
    email: str
    password: str