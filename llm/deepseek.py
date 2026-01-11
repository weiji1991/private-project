# Please install OpenAI SDK first: `pip3 install openai`
from langchain.agents import create_agent
from langchain.chat_models import init_chat_model
from langchain_core.rate_limiters import InMemoryRateLimiter
from langchain_deepseek import ChatDeepSeek
from openai import OpenAI
from langchain_community.llms import Tongyi
from langchain_community.chat_models.tongyi import ChatTongyi


class ModelFactory:
    def __init__(self, model = None):
        model = model if model else "deepseek-chat"

        rate_limiter = InMemoryRateLimiter(
            requests_per_second=0.1,  # 1 request every 10s
            check_every_n_seconds=0.1,  # Check every 100ms whether allowed to make a request
            max_bucket_size=10,  # Controls the maximum burst size.
        )

        if model == "qwen-plus":
            self.model = ChatTongyi(model="qwen-plus")
        else:
            self.model = init_chat_model(model)


    def get_model(self):
        return self.model


class AgentFactory:
    def __init__(self, model, tools=None, system_prompt=None, context_schema=None, response_format=None, checkpointer=None):
        model = ModelFactory(model).get_model()
        self.agent = create_agent(
            model=model,
            system_prompt=system_prompt,
            tools=tools,
            context_schema=context_schema,
            response_format=response_format,
            checkpointer=checkpointer
        )

    def get_agent(self):
        return self.agent

