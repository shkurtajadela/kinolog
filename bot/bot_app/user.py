import random
from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from .states import GeneralStates, DogFormStatesGroup
from .app import dp , bot
from .keyboards import get_ikb_problem, get_ikb_weight, get_ikb_origin, get_ikb_disease, get_ikb_choose_kinolog, get_ikb_choose_kinolog_back, get_ikb_registration, get_ikb_choose_kinolog_with_back, get_ikb_chat, get_ikb_confirm_dog_form
from bot.db.db_interface import new_dog, get_kinologs_by_problem
import pyrogram
from pyrogram import raw, Client, filters
from .show_form import show_kinolog_info, show_dog_info

async def start_form_dog(callback:types.CallbackQuery, state:FSMContext):
    async with state.proxy() as data:
        if callback.data == "form":
            await bot.delete_message(chat_id=callback.from_user.id, message_id=callback.message.message_id)
            text = "Что вас беспокоит?"
            reply_markup  = get_ikb_problem()
            await bot.send_message(chat_id=callback.from_user.id, text=text, reply_markup=reply_markup)
            await DogFormStatesGroup.problem.set()
        else:
            welcome_msg = "Привет! Это бот для заполнения анкеты кинологом или поиска кинолога владельцем собаки. \nЕсли хотите зарегистрироваться, то нажимайте кнопку ниже"
            await bot.send_message(chat_id=callback.from_user.id, text=welcome_msg, reply_markup=get_ikb_registration())
            await GeneralStates.registration.set()

async def dog_form_load_problem(callback:types.CallbackQuery, state:FSMContext):
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
        await bot.delete_message(chat_id=callback.from_user.id, message_id=callback.message.message_id)
        text = 'Напишите возраст собаки:'
        msg = await bot.send_message(chat_id=callback.from_user.id, text=text)
        data['msg_id'] = msg.message_id
        await DogFormStatesGroup.next()


