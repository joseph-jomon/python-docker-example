from fastapi import FastAPI

app = FastAPI()


@app.get("/api")
async def root():
    return {"message": "Hello World this is joseph and this is my api endpoint routed with traefik, and hey you the one sitiing in traffck schike eine hallo"}
