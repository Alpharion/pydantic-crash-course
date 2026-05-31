from pydantic import BaseModel, ConfigDict, Field, field_validator, BaseSettings
from typing import Optional
from typing import Literal

class User(BaseModel):
    id: int
    email: str
    age: int
    
name : str = "alpha" # kind of like castings, but is jus documentation


def create_user(name: str, email: str, age: int) -> dict:
    user_dict = {"name": name, "email": email, "age": age}
    return user_dict

middle_name: Optional[str] = None
middle_name: str | None = None

status: Literal["draft", "submitted", "archived"] = "draft" # value must be one of the values listed

user = User(id=1, email="@gmail", age=22)
user_dict = user.model_dump() #model_dump_json(), enclose the dict in strings

print(user_dict)

'''
    Unpacking data = {"name": val, "email": "test@", "age": 1}
    user = User(**data) , simple data unpacking
    OR
    user = User.model_validate(data) 
    
'''

def greet_user(user: User) -> str:
    return f"Hello {user.name}"

def load_user(data: dict) -> User:
    return User.model_validate(data)

class StrictUser(BaseModel):
    model_config = ConfigDict(strict=True)
     
    name: str
    age: int
    
# defers coercion, where Strings can be auto converted to int for example

class UserField(BaseModel):
    
    name: str = Field(min_length=1, max_length=100)
    age: int = Field(gt=0, le=120) # greater than, lesser than or equal to
    email: str
    username: str
    
    @field_validator("username")
    def validate_username(cls, v): # class thats being worked on (not instantiated yet) and value v
        if " " in v:
            raise ValueError("Username cannot have spaces")
        return v.loser() # normalize to lowercase
    
# pattern matching for str w regex for Field(pattern=""), add description field for documentation

# User.model_json_schema()

class Settings(BaseSettings):
    api_key: str
    max_connections: int = 100
    debug: bool = False
    
 
    
