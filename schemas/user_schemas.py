from pydantic import BaseModel

class userSchemas(BaseModel):
    email: str
    password: str