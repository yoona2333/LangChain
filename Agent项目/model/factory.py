from abc import ABC, abstractmethod
from typing import Optional
import os
from langchain_core.embeddings import Embeddings
from langchain_core.language_models import BaseChatModel
from langchain_deepseek import ChatDeepSeek
from Agent项目.utils.config_handler import rag_conf

class BaseModelFactory(ABC):
    @abstractmethod
    def generator(self) -> Optional[Embeddings | BaseChatModel]:
        pass

class ChatModelFactory(BaseModelFactory):
    def generator(self) -> Optional[Embeddings | BaseChatModel]:
        api_key = os.getenv("DEEPSEEK_API_KEY")
        if not api_key:
            raise ValueError("DEEPSEEK_API_KEY 环境变量为空，请检查.env")
        return ChatDeepSeek(
            model=rag_conf["chat_model_name"],
            api_key=api_key
        )

class EmbeddingsFactory(BaseModelFactory):
    def generator(self) -> Optional[Embeddings | BaseChatModel]:
        api_key = os.getenv("DEEPSEEK_API_KEY")
        if not api_key:
            raise ValueError("DEEPSEEK_API_KEY 环境变量为空，请检查.env")
        return ChatDeepSeek(
            model=rag_conf["embedding_model_name"],
            api_key=api_key
        )

# ========= 删除下面两行全局变量！！=========
# chat_model = ChatModelFactory().generator()
# embed_model = EmbeddingsFactory().generator()

# 改为对外暴露函数，需要的时候再创建
def get_chat_model():
    return ChatModelFactory().generator()

def get_embed_model():
    return EmbeddingsFactory().generator()
