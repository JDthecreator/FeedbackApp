from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Define the data model
class Feedback(BaseModel):
    first_name: str
    last_name: str

# Endpoint to handle form submission
@app.post("/submit-feedback/")
async def submit_feedback(feedback: Feedback):
    # Simulate storing feedback or processing it
    # For now, just return a success response with the data
    return {"message": "Feedback received successfully", "data": feedback}
