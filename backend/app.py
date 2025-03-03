from apps.routers.base import router
from config.settings import settings
from database.models.base import Base
from database.session import engine
from fastapi import FastAPI
from starlette.responses import RedirectResponse


def include_router(app: FastAPI) -> None:
    app.include_router(router)


def create_tables():
    Base.metadata.create_all(bind=engine)


def start_application() -> FastAPI:
    app = FastAPI(title=settings.PROJECT_TITLE, version=settings.PROJECT_VERSION)
    include_router(app)

    @app.get("/")
    def redirect_to_docs():
        return RedirectResponse("/docs")

    create_tables()
    return app


app = start_application()
