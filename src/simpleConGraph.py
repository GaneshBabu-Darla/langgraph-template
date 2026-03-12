from langgraph.graph import StateGraph, START, END
from pydantic import BaseModel
# from IPython.display import Image
from PIL import Image
import io
import random
from typing import Literal

class State(BaseModel):
    graph_info: str

# NODES

def start_play(state: State):
    print("Start_Play node called")
    return {
        "graph_info": state.graph_info + " I am planning to play"
    }

def cricket(state: State):
    print("Cricket node called")
    return {
        "graph_info": state.graph_info + " Cricket"
    }

def batminton(state: State):
    print("Cricket node called")
    return {
        "graph_info": state.graph_info + " Batminton"
    }


def random_play(state:State)->Literal['cricket', 'batminton']:
    graph_info= state.graph_info

    if random.random()>0.5:
        return 'cricket'
    else:
        return 'batminton'
    

# Build Simple Graph
# -------------------
graph = StateGraph(State)

# adding nodes
graph.add_node('start_play', start_play)
graph.add_node('cricket', cricket)    
graph.add_node('batminton', batminton) 

# adding edges

graph.set_entry_point('start_play')
graph.add_conditional_edges('start_play', random_play)
graph.add_edge('cricket', END)
graph.add_edge('batminton', END)


# compile
graph_builder = graph.compile()

result = graph_builder.invoke({"graph_info": "Hey I'm Ganesh"})
print(result)
# Visualize
# -------------------
img_bytes = graph_builder.get_graph().draw_mermaid_png()
image = Image.open(io.BytesIO(img_bytes))
image.show()