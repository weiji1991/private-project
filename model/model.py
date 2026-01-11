from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, AIMessage, ToolMessage
from langchain_core.tools import tool

from llm.deepseek import ModelFactory

print("loading dotenv")
load_dotenv()
# model = ModelFactory("deepseek-chat").get_model()
model = ModelFactory("qwen-plus").get_model()

@tool
def get_weather(location):
    """Get weather for a given city."""
    return f"今天{location}阳光明媚"

@tool
def add(a, b):
    """Add two numbers."""
    return a + b

# model_with_tools = model.bind_tools([get_weather, add], tool_choice="add").bind(logprobs=True)
model_with_tools = model
msg = model_with_tools.invoke([HumanMessage(content="1+3等于多少")])
print(msg)
# print(msg.usage_metadata)
# print(msg.content_blocks)
#
# for tool_call in msg.tool_calls:
#     # Execute the tool with the generated arguments
#     tool_result = add.invoke(tool_call)
#     print(type(tool_result))
#     print(tool_result)
#     # messages.append(tool_result)
# # print(type(msg))