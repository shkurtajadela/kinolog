import sqlite3 as sq
from datetime import datetime


def db_start():
    global db, cur

    db = sq.connect('bot_db.db')
    cur = db.cursor()

    cur.execute("CREATE TABLE IF NOT EXISTS Kinolog(kinolog_id INTEGER PRIMARY KEY AUTOINCREMENT, chat_id INTEGER, name TEXT, surname TEXT, "
                "patronymic TEXT, birthday TEXT, email TEXT, education TEXT, other_education TEXT, communities TEXT,"
                "practice_date TEXT, online_work TEXT, supervised TEXT, other_interests TEXT, kinolog_site TEXT,"
                "motivation TEXT, work_stages TEXT, dog_teaching TEXT, influenced_by TEXT, punishment TEXT, "
                "punishment_effect TEXT, ammunition TEXT, other_activities TEXT, work_methods TEXT, "
                "choice_importance TEXT, training_situation TEXT, advise TEXT, video TEXT, form_status TEXT)")
    cur.execute("CREATE TABLE IF NOT EXISTS Dog(dog_id INTEGER PRIMARY KEY AUTOINCREMENT, chat_id INTEGER, problem TEXT, age INTEGER, "
                "breed TEXT, weight INTEGER, origin TEXT, living_together TEXT, diseases TEXT)")
    cur.execute("CREATE TABLE IF NOT EXISTS Consultation(consult_id INTEGER PRIMARY KEY AUTOINCREMENT, "
                "kinolog_id INTEGER, dog_id INTEGER, consult_status INTEGER, consult_date datetime, consult_sum TEXT, "
                " FOREIGN KEY (kinolog_id) REFERENCES Kinolog(kinolog_id), "
                "FOREIGN KEY (dog_id) REFERENCES Dog(dog_id))")
    db.commit()


def new_kinolog(chat_id: int, name: str, surname: str, patronymic: str, birthday: str, email: str,
                education: str, other_education: str, communities: str, practice_date: str, online_work: str,
                supervised: str, other_interests: str, kinolog_site: str, motivation: str, work_stages: str,
                dog_teaching: str, influenced_by: str, punishment: str, punishment_effect: str, ammunition: str,
                other_activities: str, work_methods: str, choice_importance: str, training_situation: str, advise: str):
    cur.execute("INSERT INTO Kinolog VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                (None, chat_id, name, surname, patronymic, birthday, email, education, other_education, communities,
                 practice_date, online_work, supervised, other_interests, kinolog_site, motivation, work_stages,
                 dog_teaching, influenced_by, punishment, punishment_effect, ammunition, other_activities,
                 work_methods, choice_importance, training_situation, advise, '', 'form'))

    db.commit()


def new_dog(chat_id: int, problem: str, age:str, breed: str, weight: int, origin: str, living_together: str,
            diseases: str):
    cur.execute("INSERT INTO Dog VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)",
                (None, chat_id, problem, age, breed, weight, origin, living_together, diseases))

    db.commit()


def update_video(kinolog_id: int, video: str):
    cur.execute(f"UPDATE Kinolog SET video = '{video}' WHERE kinolog_id == '{kinolog_id}'")
    db.commit()


def get_consults_by_kinolog(kinolog_id: int):
    value = cur.execute(f"SELECT * FROM Consultation WHERE kinolog_id == {kinolog_id}").fetchall()
    return value


def get_kinolog(kinolog_id: int):
    value = cur.execute(f"SELECT * FROM Kinolog WHERE kinolog_id == '{kinolog_id}'").fetchone()
    return value


def get_dog(dog_id: int):
    value = cur.execute(f"SELECT * FROM Dog WHERE dog_id == '{dog_id}'").fetchone()
    return value


def new_consul_empty(kinolog_id: int, consult_date: datetime):
    cur.execute("INSERT INTO Consultation VALUES(?, ?, ?, ?, ?, ?)",
                (None, kinolog_id, 0, 0, consult_date, 0))

    db.commit()

def update_consul_dog_id(consult_id: int, dog_id: int, consult_status: int):
    cur.execute(f"UPDATE Consultation SET dog_id = '{dog_id}' AND consult_status = '{consult_status}' WHERE consult_id == '{consult_id}'")
    db.commit()

def update_consul_sum(consult_id: int, consult_sum: int, consult_status: int):
    cur.execute(f"UPDATE Consultation SET consult_sum = '{consult_sum}'AND consult_status = '{consult_status}' WHERE consult_id == '{consult_id}'")
    db.commit()


def get_consults_by_dog(dog_id: int):
    value = cur.execute(f"SELECT * FROM Consultation WHERE dog_id == '{dog_id}'").fetchall()
    return value


def get_consults_by_kinolog_and_dog(kinolog_id: int, dog_id: int):
    value = cur.execute(f"SELECT * FROM Consultation WHERE dog_id == {dog_id} AND kinolog_id == '{kinolog_id}'").fetchone()
    return value


def delete_consult(consult_id: int):
    cur.execute(f"DELETE FROM Consultation WHERE consult_id == '{consult_id}'")
    db.commit()


def delete_consults_kinolog(kinolog_id: int):
    cur.execute(f"DELETE FROM Consultation WHERE kinolog_id == '{kinolog_id}'")
    db.commit()


def delete_kinolog(kinolog_id: int):
    cur.execute(f"DELETE FROM Kinolog WHERE kinolog_id == '{kinolog_id}'")
    db.commit()


# def update_conn_sum(conn_id: int, conn_sum: int):
#     cur.execute(f"UPDATE Connections SET conn_sum = {conn_sum} WHERE conn_id == {conn_id}")
#     db.commit()
#
#
#




