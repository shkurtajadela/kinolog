from aiogram import types
from aiogram.dispatcher import FSMContext
from .app import dp, bot
from .keyboards import get_ikb_supervised, get_ikb_problem, get_ikb_choose_kinolog_back, get_ikb_registration, get_ikb_send_card 
from aiogram import types, Dispatcher
from .states import KinologFormStatesGroup, GeneralStates
from bot.db.db_interface import new_kinolog, update_kinolog_card, get_form_status, get_kinolog
from datetime import datetime
from telegram_bot_calendar import DetailedTelegramCalendar, LSTEP
from datetime import date

async def start_form_kinolog(callback:types.CallbackQuery, state:FSMContext):
    await bot.delete_message(chat_id=callback.from_user.id, message_id=callback.message.message_id)
    if callback.data == "card":
        text="Загрузите ваше фото"
        await bot.send_message(chat_id=callback.from_user.id, text=text, reply_markup=get_ikb_choose_kinolog_back())
        await KinologFormStatesGroup.photo.set()
    elif callback.data == "form":
        text = "Напишите ваше имя:"
        await bot.send_message(chat_id=callback.from_user.id, text=text)
        await KinologFormStatesGroup.name.set()
    elif callback.data == "back":
        welcome_msg = "Привет! Это бот для заполнения анкеты кинологом или поиска кинолога владельцем собаки. \nЕсли хотите зарегистрироваться, то нажимайте кнопку ниже"
        await bot.send_message(chat_id=callback.from_user.id, text=welcome_msg, reply_markup=get_ikb_registration())
        await GeneralStates.registration.set()

async def form_load(message:types.Message, state:FSMContext, field: str, text: str):
    async with state.proxy() as data:
        data[field] = message.text

        await bot.send_message(chat_id=message.from_user.id, text=text)
        await KinologFormStatesGroup.next()

async def form_load_kinolog_name(message:types.Message, state:FSMContext):
    await form_load(message, state, 'name', 'Напишите вашу фамилию:')

async def form_load_kinolog_surname(message:types.Message, state:FSMContext):
    await form_load(message, state, 'surname', 'Напишите ваше отчество:')

