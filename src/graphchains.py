import os
from dotenv import load_dotenv
load_dotenv()
from langchain_groq import ChatGroq

groq_api_key = os.getenv('GROQ_API_KEY')
llm_model = ChatGroq(model="openai/gpt-oss-20b",temperature=1)

from langchain_core.messages import AIMessage, HumanMessage
from pprint import pprint

messages=[AIMessage(content=f"Please tell me how can i help you", name='LLm Model')]

messages.append([HumanMessage(content=f"I want to learn programming", name='Ganesh')])
messages.append(AIMessage(content=f"Which programming?", name='LLm Model'))

res = llm_model.invoke(messages)