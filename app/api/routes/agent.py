from fastapi import APIRouter

from app.schemas.agent import (
    AgentRequest,
    AgentResponse,
)
from app.services.agent_service import run_agent


router = APIRouter(
    prefix="/agent",
    tags=["Agent"],
)


@router.post(
    "",
    response_model=AgentResponse,
)
async def execute_agent(
    request: AgentRequest,
):

    result = await run_agent(
        message=request.message,
        conversation_id=request.conversation_id,
    )

    return result