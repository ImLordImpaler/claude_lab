from app.config.settings import settings
from app.llm.base import LLM
from app.llm.ollama import OllamaInterface


def get_llm() -> LLM:
    if settings.llm_provider == "ollama":
        return OllamaInterface()
    
    raise ValueError(
        "Please use Ollama"
    )