import os
from abc import ABC, abstractmethod
from typing import Optional
from langchain_core.embeddings import Embeddings
from langchain_core.language_models.chat_models import BaseChatModel
from langchain_deepseek import ChatDeepSeek
from langchain_openai import OpenAIEmbeddings
from utils.config_handler import rag_conf


class BaseModelFactory(ABC):
    @abstractmethod
    def generator(self) -> Optional[Embeddings | BaseChatModel]:
        pass


class ChatModelFactory(BaseModelFactory):
    def generator(self) -> Optional[Embeddings | BaseChatModel]:
        api_key = rag_conf.get("chat_api_key") or os.getenv("DEEPSEEK_API_KEY")

        if not api_key:
            raise ValueError("缺少 DeepSeek API Key：请填写 config/rag.yml 的 chat_api_key，"
                             "或设置环境变量 DEEPSEEK_API_KEY")

        return ChatDeepSeek(
            model=rag_conf["chat_model_name"],
            api_key=api_key,
            api_base=rag_conf.get("chat_api_base") or None,
        )


class EmbeddingsFactory(BaseModelFactory):
    def generator(self) -> Optional[Embeddings | BaseChatModel]:
        api_key = rag_conf.get("embedding_api_key") or os.getenv("SILICONFLOW_API_KEY")

        if not api_key:
            raise ValueError("缺少 SiliconFlow API Key：请填写 config/rag.yml 的 embedding_api_key，"
                             "或设置环境变量 SILICONFLOW_API_KEY")

        return OpenAIEmbeddings(
            model=rag_conf["embedding_model_name"],
            openai_api_key=api_key,
            openai_api_base=rag_conf.get("embedding_api_base") or None,
            # 非 OpenAI 官方模型不做 tiktoken 上下文长度校验
            tiktoken_enabled=False,
            check_embedding_ctx_length=False,
        )


chat_model = ChatModelFactory().generator()
embed_model = EmbeddingsFactory().generator()
