from datetime import datetime

from sqlalchemy import MetaData, Integer, String, TIMESTAMP, ForeignKey, Table, Column, JSON

metadata = MetaData()

#создаем таблицу
roles = Table(
    "roles",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String, nullable=False),
    Column("permisions", JSON),
)

users = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("email", String, nullable=False),
    Column("username", String, nullable=False),
    Column("password", String, nullable=False),#пароли нужно хранить в захешированном виде всегда, это для безопасности. Без ключа в захеришрованном виде нельзя его расшифровать
    Column("registered_at", TIMESTAMP, default=datetime.utcnow),#utcnow для разных часовых поясов в случае расположения бд и пользователя в разных часовых поясах
    Column("role_id", Integer, ForeignKey("roles.id")),#ссылаемся на таблицу roles и на ее элемент id
)

#внешний ключ нужен для связи таблиц в бд. Также просто так нельзя удалить таблицу если в ней есть связи другой таблицей через внешний ключ
#миграции создают все таблицы. библиотека alembic нужна для миграций
#для запуска миграций команда: alembic init migrations через консоль. Как это сделать через питон нужно гуглить. Без активации виртуального окружения не срабатывает
#далее в файле alembic.ini нам надо прописать нашу базу точнее ссылку на базу в строке sqlalchemy.url. Перед эти мы в создадим файл .env в нем мы сохраним все пароли от бд и тд, это файл для защиты. Потом создадим файл config.py для импорта наших паролей. Также в файле env.py из папки migrations нужно его отредачить. ТАм есть config - config = context.config. Там мы сделали изменения это нужно для передачи изменений в alembic.ini. Потом редачим target_metadata, в эту переменную нужно записать значение переменной metadata из файла с таблицами.
# Для миграций: нужно их сначала создать потом запустить. Сначала создаем ревизию. Команда для ревизии в терминале: alembic revision --autogenerate -m "Database creation". Database creation это просто название. Потом в папке versions появится новый файл с названием сначала херишрованные даные потом назвнаие которые мы прописали в ревизии Database_creation. Далее в этом файле мы можем проверить конфиги наших таблиц, то есть поля типы данных и тд. Там есть 2 функции upgrade и downgrade. upgrade это внести новые данные, downgrade это откат базы. Пока не сделали миграцию там будет только таблица alembic version.
# Теперь чтобы запустить ревизию по нужному нам хешу нужно в терминале прописать команду: alembic upgrade hash. Где hash это наш хеш набор букв и цифр который получился когда запускали ревизию. После этого будут созданы таблицы в пгадмине. В таблице alembic version будет записан наш хэш, это как бы версия наших баз. То есть по этим хешам получается можно откатываться и тд.
