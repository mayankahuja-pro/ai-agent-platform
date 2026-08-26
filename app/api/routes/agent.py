from fastapi import APIRouter, Depends

from app.auth import get_current_user
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
    # user=Depends(get_current_user),
):

    result = await run_agent(
        message=request.message,
        conversation_id=request.conversation_id,
    )

    return result