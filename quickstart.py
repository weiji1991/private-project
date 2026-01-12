from dotenv import load_dotenv
from langchain_core.messages import HumanMessage
from langchain_deepseek import ChatDeepSeek

from llm.deepseek import ModelFactory, AgentFactory

load_dotenv()

# https://docs.langchain.com/oss/python/integrations/chat#chat-completions-api
def get_weather(city: str) -> str:
    """Get weather for a given city."""
    return f"It's always sunny in {city}!"

agent = AgentFactory("deepseek-chat", [get_weather]).get_agent()

# Run the agent
# model.invoke(
#     [HumanMessage(content="what is the weather in 上海")]
# ).pretty_print()

for data in agent.stream(
    {"messages": [HumanMessage(content="what is the weather in 上海")]},
    stream_mode='messages'
):
    print(data)
# for token, metadata in agent.stream(
#     {"messages": [HumanMessage(content="what is the weather in 上海")]},
#     stream_mode='messages'
# ):
#     print(token)
#     print(type(metadata))
#     print(metadata)
#     print('------------------------------------------------------------')

# for chuck in agent.stream(
#     {"messages": [HumanMessage(content="what is the weather in 上海")]},
#     stream_mode='updates'
# ):
#     # print(chuck)
#     for step, data in chuck.items():
#         print(step)
#         print(data["messages"][-1].content)

# for chuck in agent.stream(
#     {"messages": [HumanMessage(content="what is the weather in 上海")]},
#     stream_mode=['updates', 'messages']
# ):
#     print(chuck)
    # for step, data in chuck.items():
    #     print(step)
    #     print(data["messages"][-1].content)