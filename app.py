from fastapi import FastAPI

app = FastAPI()


@app.get("/api")
async def root():
    return {"message": "Hello World this is joseph and this is my Fastapi endpoint and routed with traefik from a docker compose file"}
