#scripts/schema/init
from pydantic import BaseModel


class StudentDatabase(BaseModel):
    name: str
    age: int
    course: str