import os

from dotenv import load_dotenv
from fastapi import FastAPI
import pymysql
import uvicorn

load_dotenv()

# 1. FastAPI 인스턴스 생성
app = FastAPI()

# 2. 기본 경로(Root Path) 설정
@app.get("/")
def read_root():
    return {"Hello": "World", "status": "Success"}

def _can_connect_mysql() -> bool:
    host = os.getenv("DB_HOST")
    user = os.getenv("DB_USER")
    password = os.getenv("DB_PASSWORD")
    db = os.getenv("DB_NAME")
    port = int(os.getenv("DB_PORT", "3306"))

    if not all([host, user, password]):
        return False

    try:
        connect_kwargs = {
            "host": host,
            "user": user,
            "password": password,
            "port": port,
            "connect_timeout": 3,
        }
        if db:
            connect_kwargs["database"] = db
        conn = pymysql.connect(**connect_kwargs)
        conn.close()
        return True
    except Exception:
        return False


@app.get("/api/")
def read_api():
    return {"status": "ok" if _can_connect_mysql() else "fail"}
# 3. 경로 파리미터 예시(아이템 조회)
# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: str = None):
#     return {"item_id": item_id, "query": q}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
