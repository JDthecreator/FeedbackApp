from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Define the data model
class Feedback(BaseModel):
    feedback: str
    rating: int

# Endpoint to handle form submission
@app.post("/submit-feedback/")
async def submit_feedback(feedback: Feedback):
    # Simulate storing feedback or processing it
    # For now, just return a success response with the data
    return {"message": "Feedback received successfully", "data": feedback}
