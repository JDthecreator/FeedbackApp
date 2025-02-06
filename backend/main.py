from fastapi import FastAPI, HTTPException 
import snowflake.connector
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

    #Connect to Snowflake database
    conn = snowflake.connector.connect(
        user='JDthecreator',
        password='Maintain4me',
        account='KIB19333',
        warehouse='COMPUTE_WH',
        database='feedbackApp',
        schema='PUBLIC'
    )

    cursor = conn.cursor()
    try:
        #inserting data into feedback database

        cursor.execute(
            "INSERT INTO feedback(feedback, rating) VALUES (%s, %s)",
            (feedback.feedback, feedback.rating)
        )

        conn.commit()
        return {"message": "Feedback received successfully", "data": feedback}
    except Exception as e:
        raise HTTPException(status_code=500, detail="Error saving Feedback")
    finally:
        cursor.close()
        conn.close()

        
