from typing import Union
from fastapi import FastAPI, status, Response
from pydantic import BaseModel
from dbTools import Person, addParticipant, showStatistics
from dotenv import load_dotenv
import os


load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")


app = FastAPI()


@app.post("/send_person_data", status_code=status.HTTP_200_OK)
async def handelPersonData(person: Person, response: Response):
    try:
        addParticipant(person=person)
        response.status_code = status.HTTP_201_CREATED
        return {"person": person}
    except:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {"bad":"reauest"}
        


@app.get("/statistics/{SECRET_KEY_URL}", status_code=status.HTTP_200_OK)
def get_statistics(SECRET_KEY_URL: str, response:Response):
    if SECRET_KEY == SECRET_KEY_URL:
        
        participants = showStatistics()

        return {
            "participants":participants
        }
    else:
        response.status_code = status.HTTP_401_UNAUTHORIZED
        return {"bad":"reauest"}