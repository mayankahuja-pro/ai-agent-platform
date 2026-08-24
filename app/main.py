from fastapi import FastAPI

from app.api.routes.agent import router as agent_router


app = FastAPI(
    title="AI Operations Agent",
    version="1.0.0",
)  


@app.get("/health")
def health():

    return {
        "status": "healthy",
        "service": "ai-agent-platform",
    }


app.include_router(agent_router)