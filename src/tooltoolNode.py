import os
from dotenv import load_dotenv
load_dotenv()
from langchain_groq import ChatGroq

groq_api_key = os.getenv('GROQ_API_KEY')
llm_model = ChatGroq(model="openai/gpt-oss-20b",temperature=1)

from langchain_core.messages import AIMessage, HumanMessage

from langchain_core.messages import AIMessage,HumanMessage
from pprint import pprint

messages=[AIMessage(content=f"Please tell me how can I help",name="LLMModel")]
messages.append(HumanMessage(content=f"I want to learn coding",name="Ganesh"))
messages.append(AIMessage(content=f"Which programming language you want to learn",name="LLMModel"))
messages.append(HumanMessage(content=f"I want to learn python programming language",name="Ganesh"))

# for message in messages:
#     message.pretty_print()

# result=llm_model.invoke(messages)
# print(result.content)

# tool
def add(a:int,b:int)-> int:
    """ Add a and b
    Args:
        a (int): first int
        b (int): second int

    Returns:
        int
    """
    return a+b

### Binding tool with llm

llm_with_tools=llm_model.bind_tools([add])

tool_call=llm_with_tools.invoke([HumanMessage(content=f"What is 2 plus 2",name="Ganesh")])

# print(tool_call.tool_calls)


# Using messages as State
from typing_extensions import TypedDict
from langchain_core.messages import AnyMessage

# class State(TypedDict):
#     message:list[AnyMessage]

# Reducers
from langgraph.graph.message import add_messages
from typing import Annotated
class State(TypedDict):
    messages:Annotated[list[AnyMessage],add_messages]

initial_messages=[AIMessage(content=f"Please tell me how can I help",name="LLMModel")]
initial_messages.append(HumanMessage(content=f"I want to learn coding",name="Ganesh"))
initial_messages
ai_message=AIMessage(content=f"Which programming language you want to learn",name="LLMModel")

### Reducers add_messages is to append instead of override
add_messages(initial_messages,ai_message)

## chatbot node functionality
def llm_tool(state:State):
    return {"messages":[llm_with_tools.invoke(state["messages"])]}

from PIL import Image
import io
from langgraph.graph import StateGraph, START, END



# builder=StateGraph(State)

# builder.add_node("llm_tool",llm_tool)

# builder.add_edge(START,"llm_tool")
# builder.add_edge("llm_tool",END)

# graph=builder.compile()


# img_bytes = graph.get_graph().draw_mermaid_png()
# image = Image.open(io.BytesIO(img_bytes))
# image.show()

tools=[add]

from langgraph.prebuilt import ToolNode
from langgraph.prebuilt import tools_condition


builder=StateGraph(State)

## Add nodes

builder.add_node("llm_tool",llm_tool)
builder.add_node("tools",ToolNode(tools))

## Add Edge
builder.add_edge(START,"llm_tool")
builder.add_conditional_edges(
    "llm_tool",
    # If the latest message (result) from assistant is a tool call -> tools_condition routes to tools
    # If the latest message (result) from assistant is a not a tool call -> tools_condition routes to END
    tools_condition
)
builder.add_edge("tools",END)

graph_builder = builder.compile()
# img_bytes = graph_builder.get_graph().draw_mermaid_png()
# image = Image.open(io.BytesIO(img_bytes))
# image.show()

## invocation

messages=graph_builder.invoke({"messages":"What AI foundary"})

for message in messages["messages"]:
    message.pretty_print()
