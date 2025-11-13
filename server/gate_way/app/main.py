from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.gatewayRoute import router as gateway_router

app = FastAPI(title="Gateway Service")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or ["http://localhost:8005"] if your frontend runs on that port
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(gateway_router)

@app.get("/")
def root():
    return {"message": "Gateway Service is running"}
