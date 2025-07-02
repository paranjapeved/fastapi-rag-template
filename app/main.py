from fastapi import FastAPI
from app import config
from app.rag.agent import RagAgent

app = FastAPI(openapi_url="/openapi.json" if config.enable_docs else None)


agent = RagAgent()


@app.get("/")
async def root() -> str:
    for step in agent.graph.stream(
        {"messages": [{"role": "user", "content": "What is the best credit card in Canada?"}], "query": "What is the best credit card in Canada?"},
        stream_mode="values",
    ):
        step["messages"][-1].pretty_print()

