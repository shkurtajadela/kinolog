from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup

inline_button_kin = InlineKeyboardButton('Кинолог', callback_data='kinolog')
inline_button_user = InlineKeyboardButton('Пользователь', callback_data='user')
inline_kb = InlineKeyboardMarkup()

inline_kb.add(inline_button_kin).add(inline_button_user)

kin_q1 = InlineKeyboardButton('answer 1', callback_data='ans1')
kin_q2 = InlineKeyboardButton('answer 2', callback_data='ans2')
kin_q3 = InlineKeyboardButton('answer 3', callback_data='ans3')

kb_kin_q = InlineKeyboardMarkup()
kb_kin_q.add(kin_q1).add(kin_q2).add(kin_q3)

ikbb_supervised_no = InlineKeyboardButton(text='Нет, никогда не проходил(а)', callback_data='no_supervised')
ikbb_supervised_yes_before = InlineKeyboardButton(text='Да, проходил(а) когда-то, сейчас не прохожу', callback_data='before_supervised')
ikbb_supervised_yes_rarely = InlineKeyboardButton(text='Да, прохожу редко (раз в несколько месяцев)', callback_data='rarely_supervised')
ikbb_supervised_yes_usually = InlineKeyboardButton(text='Да, прохожу постоянно (раз в месяц и чаще)', callback_data='usually_supervised')

ikbb_problem_agression = InlineKeyboardButton(text='Агрессия по отношению к другим собакам/животным', callback_data='agression')
ikbb_problem_barking = InlineKeyboardButton(text='Лай на звуки/дверь и тревожность дома', callback_data='barking')
ikbb_problem_behaviour = InlineKeyboardButton(text='Деструктивное поведение (порча вещей, дефекция и тд)', callback_data='behaviour')
ikbb_problem_hyper = InlineKeyboardButton(text='Гиперактивность (копание, прыгучесть и тд)', callback_data='hyper')
ikbb_problem_anxiety = InlineKeyboardButton(text='Сепарационная тревога (скулит или воет, когда оставляют одного / уходят)', callback_data='anxiety')
ikbb_problem_tension = InlineKeyboardButton(text='Подавленное состояние животного без медицинских причин', callback_data='tension')
ikbb_problem_agression_people = InlineKeyboardButton(text='Агрессия ко мне и/или другим людям', callback_data='agression_people')
ikbb_problem_fear = InlineKeyboardButton(text='Страх других животных / собак', callback_data='fear')
ikbb_problem_food = InlineKeyboardButton(text='Проблемы с пищевым поведением (подбор на улице, сложности дома)', callback_data='food')
ikbb_problem_leash = InlineKeyboardButton(text='Тянет поводок', callback_data='leash')
ikbb_problem_hearing = InlineKeyboardButton(text='Проблемы с послушанием и командами', callback_data='hearing')
ikbb_problem_else = InlineKeyboardButton(text='Другое...', callback_data='else')

ikbb_race_1 = InlineKeyboardButton(text='Пород 1', callback_data='breed1')
ikbb_race_2 = InlineKeyboardButton(text='Пород 2', callback_data='breed2')
ikbb_race_3 = InlineKeyboardButton(text='Пород 3', callback_data='breed3')
ikbb_race_else = InlineKeyboardButton(text='Другое...', callback_data='else')


ikbb_origin_breeder = InlineKeyboardButton(text='У заводчика', callback_data='breeder')
ikbb_origin_street = InlineKeyboardButton(text='Из приюта / с улицы', callback_data='street')
ikbb_origin_other_owner = InlineKeyboardButton(text='От другого хозяина, который отдавал собаку', callback_data='other_owner')

ikbb_disease_no = InlineKeyboardButton(text='Нет', callback_data='no')
ikbb_disease_yes = InlineKeyboardButton(text='Да', callback_data='yes')

def get_ikb_supervised() -> InlineKeyboardMarkup:
    ikb_supervised = InlineKeyboardMarkup(row_width=1)
    ikb_supervised.add(ikbb_supervised_no, ikbb_supervised_yes_before, ikbb_supervised_yes_rarely, ikbb_supervised_yes_usually)
    return ikb_supervised

def get_ikb_problem() -> InlineKeyboardMarkup:
    ikb_problem = InlineKeyboardMarkup(row_width=1)
    ikb_problem.add(ikbb_problem_agression, ikbb_problem_barking, ikbb_problem_behaviour, ikbb_problem_hyper, ikbb_problem_anxiety, ikbb_problem_tension, ikbb_problem_agression_people, ikbb_problem_fear, ikbb_problem_food, ikbb_problem_leash, ikbb_problem_hearing, ikbb_problem_else)
    return ikb_problem

def get_ikb_breed() -> InlineKeyboardMarkup:
    ikb_breed = InlineKeyboardMarkup(row_width=1)
    ikb_breed.add(ikbb_race_1, ikbb_race_2, ikbb_race_3, ikbb_race_else)
    return ikb_breed

def get_ikb_origin() -> InlineKeyboardMarkup:
    ikb_origin = InlineKeyboardMarkup(row_width=1)
    ikb_origin.add(ikbb_origin_breeder, ikbb_origin_street, ikbb_origin_other_owner)
    return ikb_origin

def get_ikb_disease() -> InlineKeyboardMarkup:
    ikb_disease = InlineKeyboardMarkup(row_width=1)
    ikb_disease.add(ikbb_disease_yes, ikbb_disease_no)
    return ikb_disease