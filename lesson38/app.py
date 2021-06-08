from fastapi import FastAPI
import api


tags_metadata = [
    {
        'name': 'logins',
        'description': 'Авторизация и регистрация',
    },
    {
        'name': 'records', 
        'description': 'Создание, редактирование, удаление и просмотр операций',
    },
    {
        'name': 'incomes',
        'description': "список всіх записів з додатними значеннями",
    },
    {
        'name': 'outcomes',
        'description': "список всіх записів з від'ємними значеннями",
    },
]

app = FastAPI(
    title='Accountr',
    description='Сервис учета личных доходов и расходов',
    version='1.0.0',
    openapi_tags=tags_metadata,
)

app.include_router(api.router)
