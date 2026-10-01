
from fastapi import FastAPI
from app.api.routes.ChatRouter import router

app = FastAPI(
    title = "Claude Lab",
    version = "1.0.0",
)

# Register New Routers Here
app.include_router(router)


@app.get('/health')
def check_health():
    return {
        "status": True
    }
