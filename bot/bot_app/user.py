from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from .states import GeneralStates, DogFormStatesGroup
from .app import dp , bot
from .keyboards import get_ikb_problem, get_ikb_breed, get_ikb_origin, get_ikb_disease
from bot.db.db_interface import new_dog


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
        reply_markup = get_ikb_breed()
        await bot.send_message(chat_id=message.from_user.id, text=text, reply_markup=reply_markup)
        await DogFormStatesGroup.next()

async def dog_form_load_breed(callback:types.CallbackQuery, state:FSMContext):
    async with state.proxy() as data:
        data['breed'] = callback.data

        if callback.data == 'else':
            text = 'Вес собаки? (кг)'
            await bot.send_message(chat_id=callback.from_user.id, text=text)
            await DogFormStatesGroup.next()
        else:
            data['weight'] = None
            text = 'Откуда вы взяли собаку?'
            reply_markup = get_ikb_origin()
            await bot.send_message(chat_id=callback.from_user.id, text=text, reply_markup=reply_markup)
            await DogFormStatesGroup.origin.set()

async def dog_form_load_weight(message:types.Message, state:FSMContext):
    async with state.proxy() as data:
        if not message.text.isdigit():
            text = 'Вес должен быть числом. Пожалуйсте напишите его еще раз:'
            await bot.send_message(chat_id=message.from_user.id, text=text)
        else:
            data['weight'] = int(message.text)

            text = 'Откуда вы взяли собаку?'
            reply_markup = get_ikb_origin()
            await bot.send_message(chat_id=message.from_user.id, text=text, reply_markup=reply_markup)
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

            text = 'Спасибо что заполнили анкету.'
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
        text = 'Спасибо что заполнили анкету.'
        await bot.send_message(chat_id=message.from_user.id, text=text)
        await GeneralStates.choose_user.set()


def register_main_handlers_user(dp: Dispatcher) -> None:
    dp.register_message_handler(start_form_dog, commands=['dogform'], state=GeneralStates.user)
    dp.register_callback_query_handler(dog_form_load_problem, state=DogFormStatesGroup.problem)
    dp.register_message_handler(dog_form_load_age, state=DogFormStatesGroup.age)
    dp.register_callback_query_handler(dog_form_load_breed, state=DogFormStatesGroup.breed)
    dp.register_message_handler(dog_form_load_weight, state=DogFormStatesGroup.weight)
    dp.register_callback_query_handler(dog_form_load_origin, state=DogFormStatesGroup.origin)
    dp.register_message_handler(dog_form_load_living_together, state=DogFormStatesGroup.living_together)
    dp.register_callback_query_handler(dog_form_load_diseases, state=DogFormStatesGroup.diseases)
    dp.register_message_handler(dog_form_load_diseases_list, state=DogFormStatesGroup.diseases_list)
