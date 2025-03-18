from fastapi import FastAPI, HTTPException
from models import Todo
from database import collection
from bson import ObjectId

app = FastAPI()

# Helper to convert MongoDB _id to string
def todo_serializer(todo) -> dict:
    return {
        "id": str(todo["_id"]),
        "title": todo["title"],
        "description": todo["description"],
        "completed": todo["completed"]
    }

# Create a to-do
@app.post("/todos/", response_model=dict)
async def create_todo(todo: Todo):
    result = await collection.insert_one(todo.dict())
    new_todo = await collection.find_one({"_id": result.inserted_id})
    return todo_serializer(new_todo)

# Read all to-dos
@app.get("/todos/", response_model=list[dict])
async def get_todos():
    todos = []
    async for todo in collection.find():
        todos.append(todo_serializer(todo))
    return todos

# Update a to-do
@app.put("/todos/{id}", response_model=dict)
async def update_todo(id: str, todo: Todo):
    result = await collection.update_one(
        {"_id": ObjectId(id)}, {"$set": todo.dict()}
    )
    if result.modified_count == 0:
        raise HTTPException(status_code=404, detail="Todo not found")
    updated_todo = await collection.find_one({"_id": ObjectId(id)})
    return todo_serializer(updated_todo)

# Delete a to-do
@app.delete("/todos/{id}")
async def delete_todo(id: str):
    result = await collection.delete_one({"_id": ObjectId(id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Todo not found")
    return {"message": "Todo deleted"}