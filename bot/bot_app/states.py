from aiogram.dispatcher.filters.state import State, StatesGroup

class GeneralStates(StatesGroup):
    start = State()
    registration = State()
    choose_user = State()
    kinolog = State()
    user = State()

class KinologFormStatesGroup(StatesGroup):
    name = State()
    surname = State()
    patronymic = State()
    birthday = State()
    email = State()
    education = State() 
    other_education = State()
    communities = State()
    practice_date = State()
    online_work = State()
    supervised = State()
    other_interests = State()
    kinolog_site = State()
    motivation = State()
    work_stages = State()
    dog_teaching = State()
    influenced_by = State()
    punishment = State() 
    punishment_effect = State()
    ammunition = State()
    other_activities = State()
    work_methods = State()
    choice_importance = State()
    training_situation = State()
    advise = State()
    problem = State()
    problem2 = State()
    problem3 = State()
    form_confirm = State()
    change_form = State()
    edit_form = State()
    photo = State()
    intro = State()
    card_confirm = State()


class MainMenuStatesGroup(StatesGroup):
    main_menu = State()


class KinologFormSubmissionStatesGroup(StatesGroup):
    kinolog_form_submission = State()


class DogFormStatesGroup(StatesGroup):
    problem = State()
    age = State()
    breed = State()
    weight = State()
    origin = State()
    living_together = State() 
    diseases = State()
    diseases_list = State()
    form_confirm = State()
    kinolog_choose = State()
    chat = State()
    