from aiogram import types
from aiogram.dispatcher import FSMContext
import telegram
from .app import dp, bot
from .keyboards import get_ikb_problem_optional, get_ikb_supervised, get_ikb_problem, get_ikb_choose_kinolog_back, get_ikb_registration, get_ikb_send_card, get_ikb_kinolog_card, get_ikb_confirm_form, get_ikb_change_form
from aiogram import types, Dispatcher
from .states import KinologFormStatesGroup, GeneralStates
from bot.db.db_interface import new_kinolog, update_kinolog_card, get_form_status, get_kinolog
from telegram_bot_calendar import DetailedTelegramCalendar, LSTEP
from datetime import date
from .show_form import show_created_check_info

async def start_form_kinolog(callback:types.CallbackQuery, state:FSMContext):
    async with state.proxy() as data:
        await bot.delete_message(chat_id=callback.from_user.id, message_id=callback.message.message_id)
        if callback.data == "card":
            text="Загрузите ваше фото:"
            msg = await bot.send_message(chat_id=callback.from_user.id, text=text, reply_markup=get_ikb_choose_kinolog_back())
            data['msg_id'] = msg.message_id
            await KinologFormStatesGroup.photo.set()
        elif callback.data == "form":
            text = "На все вопросы нужно ответить! \n\n<b>Напишите ваше имя:</b>"
            msg = await bot.send_message(chat_id=callback.from_user.id, text=text, parse_mode=telegram.constants.ParseMode.HTML)
            data['msg_id'] = msg.message_id
            data['change'] = 0
            # data['patronymic'], data['birthday'], data['email'], data['education'], data['other_education'], data['communities'], data['practice_date'], data['online_work'], data['supervised'], data['other_interests'], data['kinolog_site'], data[ 'motivation'], data['work_stages'], data['dog_teaching'], data['influenced_by'], data['punishment'], data['punishment_effect'], data['ammunition'], data['other_activities'], data['work_methods'], data['choice_importance'], data['training_situation'], data['advise'], data['problem'] = "0"
            await KinologFormStatesGroup.name.set()
        elif callback.data == "back":
            welcome_msg = "Привет! Это бот для заполнения анкеты кинологом или поиска кинолога владельцем собаки. \nЕсли хотите зарегистрироваться, то нажимайте кнопку ниже"
            await bot.send_message(chat_id=callback.from_user.id, text=welcome_msg, reply_markup=get_ikb_registration())
            await GeneralStates.registration.set()

