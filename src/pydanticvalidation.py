from langgraph.graph import StateGraph, START, END
from pydantic import BaseModel

class State(BaseModel):
    name: str

def example_node(state:State):
    return {'name':'hello' }

graph = StateGraph(State)

graph.add_node('example_node',example_node)
graph.add_edge(START, 'example_node')
graph.add_edge('example_node', END)

graph_builder = graph.compile()

graph_builder.invoke({'name': 654})