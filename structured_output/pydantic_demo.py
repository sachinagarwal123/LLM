from pydantic import BaseModel,EmailStr,Field
from typing import Optional

class Student(BaseModel):
    name: str = 'sachin'
    age: Optional[int] = None
    email: EmailStr
    cgpa: float = Field(gt=0,lt=10)

new_student = {'name': 'sachin','email': 'abc@gmail.com'}

student = Student(**new_student)
print(student)