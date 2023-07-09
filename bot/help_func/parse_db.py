def parse_kinolog(db_kinolog: tuple):
    kinolog = {
        'kinolog_id': db_kinolog[0],
        'chat_id': db_kinolog[1],
        'name': db_kinolog[2],
        'surname': db_kinolog[3],
        'patronymic': db_kinolog[4],
        'birthday': db_kinolog[5],
        'email': db_kinolog[6],
        'education': db_kinolog[7],
        'other_education': db_kinolog[8],
        'communities': db_kinolog[9],
        'practice_date': db_kinolog[10],
        'online_work': db_kinolog[11],
        'supervised': db_kinolog[12],
        'other_interests': db_kinolog[13],
        'kinolog_site': db_kinolog[14],
        'motivation': db_kinolog[15],
        'work_stages': db_kinolog[16],
        'dog_teaching': db_kinolog[17],
        'influenced_by': db_kinolog[18],
        'punishment': db_kinolog[19],
        'punishment_effect': db_kinolog[20],
        'ammunition': db_kinolog[21],
        'other_activities': db_kinolog[22],
        'work_methods': db_kinolog[23],
        'choice_importance': db_kinolog[24],
        'training_situation': db_kinolog[25],
        'advise': db_kinolog[26],
        'problem': db_kinolog[27],
        'photo': db_kinolog[28],
        'intro': db_kinolog[29],
        'form_status': db_kinolog[30]
    }

    return kinolog


def parse_dog(db_dog: tuple):
    dog = {
        'dog_id': db_dog[0],
        'problem': db_dog[1],
        'age': db_dog[2],
        'breed': db_dog[3],
        'weight': db_dog[4],
        'origin': db_dog[5],
        'living_together': db_dog[6],
        'diseases': db_dog[7],
    }

    return dog


def parse_consult(db_consult: tuple):
    consult = {
        'consult_id': db_consult[0],
        'kinolog_id': db_consult[1],
        'dog_id': db_consult[2],
        'consult_status': db_consult[3],
        'consult_date': db_consult[4],
        'consult_sum': db_consult[5],
    }

    return consult


def parse_consults(db_consults: list):
    consults = [parse_consult(db_consult=db_consult) for db_consult in db_consults]

    return consults


def parse_kinologs(db_kinologs: list):
    kinologs = [parse_kinolog(db_kinolog=db_kinolog) for db_kinolog in db_kinologs]

    return kinologs
