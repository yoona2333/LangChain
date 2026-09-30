from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_ollama import ChatOllama

parser = StrOutputParser() # 输出解析器，将模型输出转换为字符串
model = ChatOllama(
    model="qwen3-vl:4b",
    base_url="http://localhost:11434",
)

prompt = PromptTemplate.from_template(
    "我邻居姓：{lastname}，刚生了{gender}，请起名，仅告知我名字无需其它内容。"
)

chain = prompt | model | parser | model | parser

res: str = chain.invoke({"lastname": "张", "gender": "女儿"}) # 执行链 ，返回字符串
print(res)
print(type(res))
