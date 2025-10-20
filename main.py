from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI(title="People Info API")

# Define the data model for one person
class Person(BaseModel):
    name: str
    age: int
    phone: str

# Define a request model containing 5 people
class PeopleRequest(BaseModel):
    people: List[Person]

@app.post("/people")
def collect_people(data: PeopleRequest):
    messages = []
    for person in data.people:
        message = f"Hi {person.name}, you are {person.age} years old and your phone number is {person.phone}."
        messages.append(message)
    return {"messages": messages}