async def dog_form_load_age(message:types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['age'] = message.text

        await bot.delete_message(chat_id=message.from_user.id, message_id=message.message_id)
        text = 'Напишите породу собаки?'
        await bot.edit_message_text(chat_id=message.from_user.id, text=text, message_id=data['msg_id'])
        await DogFormStatesGroup.next()

async def dog_form_load_breed(message:types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['breed'] = message.text

        await bot.delete_message(chat_id=message.from_user.id, message_id=message.message_id)
        await bot.delete_message(chat_id=message.from_user.id, message_id=data['msg_id'])
        text = 'Выберите вес собаки? (кг)'
        reply_markup  = get_ikb_weight()
        await bot.send_message(chat_id=message.from_user.id, text=text, reply_markup=reply_markup)
        await DogFormStatesGroup.next()

async def dog_form_load_weight(callback:types.CallbackQuery, state:FSMContext):
    async with state.proxy() as data:
        ans = {'weight1': 'Мини (до 5 кг)',
         'weight2': 'Малый (5-10 кг)',
         'weight3': 'Средний (10-20 кг)',
         'weight4': 'Большой (20-40 кг)',
         'weight5': 'Огромный (40кг+)'
         }
        data['weight'] = ans[callback.data]

        await bot.delete_message(chat_id=callback.from_user.id, message_id=callback.message.message_id)
        text = 'Откуда вы взяли собаку?'
        reply_markup = get_ikb_origin()
        await bot.send_message(chat_id=callback.from_user.id, text=text, reply_markup=reply_markup)
        await DogFormStatesGroup.next()

async def dog_form_load_origin(callback:types.CallbackQuery, state:FSMContext):
    async with state.proxy() as data:
        ans = {
            'breeder': 'У заводчика',
            'street': 'Из приюта / с улицы',
            'other_owner': 'От другого хозяина, который отдавал собаку'
        }

        data['origin'] = ans[callback.data]
        await bot.delete_message(chat_id=callback.from_user.id, message_id=callback.message.message_id)
        text = 'Как давно собака живет с вами?'
        msg = await bot.send_message(chat_id=callback.from_user.id, text=text)
        data['msg_id'] = msg.message_id
        await DogFormStatesGroup.next()

async def dog_form_load_living_together(message:types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['living_together'] = message.text

        await bot.delete_message(chat_id=message.from_user.id, message_id=message.message_id)
        await bot.delete_message(chat_id=message.from_user.id, message_id=data['msg_id'])
        text = 'Есть ли у собаки какие-либо диагностированные заболевания (в т.ч. хронические), о которых вам известно?'
        reply_markup = get_ikb_disease()
        await bot.send_message(chat_id=message.from_user.id, text=text, reply_markup=reply_markup)
        await DogFormStatesGroup.next()

async def dog_form_load_diseases(callback:types.CallbackQuery, state:FSMContext):
    async with state.proxy() as data:
        if callback.data == 'no':
            new_dog(chat_id=callback.from_user.id, problem=data['problem'], age=data['age'], 
                    breed=data['breed'], weight=data['weight'], origin=data['origin'], living_together=data['living_together'],
                   diseases='нет')

            await bot.delete_message(chat_id=callback.from_user.id, message_id=callback.message.message_id)
            text = 'Спасибо, что заполнили анкету.\n\n' 
            text += show_dog_info(problem=data['problem'], age=data['age'], breed=data['breed'], weight=data['weight'], origin=data['origin'], living_together=data['living_together'], diseases="нет")
            text += 'Что хотите делать:'
            msg = await bot.send_message(chat_id=callback.from_user.id, text=text, reply_markup=get_ikb_confirm_dog_form())
            data['msg_id'] = msg.message_id
            await DogFormStatesGroup.form_confirm.set()
        elif callback.data == 'yes':
            text = 'Какие? Впишите?'
            await bot.delete_message(chat_id=callback.from_user.id, message_id=callback.message.message_id)
            msg = await bot.send_message(chat_id=callback.from_user.id, text=text)
            data['msg_id'] = msg.message_id
            await DogFormStatesGroup.next()

async def dog_form_load_diseases_list(message:types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['diseases'] = message.text

        new_dog(chat_id=message.from_user.id, problem=data['problem'], age=data['age'], 
                    breed=data['breed'], weight=data['weight'], origin=data['origin'], living_together=data['living_together'],
                   diseases=message.text)
        await bot.delete_message(chat_id=message.from_user.id, message_id=message.message_id)
        await bot.delete_message(chat_id=message.from_user.id, message_id=data['msg_id'])

        text = 'Спасибо, что заполнили анкету.\n\n'
        text += show_dog_info(problem=data['problem'], age=data['age'], breed=data['breed'], weight=data['weight'], origin=data['origin'], living_together=data['living_together'], diseases=message.text)
        text += 'Что хотите делать:'
        msg = await bot.send_message(chat_id=message.from_user.id, text=text, reply_markup=get_ikb_confirm_dog_form())
        data['msg_id'] = msg.message_id
        await DogFormStatesGroup.next()

async def dog_form_load_confirm(callback:types.CallbackQuery, state:FSMContext):
    async with state.proxy() as data:
        if callback.data == 'get_kinologs':
            kinologs = get_kinologs_by_problem(data['problem'], callback.from_user.id)
            if len(kinologs) > 0:
                text = f"Под ваш запрос подходит следующий специалист: \n"
                text += f"\n\n{show_kinolog_info(name=kinologs[0]['name'], surname=kinologs[0]['surname'], patronymic=kinologs[0]['patronymic'], birthday=kinologs[0]['birthday'], email=kinologs[0]['email'], education=kinologs[0]['education'], other_education=kinologs[0]['other_education'], communities=kinologs[0]['communities'], practice_date=kinologs[0]['practice_date'], online_work=kinologs[0]['online_work'], supervised=kinologs[0]['supervised'], other_interests=kinologs[0]['other_interests'], kinolog_site=kinologs[0]['kinolog_site'], motivation=kinologs[0][ 'motivation'], work_stages=kinologs[0]['work_stages'], dog_teaching=kinologs[0]['dog_teaching'], influenced_by=kinologs[0]['influenced_by'],punishment=kinologs[0]['punishment'], punishment_effect=kinologs[0]['punishment_effect'], ammunition=kinologs[0]['ammunition'], other_activities=kinologs[0]['other_activities'], work_methods=kinologs[0]['work_methods'], choice_importance=kinologs[0]['choice_importance'], training_situation=kinologs[0]['training_situation'], advise=kinologs[0]['advise'], problem=kinologs[0]['problem'])}"
                data['kinolog'] = 1
                await bot.delete_message(chat_id=callback.from_user.id, message_id=data['msg_id'])

                reply_markup = get_ikb_choose_kinolog()
                msg = await bot.send_photo(chat_id=callback.from_user.id, caption=text, photo=kinologs[0]['photo'], reply_markup=reply_markup)
                data['msg_id'] = msg.message_id
                await DogFormStatesGroup.kinolog_choose.set()
            else:
                text = f"К сожалению, под ваш запрос не подходит ни одного специалист! \n\nНажимайте /start чтобы снова начинать"
                await bot.edit_message_text(chat_id=callback.from_user.id, text=text, message_id=data['msg_id'])
                await GeneralStates.choose_user.set()
        elif callback.data == "go_to_start":
            welcome_msg = "Привет! Это бот для заполнения анкеты кинологом или поиска кинолога владельцем собаки. \nЕсли хотите зарегистрироваться, то нажимайте кнопку ниже"
            await bot.delete_message(chat_id=callback.from_user.id, message_id=data['msg_id'])
            await bot.send_message(chat_id=callback.from_user.id, text=welcome_msg, reply_markup=get_ikb_registration())
            await GeneralStates.registration.set()


async def dog_form_load_kinolog_choose(callback:types.CallbackQuery, state:FSMContext):
    async with state.proxy() as data:
        if callback.data == 'choose':
            kinolog = get_kinologs_by_problem(data['problem'], callback.from_user.id)[data['kinolog']-1]

            data['kinolog_id'] = kinolog['chat_id']
            text = f"Кинолог выбран.\nНажимайте кнопку перейти чтобы перейти к чату с кинологом и менеджером:"
            reply_markup = get_ikb_chat()
            await bot.send_message(chat_id=callback.from_user.id, text=text, reply_markup=reply_markup)
            await DogFormStatesGroup.next()
        elif callback.data == 'refuse':
            kinologs = get_kinologs_by_problem(data['problem'], callback.from_user.id)
            if len(kinologs) > data['kinolog']:
                text = 'Другой подходящий специалист под ваш запрос это:\n'
                kinologs = get_kinologs_by_problem(data['problem'], callback.from_user.id)
                text += f"\n\n{show_kinolog_info(name=kinologs[data['kinolog']]['name'], surname=kinologs[data['kinolog']]['surname'], patronymic=kinologs[data['kinolog']]['patronymic'], birthday=kinologs[data['kinolog']]['birthday'], email=kinologs[data['kinolog']]['email'], education=kinologs[data['kinolog']]['education'], other_education=kinologs[data['kinolog']]['other_education'], communities=kinologs[data['kinolog']]['communities'], practice_date=kinologs[data['kinolog']]['practice_date'], online_work=kinologs[data['kinolog']]['online_work'], supervised=kinologs[data['kinolog']]['supervised'], other_interests=kinologs[data['kinolog']]['other_interests'], kinolog_site=kinologs[data['kinolog']]['kinolog_site'], motivation=kinologs[data['kinolog']][ 'motivation'], work_stages=kinologs[data['kinolog']]['work_stages'], dog_teaching=kinologs[data['kinolog']]['dog_teaching'], influenced_by=kinologs[data['kinolog']]['influenced_by'],punishment=kinologs[data['kinolog']]['punishment'], punishment_effect=kinologs[data['kinolog']]['punishment_effect'], ammunition=kinologs[data['kinolog']]['ammunition'], other_activities=kinologs[data['kinolog']]['other_activities'], work_methods=kinologs[data['kinolog']]['work_methods'], choice_importance=kinologs[data['kinolog']]['choice_importance'], training_situation=kinologs[data['kinolog']]['training_situation'], advise=kinologs[data['kinolog']]['advise'], problem=kinologs[data['kinolog']]['problem'])}"
                data['kinolog'] += 1
                reply_markup = get_ikb_choose_kinolog_with_back()
                await bot.send_message(chat_id=callback.from_user.id, text=text, reply_markup=reply_markup)
            else:
                text = 'К сожалению, у нас больше подходящих специалистов под ваш запрос нет!\n\nНажимайте /start чтобы снова начинать'
                reply_markup = get_ikb_choose_kinolog_back()
                await bot.send_message(chat_id=callback.from_user.id, text=text, reply_markup=reply_markup)
        elif callback.data == 'back':
            text = 'Другой подходящий специалист под ваш запрос это:\n'
            kinologs = get_kinologs_by_problem(data['problem'], callback.from_user.id)
            data['kinolog'] -= 1

            text += f"\n\n{show_kinolog_info(name=kinologs[data['kinolog']]['name'], surname=kinologs[data['kinolog']]['surname'], patronymic=kinologs[data['kinolog']]['patronymic'], birthday=kinologs[data['kinolog']]['birthday'], email=kinologs[data['kinolog']]['email'], education=kinologs[data['kinolog']]['education'], other_education=kinologs[data['kinolog']]['other_education'], communities=kinologs[data['kinolog']]['communities'], practice_date=kinologs[data['kinolog']]['practice_date'], online_work=kinologs[data['kinolog']]['online_work'], supervised=kinologs[data['kinolog']]['supervised'], other_interests=kinologs[data['kinolog']]['other_interests'], kinolog_site=kinologs[data['kinolog']]['kinolog_site'], motivation=kinologs[data['kinolog']][ 'motivation'], work_stages=kinologs[data['kinolog']]['work_stages'], dog_teaching=kinologs[data['kinolog']]['dog_teaching'], influenced_by=kinologs[data['kinolog']]['influenced_by'],punishment=kinologs[data['kinolog']]['punishment'], punishment_effect=kinologs[data['kinolog']]['punishment_effect'], ammunition=kinologs[data['kinolog']]['ammunition'], other_activities=kinologs[data['kinolog']]['other_activities'], work_methods=kinologs[data['kinolog']]['work_methods'], choice_importance=kinologs[data['kinolog']]['choice_importance'], training_situation=kinologs[data['kinolog']]['training_situation'], advise=kinologs[data['kinolog']]['advise'], problem=kinologs[data['kinolog']]['problem'])}"

            reply_markup = get_ikb_choose_kinolog_with_back() if data['kinolog'] != 1 else get_ikb_choose_kinolog()
            await bot.send_message(chat_id=callback.from_user.id, text=text, reply_markup=reply_markup)


async def dog_form_load_chat(callback: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        if callback.data == 'go_to_chat':
            chat_title = "WowPet GroupChat"
            cynologist_id = data['kinolog_id']
            app_pyr = Client("WowPet", api_id=27901249, api_hash="4b2bf435fafee0bde22ea278c3090e8e")
            await app_pyr.start()
            chat = await app_pyr.create_group(chat_title, cynologist_id)
            link = await app_pyr.create_chat_invite_link(chat_id=chat.id)
            await bot.send_message(chat_id=cynologist_id, text=f"У вас новый клиент. Для того чтобы связаться с ними переходите в чат {link.invite_link}")

            text = f"Chat создан. Переходите по ссылку {link.invite_link}\n\nСпасибо, что использовали наш сервис!\n\nНажимайте /start чтобы снова начинать"
            await bot.send_message(chat_id=callback.from_user.id, text=text)
            await app_pyr.stop()
            await GeneralStates.choose_user.set()


def register_main_handlers_user(dp: Dispatcher) -> None:
    dp.register_callback_query_handler(start_form_dog, state=GeneralStates.user)
    dp.register_callback_query_handler(dog_form_load_problem, state=DogFormStatesGroup.problem)
    dp.register_message_handler(dog_form_load_age, state=DogFormStatesGroup.age)
    dp.register_message_handler(dog_form_load_breed, state=DogFormStatesGroup.breed)
    dp.register_callback_query_handler(dog_form_load_weight, state=DogFormStatesGroup.weight)
    dp.register_callback_query_handler(dog_form_load_origin, state=DogFormStatesGroup.origin)
    dp.register_message_handler(dog_form_load_living_together, state=DogFormStatesGroup.living_together)
    dp.register_callback_query_handler(dog_form_load_diseases, state=DogFormStatesGroup.diseases)
    dp.register_message_handler(dog_form_load_diseases_list, state=DogFormStatesGroup.diseases_list)
    dp.register_callback_query_handler(dog_form_load_confirm, state=DogFormStatesGroup.form_confirm)
    dp.register_callback_query_handler(dog_form_load_kinolog_choose, state=DogFormStatesGroup.kinolog_choose)
    dp.register_callback_query_handler(dog_form_load_chat, state=DogFormStatesGroup.chat)