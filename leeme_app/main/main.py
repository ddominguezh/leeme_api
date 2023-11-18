from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from leeme_app.main.app.word.infrastructure.controller.get_words_filter_by_characters import get_words_filter_by_characters_router
from leeme_app.main.shared.infrastructure.controller.health import health_router

app = FastAPI()


# Configuración de CORS
origins = [
    "http://localhost:5005",
    "https://ddominguezh.pythonanywhere.com"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(health_router)
app.include_router(get_words_filter_by_characters_router)