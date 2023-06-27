from fastapi import FastAPI
from pydantic import BaseModel, Field
import uvicorn
from typing import List
from pages.router import router as router_pages
from fastapi.staticfiles import StaticFiles



app = FastAPI(title="Parser")

app.mount("/static", StaticFiles(directory="static"), name="static")#это для картинок

app.include_router(router_pages)


if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, host="127.0.0.1", reload=True, workers=3)