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

ikbb_weight_1 = InlineKeyboardButton(text='Мини (до 5 кг)', callback_data='weight1')
ikbb_weight_2 = InlineKeyboardButton(text='Малый (5-10 кг)', callback_data='weight2')
ikbb_weight_3 = InlineKeyboardButton(text='Средний (10-20 кг)', callback_data='weight3')
ikbb_weight_4 = InlineKeyboardButton(text='Большой (20-40 кг)', callback_data='weight3')
ikbb_weight_5 = InlineKeyboardButton(text='Огромный (40кг+)', callback_data='weight3')


ikbb_origin_breeder = InlineKeyboardButton(text='У заводчика', callback_data='breeder')
ikbb_origin_street = InlineKeyboardButton(text='Из приюта / с улицы', callback_data='street')
ikbb_origin_other_owner = InlineKeyboardButton(text='От другого хозяина, который отдавал собаку', callback_data='other_owner')

ikbb_disease_no = InlineKeyboardButton(text='Нет', callback_data='no')
ikbb_disease_yes = InlineKeyboardButton(text='Да', callback_data='yes')

ikbb_kinolog_choose = InlineKeyboardButton(text='Выбрать этого специалиста', callback_data='choose')
ikbb_kinolog_refuse = InlineKeyboardButton(text='Выбрать другого специалиста', callback_data='refuse')
ikbb_kinolog_back = InlineKeyboardButton(text='Вернуться назад', callback_data='back')

ikbb_kinolog_chat = InlineKeyboardButton(text='Перейти к чату', callback_data='go_to_chat')

ikbb_kinolog_registration = InlineKeyboardButton(text='Регистрация', callback_data='registration')

ikbb_kinolog_kinolog = InlineKeyboardButton(text='Кинолог', callback_data='kinolog')
ikbb_kinolog_user = InlineKeyboardButton(text='Клиент', callback_data='user')

ikbb_kinolog_form = InlineKeyboardButton(text='Заполнить анкету', callback_data='form')
ikbb_kinolog_card = InlineKeyboardButton(text='Заполнить карту', callback_data='card')

ikbb_kinolog_problem_next = InlineKeyboardButton(text='Перейти к следующим вопросам', callback_data='next')

ikbb_client_form = InlineKeyboardButton(text='Рассказать поподробнее о сложности с собакой', callback_data='form')

ikbb_kinolog_send_card = InlineKeyboardButton(text='Отправить карту', callback_data='send')
ikbb_kinolog_to_start = InlineKeyboardButton(text='Перейти к началу', callback_data='go_to_start')

ikbb_kinolog_send_form = InlineKeyboardButton(text='Отправить карту', callback_data='send')
ikbb_kinolog_change_form = InlineKeyboardButton(text='Изменить карту', callback_data='change')

ikbb_dog_get_kinologs = InlineKeyboardButton(text='Посмотреть подходящих специалистов', callback_data='get_kinologs')

def get_ikb_chat() -> InlineKeyboardMarkup:
    ikb_chat = InlineKeyboardMarkup(row_width=1)
    ikb_chat.add(ikbb_kinolog_chat)
    return ikb_chat

def get_ikb_registration() -> InlineKeyboardMarkup:
    ikb_registration = InlineKeyboardMarkup(row_width=1)
    ikb_registration.add(ikbb_kinolog_registration)
    return ikb_registration


def get_ikb_user_type() -> InlineKeyboardMarkup:
    ikb_user = InlineKeyboardMarkup(row_width=1)
    ikb_user.add(ikbb_kinolog_kinolog, ikbb_kinolog_user)
    return ikb_user


def get_ikb_kinolog_form() -> InlineKeyboardMarkup:
    ikb_user = InlineKeyboardMarkup(row_width=1)
    ikb_user.add(ikbb_kinolog_form, ikbb_kinolog_back)
    return ikb_user

def get_ikb_client_form() -> InlineKeyboardMarkup:
    ikb_user = InlineKeyboardMarkup(row_width=1)
    ikb_user.add(ikbb_client_form, ikbb_kinolog_back)
    return ikb_user

def get_ikb_kinolog_card() -> InlineKeyboardMarkup:
    ikb_user = InlineKeyboardMarkup(row_width=1)
    ikb_user.add(ikbb_kinolog_card, ikbb_kinolog_back)
    return ikb_user


def get_ikb_send_card() -> InlineKeyboardMarkup:
    ikb_user = InlineKeyboardMarkup(row_width=1)
    ikb_user.add(ikbb_kinolog_send_card, ikbb_kinolog_back, ikbb_kinolog_to_start)
    return ikb_user

