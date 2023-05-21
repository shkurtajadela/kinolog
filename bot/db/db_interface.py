from datetime import datetime
from bot.db import sqlite
from bot.help_func.help_func import get_date
from bot.help_func.parse_db import parse_dog, parse_kinolog, parse_consult, parse_consults


def new_kinolog(chat_id: int, name: str, surname: str, patronymic: str, birthday: str, email: str,
                education: str, other_education: str, communities: str, practice_date: str, online_work: str,
                supervised: str, other_interests: str, kinolog_site: str, motivation: str, work_stages: str,
                dog_teaching: str, influenced_by: str, punishment: str, punishment_effect: str, ammunition: str,
                other_activities: str, work_methods: str, choice_importance: str, training_situation: str, advise: str):
    sqlite.new_kinolog(chat_id=chat_id, name=name, surname=surname, patronymic=patronymic, birthday=birthday, email=email,
                       education=education, other_education=other_education, communities=communities,
                       practice_date=practice_date, online_work=online_work, supervised=supervised,
                       other_interests=other_interests, kinolog_site=kinolog_site, motivation=motivation,
                       work_stages=work_stages, dog_teaching=dog_teaching, influenced_by=influenced_by,
                       punishment=punishment, punishment_effect=punishment_effect, ammunition=ammunition,
                       other_activities=other_activities, work_methods=work_methods,
                       choice_importance=choice_importance, training_situation=training_situation, advise=advise)


def new_dog(chat_id: int, problem: str, age:str, breed: str, weight: int, origin: str, living_together: str,
            diseases: str):
    sqlite.new_dog(chat_id=chat_id, problem=problem, age=age, breed=breed, weight=weight, origin=origin, living_together=living_together,
                   diseases=diseases)

def get_dog(dog_id: int):
    db_dog = sqlite.get_dog(dog_id=dog_id)
    dog = parse_dog(db_dog=db_dog)

    return dog

def get_kinolog(kinolog_id: int):
    db_kinolog = sqlite.get_kinolog(kinolog_id=kinolog_id)
    kinolog = parse_kinolog(db_kinolog=db_kinolog)

    return kinolog


def new_consults_empty(kinolog_id: int, consult_date: str):
    sqlite.new_consul_empty(kinolog_id=kinolog_id, consult_date=consult_date)


def update_consult(consult_id: int, consult_sum: int = None, dog_id: int = None):
    if dog_id:
        sqlite.update_consul_dog_id(consult_id=consult_id, dog_id=dog_id, consult_sttaus=1)
    if consult_sum:
        sqlite.update_consul_sum(consult_id=consult_id, consult_sum=consult_sum, consult_status=2)


def get_consults_by_dog(dog_id: int):
    db_consults = sqlite.get_consults_by_dog(dog_id=dog_id)
    consults = parse_consults(db_consults=db_consults)

    return consults


def get_consults_by_kinolog(kinolog_id: int):
    db_consults = sqlite.get_consults_by_kinolog(kinolog_id=kinolog_id)
    consults = parse_consults(db_consults=db_consults)

    return consults


def get_consults_by_kinolog_and_dog(kinolog_id: int, dog_id: int):
    db_consults = sqlite.get_consults_by_kinolog_and_dog(kinolog_id=kinolog_id, dog_id=dog_id)
    consults = parse_consults(db_consults=db_consults)

    return consults


def delete_kinolog(kinolog_id: int):
    sqlite.delete_consults_kinolog(kinolog_id=kinolog_id)
    sqlite.delete_kinolog(kinolog_id=kinolog_id)


def delete_consult(consult_id: int):
    sqlite.delete_consult(consult_id=consult_id)
