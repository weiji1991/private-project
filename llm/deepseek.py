# Please install OpenAI SDK first: `pip3 install openai`
from langchain_deepseek import ChatDeepSeek

class ModelFactory:
    def __init__(self, model):
        if model == "deepseek-chat":
            self.model = ChatDeepSeek(
                model="deepseek-chat",
                api_key="sk-b33f5d6f5f7a4c47badb4e1593e17537",
                api_base="https://api.deepseek.com",
                extra_body={"reasoning": {"enabled": False}},
            )

    def get_model(self):
        return self.model