async def form_load(message:types.Message, state:FSMContext, field: str, text: str):
    await bot.delete_message(chat_id=message.from_user.id, message_id=message.message_id)

    async with state.proxy() as data:
        data[field] = message.text
        ans = {
            'name': "show_created_check_info(data['name'])",
            'surname': "show_created_check_info(data['name'], data['surname'])",
            'email': "show_created_check_info(name=data['name'], surname=data['surname'], patronymic=data['patronymic'], birthday=data['birthday'], email=data['email'])",
            'education': "show_created_check_info(name=data['name'], surname=data['surname'], patronymic=data['patronymic'], birthday=data['birthday'], email=data['email'], education=data['education'])",
            'other_education': "show_created_check_info(name=data['name'], surname=data['surname'], patronymic=data['patronymic'], birthday=data['birthday'], email=data['email'], education=data['education'], other_education=data['other_education'])",
            'communities': "show_created_check_info(name=data['name'], surname=data['surname'], patronymic=data['patronymic'], birthday=data['birthday'], email=data['email'], education=data['education'], other_education=data['other_education'], communities=data['communities'])",   
            'practice_date': "show_created_check_info(name=data['name'], surname=data['surname'], patronymic=data['patronymic'], birthday=data['birthday'], email=data['email'], education=data['education'], other_education=data['other_education'], communities=data['communities'], practice_date=data['practice_date'])",
            'online_work': "show_created_check_info(name=data['name'], surname=data['surname'], patronymic=data['patronymic'], birthday=data['birthday'], email=data['email'], education=data['education'], other_education=data['other_education'], communities=data['communities'], practice_date=data['practice_date'], online_work=data['online_work'])",
            'supervised': "show_created_check_info(name=data['name'], surname=data['surname'], patronymic=data['patronymic'], birthday=data['birthday'], email=data['email'], education=data['education'], other_education=data['other_education'], communities=data['communities'], practice_date=data['practice_date'], online_work=data['online_work'], supervised=data['supervised'])",
            'other_interests': "show_created_check_info(name=data['name'], surname=data['surname'], patronymic=data['patronymic'], birthday=data['birthday'], email=data['email'], education=data['education'], other_education=data['other_education'], communities=data['communities'], practice_date=data['practice_date'], online_work=data['online_work'], supervised=data['supervised'], other_interests=data['other_interests'])",
            'kinolog_site': "show_created_check_info(name=data['name'], surname=data['surname'], patronymic=data['patronymic'], birthday=data['birthday'], email=data['email'], education=data['education'], other_education=data['other_education'], communities=data['communities'], practice_date=data['practice_date'], online_work=data['online_work'], supervised=data['supervised'], other_interests=data['other_interests'], kinolog_site=data['kinolog_site'])",
            'motivation': "show_created_check_info(name=data['name'], surname=data['surname'], patronymic=data['patronymic'], birthday=data['birthday'], email=data['email'], education=data['education'], other_education=data['other_education'], communities=data['communities'], practice_date=data['practice_date'], online_work=data['online_work'], supervised=data['supervised'], other_interests=data['other_interests'], kinolog_site=data['kinolog_site'], motivation=data[ 'motivation'])",
            'work_stages': "show_created_check_info(name=data['name'], surname=data['surname'], patronymic=data['patronymic'], birthday=data['birthday'], email=data['email'], education=data['education'], other_education=data['other_education'], communities=data['communities'], practice_date=data['practice_date'], online_work=data['online_work'], supervised=data['supervised'], other_interests=data['other_interests'], kinolog_site=data['kinolog_site'], motivation=data[ 'motivation'], work_stages=data['work_stages'])",
            'dog_teaching': "show_created_check_info(name=data['name'], surname=data['surname'], patronymic=data['patronymic'], birthday=data['birthday'], email=data['email'], education=data['education'], other_education=data['other_education'], communities=data['communities'], practice_date=data['practice_date'], online_work=data['online_work'], supervised=data['supervised'], other_interests=data['other_interests'], kinolog_site=data['kinolog_site'], motivation=data[ 'motivation'], work_stages=data['work_stages'], dog_teaching=data['dog_teaching'])",
            'influenced_by': "show_created_check_info(name=data['name'], surname=data['surname'], patronymic=data['patronymic'], birthday=data['birthday'], email=data['email'], education=data['education'], other_education=data['other_education'], communities=data['communities'], practice_date=data['practice_date'], online_work=data['online_work'], supervised=data['supervised'], other_interests=data['other_interests'], kinolog_site=data['kinolog_site'], motivation=data[ 'motivation'], work_stages=data['work_stages'], dog_teaching=data['dog_teaching'], influenced_by=data['influenced_by'])",
            'punishment': "show_created_check_info(name=data['name'], surname=data['surname'], patronymic=data['patronymic'], birthday=data['birthday'], email=data['email'], education=data['education'], other_education=data['other_education'], communities=data['communities'], practice_date=data['practice_date'], online_work=data['online_work'], supervised=data['supervised'], other_interests=data['other_interests'], kinolog_site=data['kinolog_site'], motivation=data[ 'motivation'], work_stages=data['work_stages'], dog_teaching=data['dog_teaching'], influenced_by=data['influenced_by'],punishment=data['punishment'])",
            'punishment_effect': "show_created_check_info(name=data['name'], surname=data['surname'], patronymic=data['patronymic'], birthday=data['birthday'], email=data['email'], education=data['education'], other_education=data['other_education'], communities=data['communities'], practice_date=data['practice_date'], online_work=data['online_work'], supervised=data['supervised'], other_interests=data['other_interests'], kinolog_site=data['kinolog_site'], motivation=data[ 'motivation'], work_stages=data['work_stages'], dog_teaching=data['dog_teaching'], influenced_by=data['influenced_by'],punishment=data['punishment'], punishment_effect=data['punishment_effect'])",
            'ammunition': "show_created_check_info(name=data['name'], surname=data['surname'], patronymic=data['patronymic'], birthday=data['birthday'], email=data['email'], education=data['education'], other_education=data['other_education'], communities=data['communities'], practice_date=data['practice_date'], online_work=data['online_work'], supervised=data['supervised'], other_interests=data['other_interests'], kinolog_site=data['kinolog_site'], motivation=data[ 'motivation'], work_stages=data['work_stages'], dog_teaching=data['dog_teaching'], influenced_by=data['influenced_by'],punishment=data['punishment'], punishment_effect=data['punishment_effect'], ammunition=data['ammunition'])",
            'other_activities': "show_created_check_info(name=data['name'], surname=data['surname'], patronymic=data['patronymic'], birthday=data['birthday'], email=data['email'], education=data['education'], other_education=data['other_education'], communities=data['communities'], practice_date=data['practice_date'], online_work=data['online_work'], supervised=data['supervised'], other_interests=data['other_interests'], kinolog_site=data['kinolog_site'], motivation=data[ 'motivation'], work_stages=data['work_stages'], dog_teaching=data['dog_teaching'], influenced_by=data['influenced_by'],punishment=data['punishment'], punishment_effect=data['punishment_effect'], ammunition=data['ammunition'], other_activities=data['other_activities'])",
            'work_methods': "show_created_check_info(name=data['name'], surname=data['surname'], patronymic=data['patronymic'], birthday=data['birthday'], email=data['email'], education=data['education'], other_education=data['other_education'], communities=data['communities'], practice_date=data['practice_date'], online_work=data['online_work'], supervised=data['supervised'], other_interests=data['other_interests'], kinolog_site=data['kinolog_site'], motivation=data[ 'motivation'], work_stages=data['work_stages'], dog_teaching=data['dog_teaching'], influenced_by=data['influenced_by'],punishment=data['punishment'], punishment_effect=data['punishment_effect'], ammunition=data['ammunition'], other_activities=data['other_activities'], work_methods=data['work_methods'])",
            'choice_importance': "show_created_check_info(name=data['name'], surname=data['surname'], patronymic=data['patronymic'], birthday=data['birthday'], email=data['email'], education=data['education'], other_education=data['other_education'], communities=data['communities'], practice_date=data['practice_date'], online_work=data['online_work'], supervised=data['supervised'], other_interests=data['other_interests'], kinolog_site=data['kinolog_site'], motivation=data[ 'motivation'], work_stages=data['work_stages'], dog_teaching=data['dog_teaching'], influenced_by=data['influenced_by'],punishment=data['punishment'], punishment_effect=data['punishment_effect'], ammunition=data['ammunition'], other_activities=data['other_activities'], work_methods=data['work_methods'], choice_importance=data['choice_importance'])",
            'training_situation' : "show_created_check_info(name=data['name'], surname=data['surname'], patronymic=data['patronymic'], birthday=data['birthday'], email=data['email'], education=data['education'], other_education=data['other_education'], communities=data['communities'], practice_date=data['practice_date'], online_work=data['online_work'], supervised=data['supervised'], other_interests=data['other_interests'], kinolog_site=data['kinolog_site'], motivation=data[ 'motivation'], work_stages=data['work_stages'], dog_teaching=data['dog_teaching'], influenced_by=data['influenced_by'],punishment=data['punishment'], punishment_effect=data['punishment_effect'], ammunition=data['ammunition'], other_activities=data['other_activities'], work_methods=data['work_methods'], choice_importance=data['choice_importance'], training_situation=data['training_situation'])",
            'advise': "show_created_check_info(name=data['name'], surname=data['surname'], patronymic=data['patronymic'], birthday=data['birthday'], email=data['email'], education=data['education'], other_education=data['other_education'], communities=data['communities'], practice_date=data['practice_date'], online_work=data['online_work'], supervised=data['supervised'], other_interests=data['other_interests'], kinolog_site=data['kinolog_site'], motivation=data[ 'motivation'], work_stages=data['work_stages'], dog_teaching=data['dog_teaching'], influenced_by=data['influenced_by'],punishment=data['punishment'], punishment_effect=data['punishment_effect'], ammunition=data['ammunition'], other_activities=data['other_activities'], work_methods=data['work_methods'], choice_importance=data['choice_importance'], training_situation=data['training_situation'], advise=data['advise'])"
        }
        func = eval(ans[field])
        msg_text = f"{func}\n\n{text}"
        await bot.edit_message_text(chat_id=message.from_user.id, text=msg_text, message_id=data['msg_id'], parse_mode=telegram.constants.ParseMode.HTML)
        await KinologFormStatesGroup.next()

        
async def form_load_kinolog_name(message:types.Message, state:FSMContext):
    await form_load(message, state, 'name', '<b>Напишите вашу фамилию:</b>')

async def form_load_kinolog_surname(message:types.Message, state:FSMContext):
    await form_load(message, state, 'surname', '<b>Напишите ваше отчество:</b>')

async def form_load_kinolog_patronymic(message:types.Message, state:FSMContext):
    await bot.delete_message(chat_id=message.from_user.id, message_id=message.message_id)
    async with state.proxy() as data:
        data['patronymic'] = message.text

        if data['change'] == 0:
            calendar, step = DetailedTelegramCalendar(max_date=date(2022,1,1)).build()
            await bot.edit_message_text(chat_id=message.from_user.id,text=
                        f"Выберите день рождения: {LSTEP[step]}", message_id=data['msg_id'],
                        reply_markup=calendar)
            await KinologFormStatesGroup.next()
        else:
            text = 'Что еще вы хотите изменить:'
            await bot.edit_message_text(chat_id=message.from_user.id, text=text, message_id=data['msg_id'], reply_markup=get_ikb_change_form())
            await KinologFormStatesGroup.change_form.set()

