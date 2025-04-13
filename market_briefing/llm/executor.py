from langchain_openai import ChatOpenAI
from langgraph.checkpoint.memory import MemorySaver
from langgraph.prebuilt import create_react_agent

from market_briefing.tools.finlight import search_tool
from market_briefing.config import OPEN_AI_API_KEY

memory = MemorySaver()

model = ChatOpenAI(api_key=OPEN_AI_API_KEY, model="gpt-4o-2024-11-20")

tools = [search_tool]

# This is what we import elsewhere
agent_executor = create_react_agent(model=model, tools=tools, checkpointer=memory)