def get_ikb_confirm_form() -> InlineKeyboardMarkup:
    ikb_user = InlineKeyboardMarkup(row_width=1)
    ikb_user.add(ikbb_kinolog_send_form, ikbb_kinolog_change_form, ikbb_kinolog_to_start)
    return ikb_user

def get_ikb_confirm_dog_form() -> InlineKeyboardMarkup:
    ikb_user = InlineKeyboardMarkup(row_width=1)
    ikb_user.add(ikbb_dog_get_kinologs, ikbb_kinolog_to_start)
    return ikb_user


def get_ikb_change_form() -> InlineKeyboardMarkup:
    ikb_change = InlineKeyboardMarkup(row_width=6)
    row = []
    for i in range(1, 25):
        button = InlineKeyboardButton(str(i), callback_data=str(i))
        row.append(button)
        
        if len(row) == 6:
            ikb_change.add(row[0], row[1], row[2], row[3], row[4], row[5])
            row = []
    
    change_all_button = InlineKeyboardButton("Изменить всю анкету", callback_data="change_all")
    ikb_change.add(change_all_button)
    ikb_change.add(ikbb_kinolog_send_form)
    ikb_change.add(ikbb_kinolog_to_start)

    return ikb_change

def get_ikb_choose_kinolog() -> InlineKeyboardMarkup:
    ikb_kinolog = InlineKeyboardMarkup(row_width=1)
    ikb_kinolog.add(ikbb_kinolog_choose, ikbb_kinolog_refuse)
    return ikb_kinolog

def get_ikb_choose_kinolog_with_back() -> InlineKeyboardMarkup:
    ikb_kinolog = InlineKeyboardMarkup(row_width=1)
    ikb_kinolog.add(ikbb_kinolog_choose, ikbb_kinolog_refuse, ikbb_kinolog_back)
    return ikb_kinolog

def get_ikb_choose_kinolog_back() -> InlineKeyboardMarkup:
    ikb_kinolog = InlineKeyboardMarkup(row_width=1)
    ikb_kinolog.add(ikbb_kinolog_back)
    return ikb_kinolog


def get_ikb_supervised() -> InlineKeyboardMarkup:
    ikb_supervised = InlineKeyboardMarkup(row_width=1)
    ikb_supervised.add(ikbb_supervised_no, ikbb_supervised_yes_before, ikbb_supervised_yes_rarely, ikbb_supervised_yes_usually)
    return ikb_supervised

def get_ikb_problem() -> InlineKeyboardMarkup:
    ikb_problem = InlineKeyboardMarkup(row_width=1)
    ikb_problem.add(ikbb_problem_agression, ikbb_problem_barking, ikbb_problem_behaviour, ikbb_problem_hyper, ikbb_problem_anxiety, ikbb_problem_tension, ikbb_problem_agression_people, ikbb_problem_fear, ikbb_problem_food, ikbb_problem_leash, ikbb_problem_hearing, ikbb_problem_else)
    return ikb_problem

def get_ikb_problem_optional() -> InlineKeyboardMarkup:
    ikb_problem = InlineKeyboardMarkup(row_width=1)
    ikb_problem.add(ikbb_problem_agression, ikbb_problem_barking, ikbb_problem_behaviour, ikbb_problem_hyper, ikbb_problem_anxiety, ikbb_problem_tension, ikbb_problem_agression_people, ikbb_problem_fear, ikbb_problem_food, ikbb_problem_leash, ikbb_problem_hearing, ikbb_problem_else, ikbb_kinolog_problem_next)
    return ikb_problem

def get_ikb_weight() -> InlineKeyboardMarkup:
    ikb_weight = InlineKeyboardMarkup(row_width=1)
    ikb_weight.add(ikbb_weight_1, ikbb_weight_2, ikbb_weight_3, ikbb_weight_4, ikbb_weight_5)
    return ikb_weight

def get_ikb_origin() -> InlineKeyboardMarkup:
    ikb_origin = InlineKeyboardMarkup(row_width=1)
    ikb_origin.add(ikbb_origin_breeder, ikbb_origin_street, ikbb_origin_other_owner)
    return ikb_origin

def get_ikb_disease() -> InlineKeyboardMarkup:
    ikb_disease = InlineKeyboardMarkup(row_width=1)
    ikb_disease.add(ikbb_disease_yes, ikbb_disease_no)
    return ikb_disease