async def form_load_kinolog_birthday(callback:types.CallbackQuery, state:FSMContext):
    result, key, step = DetailedTelegramCalendar(max_date=date(2022,1,1)).process(callback.data)
    if not result and key:
        await bot.edit_message_text(f"Выберите день рождения: {LSTEP[step]}",
                            callback.message.chat.id,
                            callback.message.message_id,
                            reply_markup=key)
    elif result:
        async with state.proxy() as data:
            data['birthday'] = str(result)

            if data['change'] == 0:
                text = f"{show_created_check_info(data['name'], data['surname'], data['patronymic'], data['birthday'])}"
                text += '\n\n<b>Напишите вашу почту:</b>'
                await bot.edit_message_text(chat_id=callback.from_user.id, text=text, message_id=data['msg_id'], parse_mode=telegram.constants.ParseMode.HTML)
                await KinologFormStatesGroup.next()
            else:
                text = f"{show_created_check_info(name=data['name'], surname=data['surname'], patronymic=data['patronymic'], birthday=data['birthday'], email=data['email'], education=data['education'], other_education=data['other_education'], communities=data['communities'], practice_date=data['practice_date'], online_work=data['online_work'], supervised=data['supervised'], other_interests=data['other_interests'], kinolog_site=data['kinolog_site'], motivation=data[ 'motivation'], work_stages=data['work_stages'], dog_teaching=data['dog_teaching'], influenced_by=data['influenced_by'],punishment=data['punishment'], punishment_effect=data['punishment_effect'], ammunition=data['ammunition'], other_activities=data['other_activities'], work_methods=data['work_methods'], choice_importance=data['choice_importance'], training_situation=data['training_situation'], advise=data['advise'], problem=data['problem'])}"
                text += '\n\n<b>Что еще вы хотите изменить:</b>'
                await bot.edit_message_text(chat_id=callback.from_user.id, text=text, reply_markup=get_ikb_change_form(), message_id=callback.message.message_id, parse_mode=telegram.constants.ParseMode.HTML)
                await KinologFormStatesGroup.change_form.set()

        
async def form_load_kinolog_email(message:types.Message, state:FSMContext):
    await form_load(message, state, 'email', '<b>Какое у вас высшее образование?</b>')


async def form_load_kinolog_education(message:types.Message, state:FSMContext):
    text = '<b>Пожалуйста, перечислите все курсы или дополнительное образование (семинары, повышение квалификации, вебинары), которые вы прошли/прослушали:</b>'
    await form_load(message, state, 'education', text)

async def form_load_kinolog_other_education(message:types.Message, state:FSMContext):
    text = '<b>Состоите ли вы в каких-либо профессиональных сообществах, ассоциациях? Если да, то в каких?</b>'
    await form_load(message, state, 'other_education', text)


async def form_load_kinolog_communities(message:types.Message, state:FSMContext):
    text = '<b>Когда вы начали свою кинологическую практику? Укажите месяц и год.</b>'
    await form_load(message, state, 'communities', text)



async def form_load_kinolog_practice_date(message:types.Message, state:FSMContext):
    text = '<b>Есть ли опыт работы онлайн? Если да, сколько лет?</b>'
    await form_load(message, state, 'practice_date', text)



async def form_load_kinolog_online_work(message:types.Message, state:FSMContext):
    async with state.proxy() as data:
        await bot.delete_message(chat_id=message.from_user.id, message_id=data['msg_id'])
        await bot.delete_message(chat_id=message.from_user.id, message_id=message.message_id)

        data['online_work'] = message.text

        text = f"{show_created_check_info(name=data['name'], surname=data['surname'], patronymic=data['patronymic'], birthday=data['birthday'], email=data['email'], education=data['education'], other_education=data['other_education'], communities=data['communities'], practice_date=data['practice_date'], online_work=data['online_work'])}"
        text += '\n\n<b>Проходите ли вы супервизии?</b>'
        reply_markup  = get_ikb_supervised()
        msg = await bot.send_message(chat_id=message.from_user.id, text=text, reply_markup=reply_markup, parse_mode=telegram.constants.ParseMode.HTML)
        data['msg_id'] = msg.message_id
        await KinologFormStatesGroup.next()


async def form_load_kinolog_supervised(callback:types.CallbackQuery, state:FSMContext):
    async with state.proxy() as data:
        ans = {'no_supervised': 'Нет, никогда не проходил(а)',
         'before_supervised': 'Да, проходил(а) когда-то, сейчас не прохожу',
         'rarely_supervised': 'Да, прохожу редко (раз в несколько месяцев)',
         'usually_supervised': 'Да, прохожу постоянно (раз в месяц и чаще)'
         }
        data['supervised'] = ans[callback.data]

        if data['change'] == 0:
            text = f"{show_created_check_info(data['name'], data['surname'], data['patronymic'], data['birthday'], data['email'], data['education'], data['other_education'], data['communities'], data['practice_date'], data['online_work'], data['supervised'])}"
            text += '\n\n<b>Есть ли другая работа кроме специалиста по поведению собак? Как распределяются интересы и приоритеты?</b>'
            await bot.edit_message_text(chat_id=callback.from_user.id, text=text, message_id=data['msg_id'], parse_mode=telegram.constants.ParseMode.HTML)
            await KinologFormStatesGroup.next()
        else:
            await bot.delete_message(chat_id=callback.from_user.id, message_id=data['msg_id'])
            text = '\n\n<b>Что еще вы хотите изменить:</b>'
            text += f"{show_created_check_info(name=data['name'], surname=data['surname'], patronymic=data['patronymic'], birthday=data['birthday'], email=data['email'], education=data['education'], other_education=data['other_education'], communities=data['communities'], practice_date=data['practice_date'], online_work=data['online_work'], supervised=data['supervised'], other_interests=data['other_interests'], kinolog_site=data['kinolog_site'], motivation=data[ 'motivation'], work_stages=data['work_stages'], dog_teaching=data['dog_teaching'], influenced_by=data['influenced_by'],punishment=data['punishment'], punishment_effect=data['punishment_effect'], ammunition=data['ammunition'], other_activities=data['other_activities'], work_methods=data['work_methods'], choice_importance=data['choice_importance'], training_situation=data['training_situation'], advise=data['advise'], problem=data['problem'])}"
            msg = await bot.send_message(chat_id=callback.from_user.id, text=text, reply_markup=get_ikb_change_form(), parse_mode=telegram.constants.ParseMode.HTML)
            data['msg_id'] = msg.message_id
            await KinologFormStatesGroup.change_form.set()


async def form_load_kinolog_other_interests(message:types.Message, state:FSMContext):
    text = '<b>Если у вас есть сайт с вашими услугами, пожалуйста, поделитесь им ниже</b>'
    await form_load(message, state, 'other_interests', text)


