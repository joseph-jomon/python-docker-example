from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World this is joseph and this is my api endpoint routed with traefik"}
