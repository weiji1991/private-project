from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, AIMessageChunk, AnyMessage, AIMessage, ToolMessage
from langchain_deepseek import ChatDeepSeek

from llm.deepseek import ModelFactory, AgentFactory

load_dotenv()

# https://docs.langchain.com/oss/python/integrations/chat#chat-completions-api
def get_weather(city: str) -> str:
    """Get weather for a given city."""
    return f"It's always sunny in {city}!"

agent = AgentFactory("deepseek-chat", [get_weather]).get_agent()


def _render_message_chunk(token: AIMessageChunk) -> None:
    if token.text and not token.tool_calls:
        print(token.text, end="|")
    if token.tool_call_chunks:
        print(token.tool_call_chunks)
    # N.B. all content is available through token.content_blocks


def _render_completed_message(message: AnyMessage) -> None:
    if isinstance(message, AIMessage) and message.tool_calls:
        print(f"Tool calls: {message.tool_calls}")
    if isinstance(message, ToolMessage):
        print(f"Tool response: {message.content_blocks}")


input_message = {"role": "user", "content": "what is the weather in 上海?"}
for stream_mode, data in agent.stream(
    {"messages": [input_message]},
    stream_mode=["messages", "updates"],
):
    if stream_mode == "messages":
        token, metadata = data
        if isinstance(token, AIMessageChunk):
            _render_message_chunk(token)
    if stream_mode == "updates":
        for source, update in data.items():
            if source in ("model", "tools"):  # `source` captures node name
                _render_completed_message(update["messages"][-1])
