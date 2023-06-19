from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from .states import GeneralStates, DogFormStatesGroup
from .app import dp , bot
from .keyboards import get_ikb_problem, get_ikb_weight, get_ikb_origin, get_ikb_disease, get_ikb_choose_kinolog, get_ikb_choose_kinolog_back, get_ikb_choose_kinolog_with_back
from bot.db.db_interface import new_dog, get_kinologs_by_problem


async def start_form_dog(message:types.Message):
    text = "Что вас беспокоит?"
    reply_markup  = get_ikb_problem()
    await bot.send_message(chat_id=message.from_user.id, text=text, reply_markup=reply_markup)
    await DogFormStatesGroup.problem.set()

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

        text = 'Возраст собаки'
        await bot.send_message(chat_id=callback.from_user.id, text=text)
        await DogFormStatesGroup.next()


async def dog_form_load_age(message:types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['age'] = message.text

        text = 'Порода собаки?'
        await bot.send_message(chat_id=message.from_user.id, text=text)
        await DogFormStatesGroup.next()

async def dog_form_load_breed(message:types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['breed'] = message.text

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
        text = 'Как давно собака живет с вами'
        await bot.send_message(chat_id=callback.from_user.id, text=text)
        await DogFormStatesGroup.next()

async def dog_form_load_living_together(message:types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['living_together'] = message.text

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

            text = 'Спасибо что заполнили анкету.\n\n'
            kinologs = get_kinologs_by_problem(data['problem'])
            if len(kinologs) > 0:
                text += f"Под ваш запрос подходит следующий специалист: \n"
                text +=  f"ФИО: {kinologs[0]['surname']} {kinologs[0]['name']} {kinologs[0]['patronymic']}\n"
                text += f"Образование: {kinologs[0]['education']}\n"

                reply_markup = get_ikb_choose_kinolog()
                await bot.send_message(chat_id=callback.from_user.id, text=text, reply_markup=reply_markup)
                await DogFormStatesGroup.kinolog_choose.set()
            else:
                text += f"К сожалению, под ваш запрос не подходит ни одного специалист! \n"
                await bot.send_message(chat_id=callback.from_user.id, text=text)
                await GeneralStates.choose_user.set()
        elif callback.data == 'yes':
            text = 'Какие? Впишите?'
            await bot.send_message(chat_id=callback.from_user.id, text=text)
            await DogFormStatesGroup.next()

async def dog_form_load_diseases_list(message:types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['diseases'] = message.text

        new_dog(chat_id=message.from_user.id, problem=data['problem'], age=data['age'], 
                    breed=data['breed'], weight=data['weight'], origin=data['origin'], living_together=data['living_together'],
                   diseases=message.text)
        text = 'Спасибо, что заполнили анкету.\n\n'
        kinologs = get_kinologs_by_problem(data['problem'])

        if len(kinologs) > 0:
            text += f"Под ваш запрос подходит следующий специалист: \n"
            text +=  f"ФИО: {kinologs[0]['surname']} {kinologs[0]['name']} {kinologs[0]['patronymic']}\n"
            text += f"Образование: {kinologs[0]['education']}\n"
            data['kinolog'] = 1

            reply_markup = get_ikb_choose_kinolog()
            await bot.send_message(chat_id=message.from_user.id, text=text, reply_markup=reply_markup)
            await DogFormStatesGroup.next()
        
        else:
            text += f"К сожалению, под ваш запрос не подходит ни одного специалист! \n"
            await bot.send_message(chat_id=message.from_user.id, text=text)
            await GeneralStates.choose_user.set()

async def dog_form_load_kinolog_choose(callback:types.CallbackQuery, state:FSMContext):
    async with state.proxy() as data:
        if callback.data == 'choose':

            text = 'Кинолог выбран.\nНажимайте кнопку перейти чтобы перейти к чату с кинологом и менеджером'
            await bot.send_message(chat_id=callback.from_user.id, text=text)
            await GeneralStates.choose_user.set()
        elif callback.data == 'refuse':
            kinologs = get_kinologs_by_problem(data['problem'])
            if len(kinologs) > data['kinolog']:
                text = 'Другой подходящий специалист под ваш запрос это:\n'
                kinologs = get_kinologs_by_problem(data['problem'])
                text +=  f"ФИО: {kinologs[data['kinolog']]['surname']} {kinologs[data['kinolog']]['name']} {kinologs[data['kinolog']]['patronymic']}\n"
                text += f"Образование: {kinologs[data['kinolog']]['education']}\n"
                data['kinolog'] += 1
                reply_markup = get_ikb_choose_kinolog_with_back()
                await bot.send_message(chat_id=callback.from_user.id, text=text, reply_markup=reply_markup)
            else:
                text = 'К сожалению, у нас больше подходящих специалистов под ваш запрос нет!\n'
                reply_markup = get_ikb_choose_kinolog_back()
                await bot.send_message(chat_id=callback.from_user.id, text=text, reply_markup=reply_markup)
        elif callback.data == 'back':
            text = 'Другой подходящий специалист под ваш запрос это:\n'
            kinologs = get_kinologs_by_problem(data['problem'])
            data['kinolog'] -= 1

            text +=  f"ФИО: {kinologs[data['kinolog']]['surname']} {kinologs[data['kinolog']]['name']} {kinologs[data['kinolog']]['patronymic']}\n"
            text += f"Образование: {kinologs[data['kinolog']]['education']}\n"
            reply_markup = get_ikb_choose_kinolog_with_back() if data['kinolog'] != 1 else get_ikb_choose_kinolog()
            await bot.send_message(chat_id=callback.from_user.id, text=text, reply_markup=reply_markup)


def register_main_handlers_user(dp: Dispatcher) -> None:
    dp.register_message_handler(start_form_dog, commands=['dogform'], state=GeneralStates.user)
    dp.register_callback_query_handler(dog_form_load_problem, state=DogFormStatesGroup.problem)
    dp.register_message_handler(dog_form_load_age, state=DogFormStatesGroup.age)
    dp.register_message_handler(dog_form_load_breed, state=DogFormStatesGroup.breed)
    dp.register_callback_query_handler(dog_form_load_weight, state=DogFormStatesGroup.weight)
    dp.register_callback_query_handler(dog_form_load_origin, state=DogFormStatesGroup.origin)
    dp.register_message_handler(dog_form_load_living_together, state=DogFormStatesGroup.living_together)
    dp.register_callback_query_handler(dog_form_load_diseases, state=DogFormStatesGroup.diseases)
    dp.register_message_handler(dog_form_load_diseases_list, state=DogFormStatesGroup.diseases_list)
    dp.register_callback_query_handler(dog_form_load_kinolog_choose, state=DogFormStatesGroup.kinolog_choose)