async def form_load_kinolog_site(message:types.Message, state:FSMContext):
    text = '<b>Теперь вопросы про ваш опыт и взаимодействия с собаками\nЧто вас мотивирует к работе с собаками и людьми?</b>'
    await form_load(message, state, 'kinolog_site', text)

async def form_load_kinolog_motivation(message:types.Message, state:FSMContext):
    text = '<b>Расскажите, каким образом обычно выглядит ваша работа с клиентом? Как вы работаете? Перечислите поэтапно.</b>'
    await form_load(message, state, 'motivation', text)


async def form_load_kinolog_work_stages(message:types.Message, state:FSMContext):
    text = '<b>Как вам кажется, чему наиболее важно научить собаку? Пожалуйста, перечислите не более 4 пунктов.</b>'
    await form_load(message, state, 'work_stages', text)


async def form_load_kinolog_dog_teaching(message:types.Message, state:FSMContext):
    text = '<b>Как вам кажется, кто в большей степени повлиял на вас или вдохновил вас с точки зрения работы с собаками?</b>'
    await form_load(message, state, 'dog_teaching', text)


async def form_load_kinolog_influenced_by(message:types.Message, state:FSMContext):
    text = '<b>Что вы считаете наказанием в работе с собаками?</b>'
    await form_load(message, state, 'influenced_by', text)


async def form_load_kinolog_punishment(message:types.Message, state:FSMContext):
    text = '<b>Какое влияние может иметь наказание на собак?</b>'
    await form_load(message, state, 'punishment', text)


async def form_load_kinolog_punishment_effect(message:types.Message, state:FSMContext):
    text = '<b>Какую амуницию вы используете в работе и рекомендуете? Почему?</b>'
    await form_load(message, state, 'punishment_effect', text)


async def form_load_kinolog_ammunition(message:types.Message, state:FSMContext):
    text = '<b>Есть ли какие-нибудь игры или занятия, которые вы проводите со своими собаками, клиентами или рекомендуете клиентам? Почему?</b>'
    await form_load(message, state, 'ammunition', text)


async def form_load_kinolog_other_activities(message:types.Message, state:FSMContext):
    text = '<b>Используете ли вы или рекомендуете какие-то конкретные методики или протоколы в работе с собаками? Почему?</b>'
    await form_load(message, state, 'other_activities', text)

async def form_load_kinolog_work_methods(message:types.Message, state:FSMContext):
    text = '<b>Почему выбор может быть важной частью или относиться к работе с собаками?</b>'
    await form_load(message, state, 'work_methods', text)

async def form_load_kinolog_choice_importance(message:types.Message, state:FSMContext):
    text = '<b>Что бы вы сделали, если бы столкнулись с ситуацией, связанной с дрессировкой собаки, которую вы изо всех сил пытались решить или разобрать?</b>'
    await form_load(message, state, 'choice_importance', text)

async def form_load_kinolog_training_situation(message:types.Message, state:FSMContext):
    text = '<b>Если не учитывать особенности отдельно взятой собаки, что бы вы могли посоветовать всем владельцам собак?</b>'
    await form_load(message, state, 'training_situation', text)

