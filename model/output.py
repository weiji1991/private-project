import json

from langchain_core.messages import HumanMessage
from typing_extensions import Annotated, TypedDict

from llm.deepseek import ModelFactory


class Actor(TypedDict):
    name: str
    role: str

class MovieDetails(TypedDict):
    title: str
    year: int
    cast: list[Actor]
    genres: list[str]
    budget: Annotated[float | None, ..., "Budget in millions USD"]

model=ModelFactory().get_model()
model_with_structure = model.with_structured_output(MovieDetails, include_raw=True)
print(model_with_structure.invoke([HumanMessage(content="介绍无间道这部电影")]))