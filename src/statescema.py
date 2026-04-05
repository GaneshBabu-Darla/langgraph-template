# State scema with dataclasses 
# when we define a langgraph StateGraph, we use a state schema
# the state scehma represents the structure and types of data that our graph will use.
# all nodes are expected to communicate with that schema.
# langGraph offers flexibility in how you define your state schema, accommadating various python types and validation approaches.
from typing_extensions import TypedDict
from typing import Literal
import random
from langgraph.graph import StateGraph, START, END

# from IPython.display import Image
from PIL import Image
import io

class TypedDictState(TypedDict):
    name:str
    game:Literal['cricket','badminton']

def play_game(state: TypedDictState):
    print('---------Play Game node has been called-------------')
    return {'name': state['name'] + 'want to play'}

def decide_play(state: TypedDictState)->Literal['cricket', 'badminton']:
    if random.random() < 0.5:
        return 'cricket'
    else:
        return 'badminton'

def cricket(state: TypedDictState):
    print('---------Cricket node has been called-------------')
    return {'game': 'cricket'}

def badminton(state: TypedDictState):
    print('---------Badminton node has been called-------------')
    return {'game': 'badminton'}


builder = StateGraph(TypedDictState)
builder.add_node('playgame', play_game)
builder.add_node('cricket', cricket)
builder.add_node('badminton', badminton)

builder.add_edge(START, 'playgame')
builder.add_conditional_edges('playgame', decide_play)
builder.add_edge('cricket', END)
builder.add_edge('badminton', END)

# compile
graph_builder = builder.compile()
# img_bytes = graph_builder.get_graph().draw_mermaid_png()
# image = Image.open(io.BytesIO(img_bytes))
# image.show()
graph_builder.invoke({'name': 'ganesh'})