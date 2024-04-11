import sqlite3
from pydantic import BaseModel
from datetime import datetime


class Person(BaseModel):
    sex: str
    age:  int
    status: str
    town: str
    czn: str


#функция для создания базы данных
def createDb() -> None:
    connection = sqlite3.connect("participants.db")

    cursor = connection.cursor()

    cursor.execute('''
        CREATE TABLE Participants (
            p_id INTEGER PRIMARY KEY AUTOINCREMENT,
            p_sex TEXT NOT NULL,
            p_age INTEGER NOT NULL,
            p_status TEXT NOT NULL,
            p_town TEXT NOT NULL,
            p_czn TEXT NOT NULL,
            p_date_enter TEXT NOT NULL                    
        )
    ''')

    connection.commit()

    connection.close()


#функция для добавления участника в баззу данных участников
def addParticipant(person: Person) -> None:
    connection = sqlite3.connect("participants.db")

    cursor = connection.cursor()

    nowTime = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")

    cursor.execute('''INSERT INTO Participants (p_sex,p_age,p_status,p_town,p_czn,p_date_enter) values (?,?,?,?,?,?)''',(
        person.sex,
        person.age,
        person.status,
        person.town,
        person.czn,
        nowTime
    ))

    connection.commit()

    connection.close()


#фукнция для отображения данных в базе данных
def showStatistics() -> list:

    participantsList = []
    connnection = sqlite3.connect("participants.db")

    cursor = connnection.cursor()

    cursor.execute('''SELECT * FROM Participants''')

    participants = cursor.fetchall()

    for p in participants:
        participantsList.append({
            "id": p[0],
            "sex": p[1],
            "age": p[2],
            "status": p[3],
            "town": p[4],
            "czn": p[5],
            "date_enter": p[6]
        })

    return participantsList