async def form_load_kinolog_patronymic(message:types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['patronymic'] = message.text

        calendar, step = DetailedTelegramCalendar(max_date=date(2022,1,1)).build()
        await bot.send_message(message.from_user.id,
                     f"Выберите день рождения: {LSTEP[step]}",
                     reply_markup=calendar)
        await KinologFormStatesGroup.next()

async def form_load_kinolog_birthday(callback:types.CallbackQuery, state:FSMContext):
    result, key, step = DetailedTelegramCalendar(max_date=date(2022,1,1)).process(callback.data)
    if not result and key:
        await bot.edit_message_text(f"Выберите день рождения: {LSTEP[step]}",
                            callback.message.chat.id,
                            callback.message.message_id,
                            reply_markup=key)
    elif result:
        async with state.proxy() as data:
            data['birthday'] = result
        
            text = 'Write your email?'
            await bot.send_message(chat_id=callback.from_user.id, text=text)
            await KinologFormStatesGroup.next()

        
async def form_load_kinolog_email(message:types.Message, state:FSMContext):
    await form_load(message, state, 'email', 'Какое у вас высшее образование?')


async def form_load_kinolog_education(message:types.Message, state:FSMContext):
    text = 'Пожалуйста, перечислите все курсы или дополнительное образование (семинары, повышение квалификации, вебинары), которые вы прошли/прослушали:'
    await form_load(message, state, 'education', text)

async def form_load_kinolog_other_education(message:types.Message, state:FSMContext):
    text = 'Состоите ли вы в каких-либо профессиональных сообществах, ассоциациях? Если да, то в каких?'
    await form_load(message, state, 'other_education', text)


async def form_load_kinolog_communities(message:types.Message, state:FSMContext):
    text = 'Когда вы начали свою кинологическую практику? Укажите месяц и год.'
    await form_load(message, state, 'communities', text)



async def form_load_kinolog_practice_date(message:types.Message, state:FSMContext):
    text = 'Есть ли опыт работы онлайн? Если да, сколько лет?'
    await form_load(message, state, 'practice_date', text)



async def form_load_kinolog_online_work(message:types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['online_work'] = message.text

        text = 'Проходите ли вы супервизии?'
        reply_markup  = get_ikb_supervised()
        await bot.send_message(chat_id=message.from_user.id, text=text, reply_markup=reply_markup)
        await KinologFormStatesGroup.next()


async def form_load_kinolog_supervised(callback:types.CallbackQuery, state:FSMContext):
    async with state.proxy() as data:
        ans = {'no_supervised': 'Нет, никогда не проходил(а)',
         'before_supervised': 'Да, проходил(а) когда-то, сейчас не прохожу',
         'rarely_supervised': 'Да, прохожу редко (раз в несколько месяцев)',
         'usually_supervised': 'Да, прохожу постоянно (раз в месяц и чаще)'
         }
        data['supervised'] = ans[callback.data]

        text = 'Есть ли другая работа кроме специалиста по поведению собак? Как распределяются интересы и приоритеты?'
        await bot.send_message(chat_id=callback.from_user.id, text=text)
        await KinologFormStatesGroup.next()


async def form_load_kinolog_other_interests(message:types.Message, state:FSMContext):
    text = 'Если у вас есть сайт с вашими услугами, пожалуйста, поделитесь им ниже'
    await form_load(message, state, 'other_interests', text)


async def form_load_kinolog_site(message:types.Message, state:FSMContext):
    text = 'Теперь вопросы про ваш опыт и взаимодействия с собаками\nЧто вас мотивирует к работе с собаками и людьми?'
    await form_load(message, state, 'kinolog_site', text)

async def form_load_kinolog_motivation(message:types.Message, state:FSMContext):
    text = 'Расскажите, каким образом обычно выглядит ваша работа с клиентом? Как вы работаете? Перечислите поэтапно.'
    await form_load(message, state, 'motivation', text)


async def form_load_kinolog_work_stages(message:types.Message, state:FSMContext):
    text = 'Как вам кажется, чему наиболее важно научить собаку? Пожалуйста, перечислите не более 4 пунктов.'
    await form_load(message, state, 'work_stages', text)


async def form_load_kinolog_dog_teaching(message:types.Message, state:FSMContext):
    text = 'Как вам кажется, кто в большей степени повлиял на вас или вдохновил вас с точки зрения работы с собаками?'
    await form_load(message, state, 'dog_teaching', text)


async def form_load_kinolog_influenced_by(message:types.Message, state:FSMContext):
    text = 'Что вы считаете наказанием в работе с собаками?'
    await form_load(message, state, 'influenced_by', text)


async def form_load_kinolog_punishment(message:types.Message, state:FSMContext):
    text = 'Какое влияние может иметь наказание на собак?'
    await form_load(message, state, 'punishment', text)


async def form_load_kinolog_punishment_effect(message:types.Message, state:FSMContext):
    text = 'Какую амуницию вы используете в работе и рекомендуете? Почему?'
    await form_load(message, state, 'punishment_effect', text)


async def form_load_kinolog_ammunition(message:types.Message, state:FSMContext):
    text = 'Есть ли какие-нибудь игры или занятия, которые вы проводите со своими собаками, клиентами или рекомендуете клиентам? Почему?'
    await form_load(message, state, 'ammunition', text)


async def form_load_kinolog_other_activities(message:types.Message, state:FSMContext):
    text = 'Используете ли вы или рекомендуете какие-то конкретные методики или протоколы в работе с собаками? Почему?'
    await form_load(message, state, 'other_activities', text)

async def form_load_kinolog_work_methods(message:types.Message, state:FSMContext):
    text = 'Почему выбор может быть важной частью или относиться к работе с собаками?'
    await form_load(message, state, 'work_methods', text)

async def form_load_kinolog_choice_importance(message:types.Message, state:FSMContext):
    text = 'Что бы вы сделали, если бы столкнулись с ситуацией, связанной с дрессировкой собаки, которую вы изо всех сил пытались решить или разобрать?'
    await form_load(message, state, 'choice_importance', text)

async def form_load_kinolog_training_situation(message:types.Message, state:FSMContext):
    text = 'Если не учитывать особенности отдельно взятой собаки, что бы вы могли посоветовать всем владельцам собак?'
    await form_load(message, state, 'training_situation', text)

async def form_load_kinolog_advise(message:types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['advise'] = message.text

        text = "Какие проблемы собаки вы бы хотели решать?"
        reply_markup  = get_ikb_problem()
        await bot.send_message(chat_id=message.from_user.id, text=text, reply_markup=reply_markup)
        await KinologFormStatesGroup.next()

async def form_load_kinolog_problem(callback:types.CallbackQuery, state:FSMContext):
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

        new_kinolog(chat_id=callback.from_user.id, name=data['name'], surname=data['surname'], patronymic=data['patronymic'], birthday=data['birthday'], email=data['email'],
                       education=data['education'], other_education=data['other_education'], communities=data['communities'],
                       practice_date=data['practice_date'], online_work=data['online_work'], supervised=data['supervised'],
                       other_interests=data['other_interests'], kinolog_site=data['kinolog_site'], motivation=data['motivation'],
                       work_stages=data['work_stages'], dog_teaching=data['dog_teaching'], influenced_by=data['influenced_by'],
                       punishment=data['punishment'], punishment_effect=data['punishment_effect'], ammunition=data['ammunition'],
                       other_activities=data['other_activities'], work_methods=data['work_methods'],
                       choice_importance=data['choice_importance'], training_situation=data['training_situation'], advise=data['advise'], problem=ans[callback.data])
        text = 'Спасибо что заполнили анкету!\nЕсли ваш опыт и образование подходят, мы пригласим вас на следующий этап. После этого мы попросим вас прислать вас видео, возможно, с вашего занятия о том, как вы гуляете с собакой или занимаетесь с клиентской собакой.'
        await bot.send_message(chat_id=callback.from_user.id, text=text)
        await GeneralStates.start.set()

async def card_load_photo(message:types.Message, state:FSMContext, callback:types.CallbackQuery = None):

    if callback and callback.data != "back":
        await bot.delete_message(chat_id=callback.from_user.id, message_id=callback.message.message_id)

        welcome_msg = "Привет! Это бот для заполнения анкеты кинологом или поиска кинолога владельцем собаки. \nЕсли хотите зарегистрироваться, то нажимайте кнопку ниже"
        await bot.send_message(chat_id=callback.from_user.id, text=welcome_msg, reply_markup=get_ikb_registration())
        await GeneralStates.registration.set()
    elif message.photo[0].file_id:
        await bot.delete_message(chat_id=message.from_user.id, message_id=message.message_id)
        async with state.proxy() as data:
            data['photo'] = message.photo[0].file_id

            text = 'Расскажите немного о себе, чтобы потенциальные клиенты лучше могли вас узнать:'
            await bot.send_message(chat_id=message.from_user.id, text=text)
            await KinologFormStatesGroup.next()
        

async def card_load_intro(message:types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['intro'] = message.text

        await bot.delete_message(chat_id=message.from_user.id, message_id=message.message_id)
        await bot.send_photo(photo=data['photo'], chat_id=message.from_id, caption=data['intro'], reply_markup=get_ikb_send_card())
        await KinologFormStatesGroup.next()


async def card_load_confirm(callback:types.CallbackQuery, state:FSMContext):
    async with state.proxy() as data:
        if callback.data == "send":
            await bot.delete_message(chat_id=callback.from_user.id, message_id=callback.message.message_id)
            update_kinolog_card(chat_id=callback.from_user.id, photo=data['photo'], intro=data['intro'])
            text = "Спасибо, что заполнили карту! "
            await bot.send_message(chat_id=callback.from_user.id, text=text)
        elif callback.data == "back":
            await bot.delete_message(chat_id=callback.from_user.id, message_id=callback.message.message_id)
            text = 'Расскажите немного о себе, чтобы потенциальные клиенты лучше могли вас узнать:'
            await bot.send_message(chat_id=callback.from_user.id, text=text)
            await KinologFormStatesGroup.intro.set()


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
    dp.register_callback_query_handler(form_load_kinolog_problem, state=KinologFormStatesGroup.problem)
    dp.register_message_handler(card_load_photo, state=KinologFormStatesGroup.photo, content_types=types.ContentType.PHOTO)
    dp.register_message_handler(card_load_intro, state=KinologFormStatesGroup.intro)
    dp.register_callback_query_handler(card_load_confirm, state=KinologFormStatesGroup.card_confirm)
