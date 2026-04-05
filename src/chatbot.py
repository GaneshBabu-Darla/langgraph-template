from typing_extensions import TypedDict
from langgraph.graph import StateGraph, START, END

# Reducers
from typing import Annotated
from langgraph.graph.message import add_messages

class State(TypedDict):
    messages: Annotated[list, add_messages]


import os
from dotenv import load_dotenv
load_dotenv()
from langchain_groq import ChatGroq
from PIL import Image
import io

groq_api_key = os.getenv('GROQ_API_KEY')
llm_model = ChatGroq(model="openai/gpt-oss-20b",temperature=1)

def superbot(state:State):
    return {
        'messages': [
            llm_model.invoke(state['messages'])
        ]
    }

graph=StateGraph(State)

# Node
graph.add_node('SuperBot', superbot)

# Edges
graph.add_edge(START, 'SuperBot')
graph.add_edge('SuperBot', END)

graph_builder = graph.compile()

# -------------------
# img_bytes = graph_builder.get_graph().draw_mermaid_png()
# image = Image.open(io.BytesIO(img_bytes))
# image.show()
result = graph_builder.invoke({'messages': 'Hi, My name is Ganesh'})

# print(result)

# streaming the response

for event in graph_builder.stream({ 'messages': 'Hi my name is ganesh'}, stream_mode='values'):
    print(event)