async def form_load_kinolog_advise(message:types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['advise'] = message.text
        
        text = f"{show_created_check_info(name=data['name'], surname=data['surname'], patronymic=data['patronymic'], birthday=data['birthday'], email=data['email'], education=data['education'], other_education=data['other_education'], communities=data['communities'], practice_date=data['practice_date'], online_work=data['online_work'], supervised=data['supervised'], other_interests=data['other_interests'], kinolog_site=data['kinolog_site'], motivation=data[ 'motivation'], work_stages=data['work_stages'], dog_teaching=data['dog_teaching'], influenced_by=data['influenced_by'],punishment=data['punishment'], punishment_effect=data['punishment_effect'], ammunition=data['ammunition'], other_activities=data['other_activities'], work_methods=data['work_methods'], choice_importance=data['choice_importance'], training_situation=data['training_situation'], advise=data['advise'])}"
        text += "\n\n<b>Какие проблемы собаки вы бы хотели решать?</b>"
        await bot.delete_message(chat_id=message.from_user.id, message_id=message.message_id)
        reply_markup  = get_ikb_problem()
        await bot.edit_message_text(chat_id=message.from_user.id, text=text, reply_markup=reply_markup, message_id=data['msg_id'], parse_mode=telegram.constants.ParseMode.HTML)
        await KinologFormStatesGroup.next()


async def form_load_kinolog_first_problem(callback:types.CallbackQuery, state:FSMContext):
    async with state.proxy() as data:
        ans = {'agression': 'Агрессия по отношению к другим собакам/животным',
         'barking': 'Лай на звуки/дверь и тревожность дома',
         'behaviour': 'Деструктивное поведение (порча вещей, дефекция и тд)',
         'hyper': 'Гиперактивность (копание, прыгучесть и тд)',
         'anxiety': 'Сепарационная тревога (скулит или воет, когда оставляют одного / уходят)',
         'tension': 'Подавленное состояние животного без медицинских причин',
         'agression_people': 'Агрессия ко мне и/или другим людям',
         'fear': 'Страх других животных / собак',
         'food': 'Проблемы с пищевым поведением (подбор на улице, сложности дома)',
         'leash': 'Тянет поводок',
         'hearing': 'Проблемы с послушанием и командами',
         'else': 'Другое...'
         }
        data['problem'] = ans[callback.data]

        text = f"{show_created_check_info(name=data['name'], surname=data['surname'], patronymic=data['patronymic'], birthday=data['birthday'], email=data['email'], education=data['education'], other_education=data['other_education'], communities=data['communities'], practice_date=data['practice_date'], online_work=data['online_work'], supervised=data['supervised'], other_interests=data['other_interests'], kinolog_site=data['kinolog_site'], motivation=data[ 'motivation'], work_stages=data['work_stages'], dog_teaching=data['dog_teaching'], influenced_by=data['influenced_by'],punishment=data['punishment'], punishment_effect=data['punishment_effect'], ammunition=data['ammunition'], other_activities=data['other_activities'], work_methods=data['work_methods'], choice_importance=data['choice_importance'], training_situation=data['training_situation'], advise=data['advise'])}"
        text += "\n\n<b>Вы можете выбрать до трех проблем собаки, которые хотели бы решить. Выберите вторую:</b>"
        reply_markup  = get_ikb_problem_optional()
        await bot.edit_message_text(chat_id=callback.from_user.id, text=text, reply_markup=reply_markup, message_id=data['msg_id'], parse_mode=telegram.constants.ParseMode.HTML)
        await KinologFormStatesGroup.next()



async def form_load_kinolog_second_problem(callback:types.CallbackQuery, state:FSMContext):
    async with state.proxy() as data:
        ans = {'agression': 'Агрессия по отношению к другим собакам/животным',
         'barking': 'Лай на звуки/дверь и тревожность дома',
         'behaviour': 'Деструктивное поведение (порча вещей, дефекция и тд)',
         'hyper': 'Гиперактивность (копание, прыгучесть и тд)',
         'anxiety': 'Сепарационная тревога (скулит или воет, когда оставляют одного / уходят)',
         'tension': 'Подавленное состояние животного без медицинских причин',
         'agression_people': 'Агрессия ко мне и/или другим людям',
         'fear': 'Страх других животных / собак',
         'food': 'Проблемы с пищевым поведением (подбор на улице, сложности дома)',
         'leash': 'Тянет поводок',
         'hearing': 'Проблемы с послушанием и командами',
         'else': 'Другое...',
         'next': 'next'
         }
        if ans[callback.data] != 'next':
            data['problem'] += f'; {ans[callback.data]}'
            
            text = f"{show_created_check_info(name=data['name'], surname=data['surname'], patronymic=data['patronymic'], birthday=data['birthday'], email=data['email'], education=data['education'], other_education=data['other_education'], communities=data['communities'], practice_date=data['practice_date'], online_work=data['online_work'], supervised=data['supervised'], other_interests=data['other_interests'], kinolog_site=data['kinolog_site'], motivation=data[ 'motivation'], work_stages=data['work_stages'], dog_teaching=data['dog_teaching'], influenced_by=data['influenced_by'],punishment=data['punishment'], punishment_effect=data['punishment_effect'], ammunition=data['ammunition'], other_activities=data['other_activities'], work_methods=data['work_methods'], choice_importance=data['choice_importance'], training_situation=data['training_situation'], advise=data['advise'])}"
            text += "\n\n<b>Вы можете выбрать до трех проблем собаки, которые хотели бы решить. Выберите третью:</b>"
            reply_markup  = get_ikb_problem_optional()
            await bot.edit_message_text(chat_id=callback.from_user.id, text=text, reply_markup=reply_markup, message_id=data['msg_id'], parse_mode=telegram.constants.ParseMode.HTML)
            await KinologFormStatesGroup.next()
        elif ans[callback.data] == 'next':
            text = '\n\n<b>Что хотите делать:</b>'
            text += f"{show_created_check_info(name=data['name'], surname=data['surname'], patronymic=data['patronymic'], birthday=data['birthday'], email=data['email'], education=data['education'], other_education=data['other_education'], communities=data['communities'], practice_date=data['practice_date'], online_work=data['online_work'], supervised=data['supervised'], other_interests=data['other_interests'], kinolog_site=data['kinolog_site'], motivation=data[ 'motivation'], work_stages=data['work_stages'], dog_teaching=data['dog_teaching'], influenced_by=data['influenced_by'],punishment=data['punishment'], punishment_effect=data['punishment_effect'], ammunition=data['ammunition'], other_activities=data['other_activities'], work_methods=data['work_methods'], choice_importance=data['choice_importance'], training_situation=data['training_situation'], advise=data['advise'], problem=data['problem'])}"
            await bot.send_message(chat_id=callback.from_user.id, text=text, reply_markup=get_ikb_confirm_form(), parse_mode=telegram.constants.ParseMode.HTML)
            await KinologFormStatesGroup.next()
            await KinologFormStatesGroup.form_confirm.set()


async def form_load_kinolog_last_problem(callback:types.CallbackQuery, state:FSMContext):
    async with state.proxy() as data:
        ans = {'agression': 'Агрессия по отношению к другим собакам/животным',
         'barking': 'Лай на звуки/дверь и тревожность дома',
         'behaviour': 'Деструктивное поведение (порча вещей, дефекция и тд)',
         'hyper': 'Гиперактивность (копание, прыгучесть и тд)',
         'anxiety': 'Сепарационная тревога (скулит или воет, когда оставляют одного / уходят)',
         'tension': 'Подавленное состояние животного без медицинских причин',
         'agression_people': 'Агрессия ко мне и/или другим людям',
         'fear': 'Страх других животных / собак',
         'food': 'Проблемы с пищевым поведением (подбор на улице, сложности дома)',
         'leash': 'Тянет поводок',
         'hearing': 'Проблемы с послушанием и командами',
         'else': 'Другое...',
         'next': 'next'
         }
        if ans[callback.data] != 'next': 
            data['problem'] += f'; {ans[callback.data]}'

        if data['change'] == 0:
            text = f"{show_created_check_info(name=data['name'], surname=data['surname'], patronymic=data['patronymic'], birthday=data['birthday'], email=data['email'], education=data['education'], other_education=data['other_education'], communities=data['communities'], practice_date=data['practice_date'], online_work=data['online_work'], supervised=data['supervised'], other_interests=data['other_interests'], kinolog_site=data['kinolog_site'], motivation=data[ 'motivation'], work_stages=data['work_stages'], dog_teaching=data['dog_teaching'], influenced_by=data['influenced_by'],punishment=data['punishment'], punishment_effect=data['punishment_effect'], ammunition=data['ammunition'], other_activities=data['other_activities'], work_methods=data['work_methods'], choice_importance=data['choice_importance'], training_situation=data['training_situation'], advise=data['advise'], problem=data['problem'])}"
            text += '\n\n<b>Что хотите делать:</b>'
            await bot.send_message(chat_id=callback.from_user.id, text=text, reply_markup=get_ikb_confirm_form(), parse_mode=telegram.constants.ParseMode.HTML)
            await KinologFormStatesGroup.next()
        else:
            text = f"{show_created_check_info(name=data['name'], surname=data['surname'], patronymic=data['patronymic'], birthday=data['birthday'], email=data['email'], education=data['education'], other_education=data['other_education'], communities=data['communities'], practice_date=data['practice_date'], online_work=data['online_work'], supervised=data['supervised'], other_interests=data['other_interests'], kinolog_site=data['kinolog_site'], motivation=data[ 'motivation'], work_stages=data['work_stages'], dog_teaching=data['dog_teaching'], influenced_by=data['influenced_by'],punishment=data['punishment'], punishment_effect=data['punishment_effect'], ammunition=data['ammunition'], other_activities=data['other_activities'], work_methods=data['work_methods'], choice_importance=data['choice_importance'], training_situation=data['training_situation'], advise=data['advise'], problem=data['problem'])}"
            text += '\n\n<b>Что еще вы хотите изменить:</b>'            
            await bot.send_message(chat_id=callback.from_user.id, text=text, reply_markup=get_ikb_change_form(), parse_mode=telegram.constants.ParseMode.HTML)
            await KinologFormStatesGroup.change_form.set()

async def form_load_confirm(callback:types.CallbackQuery, state:FSMContext):
    async with state.proxy() as data:
        await bot.delete_message(chat_id=callback.from_user.id, message_id=callback.message.message_id)

        if callback.data == "send":
            new_kinolog(chat_id=callback.from_user.id, name=data['name'], surname=data['surname'], patronymic=data['patronymic'], birthday=data['birthday'], email=data['email'],
                       education=data['education'], other_education=data['other_education'], communities=data['communities'],
                       practice_date=data['practice_date'], online_work=data['online_work'], supervised=data['supervised'],
                       other_interests=data['other_interests'], kinolog_site=data['kinolog_site'], motivation=data['motivation'],
                       work_stages=data['work_stages'], dog_teaching=data['dog_teaching'], influenced_by=data['influenced_by'],
                       punishment=data['punishment'], punishment_effect=data['punishment_effect'], ammunition=data['ammunition'],
                       other_activities=data['other_activities'], work_methods=data['work_methods'],
                       choice_importance=data['choice_importance'], training_situation=data['training_situation'], advise=data['advise'], problem=data['problem'])
            text = 'Спасибо, что заполнили анкету!\nЧерез некоторое время мы пришлем ответ на почту с дальнейшими действиями.\n\nНажимайте /start чтобы снова начинать'
            await bot.send_message(chat_id=callback.from_user.id, text=text)
            await GeneralStates.start.set()
        elif callback.data == "change":
            
            text = f"{show_created_check_info(name=data['name'], surname=data['surname'], patronymic=data['patronymic'], birthday=data['birthday'], email=data['email'], education=data['education'], other_education=data['other_education'], communities=data['communities'], practice_date=data['practice_date'], online_work=data['online_work'], supervised=data['supervised'], other_interests=data['other_interests'], kinolog_site=data['kinolog_site'], motivation=data[ 'motivation'], work_stages=data['work_stages'], dog_teaching=data['dog_teaching'], influenced_by=data['influenced_by'],punishment=data['punishment'], punishment_effect=data['punishment_effect'], ammunition=data['ammunition'], other_activities=data['other_activities'], work_methods=data['work_methods'], choice_importance=data['choice_importance'], training_situation=data['training_situation'], advise=data['advise'], problem=data['problem'])}"
            text += '\n\n<b>Что именно вы хотите изменить:</b>'
            msg = await bot.send_message(chat_id=callback.from_user.id, text=text, reply_markup=get_ikb_change_form(), parse_mode=telegram.constants.ParseMode.HTML)
            data['msg_id'] = msg.message_id
            await KinologFormStatesGroup.next()
        elif callback.data == "go_to_start":
            welcome_msg = "Привет! Это бот для заполнения анкеты кинологом или поиска кинолога владельцем собаки. \nЕсли хотите зарегистрироваться, то нажимайте кнопку ниже"
            await bot.send_message(chat_id=callback.from_user.id, text=welcome_msg, reply_markup=get_ikb_registration())
            await GeneralStates.registration.set()

async def form_load_edit(message:types.Message, state:FSMContext):
    async with state.proxy() as data:
        data[data['field']] = message.text

        if data['field'] not in ['name', 'surname']:
            await bot.delete_message(chat_id=message.from_user.id, message_id=message.message_id)
            
            text = f"{show_created_check_info(name=data['name'], surname=data['surname'], patronymic=data['patronymic'], birthday=data['birthday'], email=data['email'], education=data['education'], other_education=data['other_education'], communities=data['communities'], practice_date=data['practice_date'], online_work=data['online_work'], supervised=data['supervised'], other_interests=data['other_interests'], kinolog_site=data['kinolog_site'], motivation=data[ 'motivation'], work_stages=data['work_stages'], dog_teaching=data['dog_teaching'], influenced_by=data['influenced_by'],punishment=data['punishment'], punishment_effect=data['punishment_effect'], ammunition=data['ammunition'], other_activities=data['other_activities'], work_methods=data['work_methods'], choice_importance=data['choice_importance'], training_situation=data['training_situation'], advise=data['advise'], problem=data['problem'])}"
            text += '\n\n<b>Что еще вы хотите изменить:</b>'
            await bot.edit_message_text(chat_id=message.from_user.id, text=text, reply_markup=get_ikb_change_form(), message_id=data['msg_id'], parse_mode=telegram.constants.ParseMode.HTML)
            await KinologFormStatesGroup.change_form.set()
        elif data['field'] == 'name':
            await bot.delete_message(chat_id=message.from_user.id, message_id=message.message_id)
            
            text = f"{show_created_check_info(name=data['name'], surname=data['surname'], patronymic=data['patronymic'], birthday=data['birthday'], email=data['email'], education=data['education'], other_education=data['other_education'], communities=data['communities'], practice_date=data['practice_date'], online_work=data['online_work'], supervised=data['supervised'], other_interests=data['other_interests'], kinolog_site=data['kinolog_site'], motivation=data[ 'motivation'], work_stages=data['work_stages'], dog_teaching=data['dog_teaching'], influenced_by=data['influenced_by'],punishment=data['punishment'], punishment_effect=data['punishment_effect'], ammunition=data['ammunition'], other_activities=data['other_activities'], work_methods=data['work_methods'], choice_importance=data['choice_importance'], training_situation=data['training_situation'], advise=data['advise'], problem=data['problem'])}"
            text += '\n\n<b>Напишите вашу фамилию:</b>'
            await bot.edit_message_text(chat_id=message.from_user.id, text=text, message_id=data['msg_id'], parse_mode=telegram.constants.ParseMode.HTML)
            await KinologFormStatesGroup.surname.set()

async def form_load_change(callback:types.CallbackQuery, state:FSMContext):
    async with state.proxy() as data:
        if callback.data == "send":
            await bot.delete_message(chat_id=callback.from_user.id, message_id=callback.message.message_id)
            new_kinolog(chat_id=callback.from_user.id, name=data['name'], surname=data['surname'], patronymic=data['patronymic'], birthday=data['birthday'], email=data['email'],
                       education=data['education'], other_education=data['other_education'], communities=data['communities'],
                       practice_date=data['practice_date'], online_work=data['online_work'], supervised=data['supervised'],
                       other_interests=data['other_interests'], kinolog_site=data['kinolog_site'], motivation=data['motivation'],
                       work_stages=data['work_stages'], dog_teaching=data['dog_teaching'], influenced_by=data['influenced_by'],
                       punishment=data['punishment'], punishment_effect=data['punishment_effect'], ammunition=data['ammunition'],
                       other_activities=data['other_activities'], work_methods=data['work_methods'],
                       choice_importance=data['choice_importance'], training_situation=data['training_situation'], advise=data['advise'], problem=data['problem'])
            text = 'Спасибо, что заполнили анкету!\nЧерез некоторое время мы пришлем ответ на почту с дальнейшими действиями.\n\nНажимайте /start чтобы снова начинать'
            await bot.send_message(chat_id=callback.from_user.id, text=text)
            await GeneralStates.start.set()
        elif callback.data == "change_all":
            await bot.delete_message(chat_id=callback.from_user.id, message_id=callback.message.message_id)
            data['change'] = 0
            text = '<b>Напишите ваше имя:</b>'
            msg = await bot.send_message(chat_id=callback.from_user.id, text=text, parse_mode=telegram.constants.ParseMode.HTML)
            data['msg_id'] = msg.message_id
            await KinologFormStatesGroup.name.set()
        elif callback.data == "go_to_start":
            await bot.delete_message(chat_id=callback.from_user.id, message_id=callback.message.message_id)
            welcome_msg = "Привет! Это бот для заполнения анкеты кинологом или поиска кинолога владельцем собаки. \nЕсли хотите зарегистрироваться, то нажимайте кнопку ниже"
            await bot.send_message(chat_id=callback.from_user.id, text=welcome_msg, reply_markup=get_ikb_registration())
            await GeneralStates.registration.set()
        else:
            # data['msg_id'] = callback.message.message_id
            data['change'] = 1
            ans = {
                '1': 'name',
                '2': 'birthday',
                '3': 'email',
                '4': 'education',
                '5': 'other_education',
                '6': 'communities',
                '7': 'practice_date',
                '8': 'online_work',
                '9': 'supervised',
                '10': 'other_interests',
                '11': 'kinolog_site',
                '12': 'motivation',
                '13': 'work_stages',
                '14': 'dog_teaching',
                '15': 'influenced_by',
                '16': 'punishment',
                '17': 'punishment_effect',
                '18': 'ammunition',
                '19': 'other_activities',
                '20': 'work_methods',
                '21': 'choice_importance',
                '22': 'training_situation',
                '23': 'advise',
                '24': 'problem'
            }
            
            ans_text = {
                '1': "Напишите ваше имя:",
                '3': "Напишите вашу почту:",
                '4': "Какое у вас высшее образование?",
                '5': "Пожалуйста, перечислите все курсы или дополнительное образование (семинары, повышение квалификации, вебинары), которые вы прошли/прослушали:",
                '6': "Состоите ли вы в каких-либо профессиональных сообществах, ассоциациях? Если да, то в каких?",
                '7': "Когда вы начали свою кинологическую практику? Укажите месяц и год",
                '8': "Есть ли опыт работы онлайн? Если да, сколько лет?",
                '10': "Есть ли другая работа кроме специалиста по поведению собак? Как распределяются интересы и приоритеты?",
                '11': "Если у вас есть сайт с вашими услугами, пожалуйста, поделитесь им ниже",
                '12': "Теперь вопросы про ваш опыт и взаимодействия с собаками\nЧто вас мотивирует к работе с собаками и людьми?",
                '13': "Расскажите, каким образом обычно выглядит ваша работа с клиентом? Как вы работаете? Перечислите поэтапно.",
                '14': "Как вам кажется, чему наиболее важно научить собаку? Пожалуйста, перечислите не более 4 пунктов.",
                '15': "Как вам кажется, кто в большей степени повлиял на вас или вдохновил вас с точки зрения работы с собаками?",
                '16': "Что вы считаете наказанием в работе с собаками?",
                '17': "Какое влияние может иметь наказание на собак?",
                '18': "Какую амуницию вы используете в работе и рекомендуете? Почему?",
                '19': "Есть ли какие-нибудь игры или занятия, которые вы проводите со своими собаками, клиентами или рекомендуете клиентам? Почему?",
                '20': "Используете ли вы или рекомендуете какие-то конкретные методики или протоколы в работе с собаками? Почему?",
                '21': "Почему выбор может быть важной частью или относиться к работе с собаками?",
                '22': "Что бы вы сделали, если бы столкнулись с ситуацией, связанной с дрессировкой собаки, которую вы изо всех сил пытались решить или разобрать?",
                '23': "Если не учитывать особенности отдельно взятой собаки, что бы вы могли посоветовать всем владельцам собак?",
            }
            data['field'] = ans[callback.data]

            if callback.data not in ['2', '9', '24']:
                await bot.delete_message(chat_id=callback.from_user.id, message_id=callback.message.message_id)
                msg = await bot.send_message(chat_id=callback.from_user.id, text=ans_text[callback.data], parse_mode=telegram.constants.ParseMode.HTML)
                data['msg_id'] = msg.message_id
                await KinologFormStatesGroup.edit_form.set()
            elif callback.data == '2':
                await bot.delete_message(chat_id=callback.from_user.id, message_id=callback.message.message_id)

                calendar, step = DetailedTelegramCalendar(max_date=date(2022,1,1)).build()
                await bot.send_message(chat_id=callback.from_user.id,text=
                            f"Выберите день рождения: {LSTEP[step]}",
                            reply_markup=calendar)
                await KinologFormStatesGroup.birthday.set()
            elif callback.data == '9':
                await bot.delete_message(chat_id=callback.from_user.id, message_id=callback.message.message_id)
                
                text = f"{show_created_check_info(name=data['name'], surname=data['surname'], patronymic=data['patronymic'], birthday=data['birthday'], email=data['email'], education=data['education'], other_education=data['other_education'], communities=data['communities'], practice_date=data['practice_date'], online_work=data['online_work'], supervised=data['supervised'], other_interests=data['other_interests'], kinolog_site=data['kinolog_site'], motivation=data[ 'motivation'], work_stages=data['work_stages'], dog_teaching=data['dog_teaching'], influenced_by=data['influenced_by'],punishment=data['punishment'], punishment_effect=data['punishment_effect'], ammunition=data['ammunition'], other_activities=data['other_activities'], work_methods=data['work_methods'], choice_importance=data['choice_importance'], training_situation=data['training_situation'], advise=data['advise'], problem=data['problem'])}"
                text += '\n\n<b>Проходите ли вы супервизии?</b>'
                reply_markup  = get_ikb_supervised()
                msg = await bot.send_message(chat_id=callback.from_user.id, text=text, reply_markup=reply_markup, parse_mode=telegram.constants.ParseMode.HTML)
                data['msg_id'] = msg.message_id
                await KinologFormStatesGroup.supervised.set()
            else:
                
                text = f"{show_created_check_info(name=data['name'], surname=data['surname'], patronymic=data['patronymic'], birthday=data['birthday'], email=data['email'], education=data['education'], other_education=data['other_education'], communities=data['communities'], practice_date=data['practice_date'], online_work=data['online_work'], supervised=data['supervised'], other_interests=data['other_interests'], kinolog_site=data['kinolog_site'], motivation=data[ 'motivation'], work_stages=data['work_stages'], dog_teaching=data['dog_teaching'], influenced_by=data['influenced_by'],punishment=data['punishment'], punishment_effect=data['punishment_effect'], ammunition=data['ammunition'], other_activities=data['other_activities'], work_methods=data['work_methods'], choice_importance=data['choice_importance'], training_situation=data['training_situation'], advise=data['advise'], problem=data['problem'])}"
                text += "\n\n<b>Какие проблемы собаки вы бы хотели решать?</b>"
                reply_markup  = get_ikb_problem()
                await bot.edit_message_text(chat_id=callback.from_user.id, text=text, message_id=callback.message.message_id, reply_markup=reply_markup, parse_mode=telegram.constants.ParseMode.HTML)
                await KinologFormStatesGroup.problem.set()


async def card_load_photo_callback_query(callback: types.CallbackQuery, state: FSMContext):
    if callback.data == "back":
        await bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)
        text = 'Это интерфейс одобренного кинолога. \nЧто вы хотите делать дальше:'
        await bot.send_message(chat_id=callback.from_user.id, text=text, reply_markup=get_ikb_kinolog_card())
        await GeneralStates.kinolog.set()

