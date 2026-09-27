from ollama import AsyncClient

from app.config.settings import settings
from app.llm.base import LLM 


class Ollama(LLM):
    def __init__(self):
        self.client = AsyncClient(host=settings.ollama_base_url)
        self.model = settings.llm_model

    async def generate(self, messages: list[dict[str,str]]) -> str:

        response = await self.client.chat(
            model=self.model,
            messages=messages,
        )
        return response["messages"]["content"]
