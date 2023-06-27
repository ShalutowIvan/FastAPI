#роутер для отображения шаблона html
from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

router = APIRouter(
prefix="/pages",#это чтобы в документации префикс выделился
tags=["Pages"]
	)


#шаблоны подключаем к фастапи
templates = Jinja2Templates(directory="templates")#тут в кавычках путь к папке templates относительно main.py

@router.get("/base")
def get_base_page(request: Request):#это функция для запроса страницы. Мы потом создаем html страницу и по адресу /pages/base будет страница файл страницы называется base.html
	return templates.TemplateResponse("base.html", {"request": request})

@router.get("/search")
def get_search_page(request: Request):#это функция для запроса страницы. Мы потом создаем html страницу и по адресу /pages/search будет страница файл страницы называется search.html
	return templates.TemplateResponse("search.html", {"request": request})

#в html файлах можно писать jinja шаблоны с кодом питона. ТАм можно делать какие либо операции

