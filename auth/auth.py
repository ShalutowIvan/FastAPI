# здесь задаются куки. И также задается JWT, это для того чтобы указать как будут храниться куки. Эта инфа есть в документации фастапиюзерс
from fastapi_users.authentication import CookieTransport, AuthenticationBackend
from fastapi_users.authentication import JWTStrategy

cookie_transport = CookieTransport(cookie_name = "save", cookie_max_age=3600)#тут есть параметры, но пока только куки name указали


SECRET = "SECRET"#это ключ который декодирует токены, его нужно хранить надежно. Желательно в файле .env и потом импорт в файл config

def get_jwt_strategy() -> JWTStrategy:#эта функция которая декодирует все токены
    return JWTStrategy(secret=SECRET, lifetime_seconds=3600)


auth_backend = AuthenticationBackend(
    name="jwt",
    transport=bearer_transport,
    get_strategy=get_jwt_strategy,
)#это переменная для бэкенда. Осталось еще создать юзерменеджера