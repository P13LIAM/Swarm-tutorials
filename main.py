from fastapi import FastAPI
import asyncio

app = FastAPI()
counter = 0
lock = asyncio.Lock()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/do_something")
async def do_something():
    global counter

    async with lock:
        counter += 1
        # some other thread-safe code here

    return {"count": counter}