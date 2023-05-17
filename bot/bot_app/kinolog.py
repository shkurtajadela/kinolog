from aiogram import types
from aiogram.dispatcher import FSMContext
from .app import dp , bot
from .keyboards import inline_kb, kb_kin_q
from .kinolog_form import k_form
from aiogram import types, Dispatcher
from .states import KinologFormStatesGroup, GeneralStates
from bot.db.db_interface import new_kinolog


async def start_form_kinolog(message:types.Message):
    text = "What's your name?"
    await bot.send_message(chat_id=message.from_user.id, text=text)
    await KinologFormStatesGroup.name.set()

async def form_load_kinolog_name(message:types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text

        text = 'Write your surname?'
        await bot.send_message(chat_id=message.from_user.id, text=text)
        await KinologFormStatesGroup.next()

async def form_load_kinolog_surname(message:types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['surname'] = message.text

        text = 'Write your patronymic?'
        await bot.send_message(chat_id=message.from_user.id, text=text)
        await KinologFormStatesGroup.next()


async def form_load_kinolog_patronymic(message:types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['patronymic'] = message.text

        text = 'Write your birthday?'
        await bot.send_message(chat_id=message.from_user.id, text=text)
        await KinologFormStatesGroup.next()


async def form_load_kinolog_birthday(message:types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['birthday'] = message.text

        text = 'Write your email?'
        await bot.send_message(chat_id=message.from_user.id, text=text)
        await KinologFormStatesGroup.next()

async def form_load_kinolog_email(message:types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['email'] = message.text

        text = 'Какое у вас высшее образование?'
        await bot.send_message(chat_id=message.from_user.id, text=text)
        await KinologFormStatesGroup.next()


async def form_load_kinolog_education(message:types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['education'] = message.text

        text = 'Пожалуйста, перечислите все курсы или дополнительное образование (семинары, повышение квалификации, вебинары), которые вы прошли/прослушали:'
        await bot.send_message(chat_id=message.from_user.id, text=text)
        await KinologFormStatesGroup.next()

async def form_load_kinolog_other_education(message:types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['other_education'] = message.text

        text = 'Состоите ли вы в каких-либо профессиональных сообществах, ассоциациях? Если да, то в каких?'
        await bot.send_message(chat_id=message.from_user.id, text=text)
        await KinologFormStatesGroup.next()

async def form_load_kinolog_communities(message:types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['communities'] = message.text

        text = 'Когда вы начали свою кинологическую практику? Укажите месяц и год.'
        await bot.send_message(chat_id=message.from_user.id, text=text)
        await KinologFormStatesGroup.next()


async def form_load_kinolog_practice_date(message:types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['practice_date'] = message.text

        text = 'Есть ли опыт работы онлайн? Если да, сколько лет?'
        await bot.send_message(chat_id=message.from_user.id, text=text)
        await KinologFormStatesGroup.next()


async def form_load_kinolog_online_work(message:types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['online_work'] = message.text

        text = 'Проходите ли вы супервизии?'
        await bot.send_message(chat_id=message.from_user.id, text=text)
        await KinologFormStatesGroup.next()


async def form_load_kinolog_supervised(message:types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['supervised'] = message.text

        text = 'Есть ли другая работа кроме специалиста по поведению собак? Как распределяются интересы и приоритеты?'
        await bot.send_message(chat_id=message.from_user.id, text=text)
        await KinologFormStatesGroup.next()


async def form_load_kinolog_other_interests(message:types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['other_interests'] = message.text

        text = 'Если у вас есть сайт с вашими услугами, пожалуйста, поделитесь им ниже'
        await bot.send_message(chat_id=message.from_user.id, text=text)
        await KinologFormStatesGroup.next()


async def form_load_kinolog_site(message:types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['kinolog_site'] = message.text

        text = 'Теперь вопросы про ваш опыт и взаимодействия с собаками\nЧто вас мотивирует к работе с собаками и людьми?'
        await bot.send_message(chat_id=message.from_user.id, text=text)
        await KinologFormStatesGroup.next()

async def form_load_kinolog_motivation(message:types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['motivation'] = message.text

        text = 'Расскажите, каким образом обычно выглядит ваша работа с клиентом? Как вы работаете? Перечислите поэтапно.'
        await bot.send_message(chat_id=message.from_user.id, text=text)
        await KinologFormStatesGroup.next()

async def form_load_kinolog_work_stages(message:types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['work_stages'] = message.text

        text = 'Как вам кажется, чему наиболее важно научить собаку? Пожалуйста, перечислите не более 4 пунктов.'
        await bot.send_message(chat_id=message.from_user.id, text=text)
        await KinologFormStatesGroup.next()


async def form_load_kinolog_dog_teaching(message:types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['dog_teaching'] = message.text

        text = 'Как вам кажется, кто в большей степени повлиял на вас или вдохновил вас с точки зрения работы с собаками?'
        await bot.send_message(chat_id=message.from_user.id, text=text)
        await KinologFormStatesGroup.next()


async def form_load_kinolog_influenced_by(message:types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['influenced_by'] = message.text

        text = 'Что вы считаете наказанием в работе с собаками?'
        await bot.send_message(chat_id=message.from_user.id, text=text)
        await KinologFormStatesGroup.next()


async def form_load_kinolog_punishment(message:types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['punishment'] = message.text

        text = 'Какое влияние может иметь наказание на собак?'
        await bot.send_message(chat_id=message.from_user.id, text=text)
        await KinologFormStatesGroup.next()


async def form_load_kinolog_punishment_effect(message:types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['punishment_effect'] = message.text

        text = 'Какую амуницию вы используете в работе и рекомендуете? Почему?'
        await bot.send_message(chat_id=message.from_user.id, text=text)
        await KinologFormStatesGroup.next()

async def form_load_kinolog_ammunition(message:types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['ammunition'] = message.text

        text = 'Есть ли какие-нибудь игры или занятия, которые вы проводите со своими собаками, клиентами или рекомендуете клиентам? Почему?'
        await bot.send_message(chat_id=message.from_user.id, text=text)
        await KinologFormStatesGroup.next()

async def form_load_kinolog_other_activities(message:types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['other_activities'] = message.text

        text = 'Используете ли вы или рекомендуете какие-то конкретные методики или протоколы в работе с собаками? Почему?'
        await bot.send_message(chat_id=message.from_user.id, text=text)
        await KinologFormStatesGroup.next()

async def form_load_kinolog_work_methods(message:types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['work_methods'] = message.text

        text = 'Почему выбор может быть важной частью или относиться к работе с собаками?'
        await bot.send_message(chat_id=message.from_user.id, text=text)
        await KinologFormStatesGroup.next()

async def form_load_kinolog_choice_importance(message:types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['choice_importance'] = message.text

        text = 'Что бы вы сделали, если бы столкнулись с ситуацией, связанной с дрессировкой собаки, которую вы изо всех сил пытались решить или разобрать?'
        await bot.send_message(chat_id=message.from_user.id, text=text)
        await KinologFormStatesGroup.next()

async def form_load_kinolog_training_situation(message:types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['training_situation'] = message.text

        text = 'Если не учитывать особенности отдельно взятой собаки, что бы вы могли посоветовать всем владельцам собак?'
        await bot.send_message(chat_id=message.from_user.id, text=text)
        await KinologFormStatesGroup.next()

async def form_load_kinolog_advise(message:types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['advise'] = message.text

        new_kinolog(name=data['name'], surname=data['surname'], patronymic=data['patronymic'], birthday=data['birthday'], email=data['email'],
                       education=data['education'], other_education=data['other_education'], communities=data['communities'],
                       practice_date=data['practice_date'], online_work=data['online_work'], supervised=data['supervised'],
                       other_interests=data['other_interests'], kinolog_site=data['kinolog_site'], motivation=data['motivation'],
                       work_stages=data['work_stages'], dog_teaching=data['dog_teaching'], influenced_by=data['influenced_by'],
                       punishment=data['punishment'], punishment_effect=data['punishment_effect'], ammunition=data['ammunition'],
                       other_activities=data['other_activities'], work_methods=data['work_methods'],
                       choice_importance=data['choice_importance'], training_situation=data['training_situation'], advise=['advise'])
        text = 'Спасибо что заполнили анкету!\nЕсли ваш опыт и образование подходят, мы пригласим вас на следующий этап. После этого мы попросим вас прислать вас видео, возможно, с вашего занятия о том, как вы гуляете с собакой или занимаетесь с клиентской собакой.'
        await bot.send_message(chat_id=message.from_user.id, text=text)
        await GeneralStates.choose_user

def register_main_handlers_kinolog(dp: Dispatcher) -> None:
    dp.register_message_handler(start_form_kinolog, commands=['form'], state=GeneralStates.kinolog)
    dp.register_message_handler(form_load_kinolog_name, state=KinologFormStatesGroup.name)
    dp.register_message_handler(form_load_kinolog_surname, state=KinologFormStatesGroup.surname)
    dp.register_message_handler(form_load_kinolog_patronymic, state=KinologFormStatesGroup.patronymic)
    dp.register_message_handler(form_load_kinolog_birthday, state=KinologFormStatesGroup.birthday)
    dp.register_message_handler(form_load_kinolog_email, state=KinologFormStatesGroup.email)
    dp.register_message_handler(form_load_kinolog_education, state=KinologFormStatesGroup.education)
    dp.register_message_handler(form_load_kinolog_other_education, state=KinologFormStatesGroup.other_education)
    dp.register_message_handler(form_load_kinolog_communities, state=KinologFormStatesGroup.communities)
    dp.register_message_handler(form_load_kinolog_practice_date, state=KinologFormStatesGroup.practice_date)
    dp.register_message_handler(form_load_kinolog_online_work, state=KinologFormStatesGroup.online_work)
    dp.register_message_handler(form_load_kinolog_supervised, state=KinologFormStatesGroup.supervised)
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
