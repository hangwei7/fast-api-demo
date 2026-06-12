from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.exc import SQLAlchemyError

from app.config import settings
from app.database import check_db_connection

app = FastAPI(title="Fast API Demo", version="0.1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[origin.strip() for origin in settings.cors_origins.split(",")],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/api/health")
def health():
    return {"status": "ok", "message": "FastAPI 服务运行正常"}


@app.get("/api/db/ping")
def db_ping():
    try:
        check_db_connection()
        return {"status": "ok", "message": "MySQL 连接正常"}
    except SQLAlchemyError as exc:
        return {
            "status": "error",
            "message": "MySQL 连接失败，请先创建数据库 fast_api_demo",
            "detail": str(exc),
        }
