from langgraph.graph import StateGraph, END, START
from pydantic import BaseModel
# from IPython.display import Image
from PIL import Image
import io


class State(BaseModel):
    graph_info: str


# Nodes

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

# Build Simple Graph
# -------------------
graph = StateGraph(State)

# adding nodes
graph.add_node('start_play', start_play)
graph.add_node('cricket', cricket)

# adding edges

graph.set_entry_point('start_play')
graph.add_edge('start_play', 'cricket')
graph.add_edge('cricket', END)

# compile
graph_builder = graph.compile()

result = graph_builder.invoke({"graph_info": "Today"})
print(result)
# Visualize
# -------------------
img_bytes = graph_builder.get_graph().draw_mermaid_png()
image = Image.open(io.BytesIO(img_bytes))
image.show()