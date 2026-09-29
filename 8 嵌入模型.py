from langchain_community.embeddings import  DashScopeEmbeddings
from langchain_ollama import OllamaEmbeddings

model = OllamaEmbeddings(
    model="nomic-embed-text",
    base_url="http://localhost:11434"
)
print(model.embed_query("你好")) #作用：将文本转换为向量表示
print("-----------------")
print(model.embed_documents(["你好","你好不好"])) #作用：将文本列表转换为向量列表
print("-----------------")



