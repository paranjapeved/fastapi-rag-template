
from pydantic import (
    BaseModel,
    Field
)
from langgraph.graph.message import add_messages
from typing import Annotated


class GraphState(BaseModel):
    """State definition for the LangGraph Agent/Workflow."""

    messages: Annotated[list, add_messages] = Field(
        default_factory=list, description="The messages in the conversation"
    )
    query: str