import time
import asyncio
import uvicorn
from fastapi import FastAPI, BackgroundTasks

app = FastAPI()

def sync_task():
    time.sleep(3)
    print("Sent to email")
    
async def async_task():
    await asyncio.sleep(3)
    print("A request was made to an external API")
    
@app.post("/")
async def some_route(Bg_tasks:BackgroundTasks):
    ...
    # asyncio.create_task(async_task())
    Bg_tasks.add_task(sync_task)
    return {"Ok":True}

if __name__ == "__main__":
    uvicorn.run("async_multithread:app")