from pydantic import BaseModel, Field


class AgentRequest(BaseModel):

    message: str = Field(
        min_length=1,
        max_length=4000,
    )

    conversation_id: str | None = None


class AgentResponse(BaseModel):

    conversation_id: str
    answer: str
    tools_used: list[str]