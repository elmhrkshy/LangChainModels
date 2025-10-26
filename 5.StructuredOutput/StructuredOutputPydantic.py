# If you name this file as pydantic.py
# It will cause a circular dependency, as we also trying to import pydantic
# Which basically means we are trying to add pydantic to pydantic

from pydantic import BaseModel
from typing import Optional

class Student(BaseModel):
    Name: str
    age: Optional[int] = None

new_student = {'Name': 'Akshay Mehra', 'age': 30}
#new_student2 = {'Name': '30'}
#new_student3 = {'Name': 30}

student = Student(**new_student)
#student2 = Student(**new_student2)
#student3 = Student(**new_student3)

print(student)
#print(new_student)
#print(type(new_student))
#print(type(student))
#print(new_student)
#print(new_student2)
#print(new_student3)
