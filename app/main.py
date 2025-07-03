from fastapi import FastAPI
from app import config
from app.rag.agent import RagAgent

app = FastAPI(openapi_url="/openapi.json" if config.enable_docs else None)


agent = RagAgent()


@app.get("/askBot")
async def ask_bot(query: str, user_name: str) -> str:
    for step in agent.graph.stream(
        {"messages": [{"role": "user", "content": query}], "query": query},
        stream_mode="values",
    ):
        step["messages"][-1].pretty_print()
    if (step["messages"][-1].type == "ai"):
        return step["messages"][-1].content
    else:
        return "Sorry,I don't know"
        