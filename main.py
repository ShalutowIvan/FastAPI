#файл для запуска приложения
import uvicorn
from fastapi import FastAPI
from database import SessionLocal, ingine, Base
from royters import user as UserRouter


#создание бд
Base.metadata.create_all(bind=engine)


app = FastAPI()

app.include_router(UserRouter.router, prefix="/user")

if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, host="127.0.0.1", reload=True, workers=3)