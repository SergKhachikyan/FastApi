from fastapi import FastAPI,Request,Response
from pydantic import BaseModel
from typing import Callable
import uvicorn
import time

app = FastAPI()

@app.middleware("http")
async def my_middleware(request:Request,call_next:Callable):
    ip_address = request.client.host
    print(f"{ip_address=}")
    if ip_address in ["127.0.0.1", "localhost"]:
        return Response(status_code=429, content="Much many requests")
    
    start = time.perf_counter()
    response = await call_next(request)
    end = time.perf_counter() - start
    print(f"Time of request {end} ")
    return response
    
    
@app.get("/users", tags=["Users"])
async def get_users():
    time.sleep(1)
    return [{"id":1,"Name":"Sergo"}]


if __name__ == "__main__":
    uvicorn.run("middleware_fastAPI:app", reload=True)