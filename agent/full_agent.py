from dataclasses import dataclass

from langchain.agents.structured_output import ToolStrategy

from llm.deepseek import AgentFactory
from memory.memory import checkpointer
from prompt.weather_prompt import SYSTEM_PROMPT
from tools.tools import Context, get_user_location, get_weather_for_location

@dataclass
class ResponseFormat:
    """Response schema for the agent."""
    # A punny response (always required)
    punny_response: str
    # Any interesting information about the weather if available
    weather_conditions: str | None = None

agent = AgentFactory("deepseek-chat", [get_user_location, get_weather_for_location], SYSTEM_PROMPT, Context, ToolStrategy(ResponseFormat), checkpointer).get_agent()
# `thread_id` is a unique identifier for a given conversation.
config = {"configurable": {"thread_id": "1"}}

# agent.invoke(dict)
# model.invoke(list[Messages])
response = agent.invoke(
    {"messages": [{"role": "user", "content": "what is the weather outside?"}]},
    config=config,
    context=Context(user_id="1")
)

print(response['structured_response'])
# ResponseFormat(
#     punny_response="Florida is still having a 'sun-derful' day! The sunshine is playing 'ray-dio' hits all day long! I'd say it's the perfect weather for some 'solar-bration'! If you were hoping for rain, I'm afraid that idea is all 'washed up' - the forecast remains 'clear-ly' brilliant!",
#     weather_conditions="It's always sunny in Florida!"
# )

# 相同线程中，可以复用内存
# Note that we can continue the conversation using the same `thread_id`.
agent = AgentFactory("deepseek-chat", [get_user_location, get_weather_for_location], SYSTEM_PROMPT, Context, ToolStrategy(ResponseFormat), checkpointer).get_agent()
response = agent.invoke(
    {"messages": [{"role": "user", "content": "thank you!"}]},
    config=config,
    context=Context(user_id="1")
)

print(response['structured_response'])
# ResponseFormat(
#     punny_response="You're 'thund-erfully' welcome! It's always a 'breeze' to help you stay 'current' with the weather. I'm just 'cloud'-ing around waiting to 'shower' you with more forecasts whenever you need them. Have a 'sun-sational' day in the Florida sunshine!",
#     weather_conditions=None
# )