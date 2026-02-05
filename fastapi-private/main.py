from fastapi import FastAPI
import uvicorn

# 1. FastAPI 인스턴스 생성
app = FastAPI()

# 2. 기본 경로(Root Path) 설정
@app.get("/")
def read_root():
    return {"Hello": "World", "status": "Success"}

@app.get("/api/")
def read_root():
    return {"Hello": "Song", "status": "Success"}
# 3. 경로 파리미터 예시(아이템 조회)
# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: str = None):
#     return {"item_id": item_id, "query": q}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)