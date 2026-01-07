from langchain_core.messages import HumanMessage
from langchain_deepseek import ChatDeepSeek

from llm.deepseek import ModelFactory


# https://docs.langchain.com/oss/python/integrations/chat#chat-completions-api
def get_weather(city: str) -> str:
    """Get weather for a given city."""
    return f"It's always sunny in {city}!"

model = ModelFactory("deepseek-chat").get_model()

# Run the agent
model.invoke(
    [HumanMessage(content="what is the weather in 上海")]
).pretty_print()