async def card_load_photo_message(message: types.Message, state: FSMContext):
    if message.photo[0].file_id:
        await bot.delete_message(chat_id=message.from_user.id, message_id=message.message_id)
        async with state.proxy() as data:
            data['photo'] = message.photo[0].file_id

            text = 'Расскажите немного о себе, чтобы потенциальные клиенты лучше могли вас узнать:'
            await bot.edit_message_text(chat_id=message.from_user.id, text=text, message_id=data['msg_id'])
            await KinologFormStatesGroup.intro.set()

async def card_load_intro(message:types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['intro'] = message.text

        await bot.delete_message(chat_id=message.from_user.id, message_id=data['msg_id'])
        await bot.delete_message(chat_id=message.from_user.id, message_id=message.message_id)
        await bot.send_photo(photo=data['photo'], chat_id=message.from_user.id, caption=data['intro'], reply_markup=get_ikb_send_card())
        await KinologFormStatesGroup.next()


async def card_load_confirm(callback:types.CallbackQuery, state:FSMContext):
    async with state.proxy() as data:
        if callback.data == "send":
            await bot.delete_message(chat_id=callback.from_user.id, message_id=callback.message.message_id)
            update_kinolog_card(chat_id=callback.from_user.id, photo=data['photo'], intro=data['intro'])
            text = "Спасибо, что заполнили карту! \nНапишите /start чтобы начинать работать снова с ботом"
            await bot.send_message(chat_id=callback.from_user.id, text=text)
        elif callback.data == "back":
            await bot.delete_message(chat_id=callback.from_user.id, message_id=callback.message.message_id)
            text = 'Расскажите немного о себе, чтобы потенциальные клиенты лучше могли вас узнать:'
            msg = await bot.send_message(chat_id=callback.from_user.id, text=text)
            data['msg_id'] = msg.message_id
            await KinologFormStatesGroup.intro.set()
        elif callback.data == "go_to_start":
            await bot.delete_message(chat_id=callback.from_user.id, message_id=callback.message.message_id)
            welcome_msg = "Привет! Это бот для заполнения анкеты кинологом или поиска кинолога владельцем собаки. \nЕсли хотите зарегистрироваться, то нажимайте кнопку ниже"
            await bot.send_message(chat_id=callback.from_user.id, text=welcome_msg, reply_markup=get_ikb_registration())
            await GeneralStates.registration.set()
    

def register_main_handlers_kinolog(dp: Dispatcher) -> None:
    dp.register_callback_query_handler(start_form_kinolog, state=GeneralStates.kinolog)
    dp.register_message_handler(form_load_kinolog_name, state=KinologFormStatesGroup.name)
    dp.register_message_handler(form_load_kinolog_surname, state=KinologFormStatesGroup.surname)
    dp.register_message_handler(form_load_kinolog_patronymic, state=KinologFormStatesGroup.patronymic)
    dp.register_callback_query_handler(form_load_kinolog_birthday, state=KinologFormStatesGroup.birthday)
    dp.register_message_handler(form_load_kinolog_email, state=KinologFormStatesGroup.email)
    dp.register_message_handler(form_load_kinolog_education, state=KinologFormStatesGroup.education)
    dp.register_message_handler(form_load_kinolog_other_education, state=KinologFormStatesGroup.other_education)
    dp.register_message_handler(form_load_kinolog_communities, state=KinologFormStatesGroup.communities)
    dp.register_message_handler(form_load_kinolog_practice_date, state=KinologFormStatesGroup.practice_date)
    dp.register_message_handler(form_load_kinolog_online_work, state=KinologFormStatesGroup.online_work)
    dp.register_callback_query_handler(form_load_kinolog_supervised, state=KinologFormStatesGroup.supervised)
    dp.register_message_handler(form_load_kinolog_other_interests, state=KinologFormStatesGroup.other_interests)
    dp.register_message_handler(form_load_kinolog_site, state=KinologFormStatesGroup.kinolog_site)
    dp.register_message_handler(form_load_kinolog_motivation, state=KinologFormStatesGroup.motivation)
    dp.register_message_handler(form_load_kinolog_work_stages, state=KinologFormStatesGroup.work_stages)
    dp.register_message_handler(form_load_kinolog_dog_teaching, state=KinologFormStatesGroup.dog_teaching)
    dp.register_message_handler(form_load_kinolog_influenced_by, state=KinologFormStatesGroup.influenced_by)
    dp.register_message_handler(form_load_kinolog_punishment, state=KinologFormStatesGroup.punishment)
    dp.register_message_handler(form_load_kinolog_punishment_effect, state=KinologFormStatesGroup.punishment_effect)
    dp.register_message_handler(form_load_kinolog_ammunition, state=KinologFormStatesGroup.ammunition)
    dp.register_message_handler(form_load_kinolog_other_activities, state=KinologFormStatesGroup.other_activities)
    dp.register_message_handler(form_load_kinolog_work_methods, state=KinologFormStatesGroup.work_methods)
    dp.register_message_handler(form_load_kinolog_choice_importance, state=KinologFormStatesGroup.choice_importance)
    dp.register_message_handler(form_load_kinolog_training_situation, state=KinologFormStatesGroup.training_situation)
    dp.register_message_handler(form_load_kinolog_advise, state=KinologFormStatesGroup.advise)
    dp.register_callback_query_handler(form_load_kinolog_first_problem, state=KinologFormStatesGroup.problem)
    dp.register_callback_query_handler(form_load_kinolog_second_problem, state=KinologFormStatesGroup.problem2)
    dp.register_callback_query_handler(form_load_kinolog_last_problem, state=KinologFormStatesGroup.problem3)
    dp.register_callback_query_handler(form_load_confirm, state=KinologFormStatesGroup.form_confirm)
    dp.register_callback_query_handler(form_load_change, state=KinologFormStatesGroup.change_form)
    dp.register_message_handler(form_load_edit, state=KinologFormStatesGroup.edit_form)
    dp.register_message_handler(card_load_photo_message, state=KinologFormStatesGroup.photo, content_types=types.ContentType.PHOTO)
    dp.register_callback_query_handler(card_load_photo_callback_query, state=KinologFormStatesGroup.photo)
    dp.register_message_handler(card_load_intro, state=KinologFormStatesGroup.intro)
    dp.register_callback_query_handler(card_load_confirm, state=KinologFormStatesGroup.card_confirm)
