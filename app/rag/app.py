from agent import RagAgent
import pprint
from IPython.display import Image, display


agent = RagAgent()
display(Image(agent.graph.get_graph().draw_mermaid_png()))
while True:
    input_message = input("How can I help?")
    for step in agent.graph.stream(
        {"messages": [{"role": "user", "content": input_message}], "query": input_message},
        stream_mode="values",
    ):
        step["messages"][-1].pretty_print()

# import json
# with open("credit_cards.json", "r") as f:
#     data = json.load(f)
# pprint.pprint(data)

# which card should i get for travel?