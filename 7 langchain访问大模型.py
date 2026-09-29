from langchain_core import messages
from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage, SystemMessage

model = ChatOllama(
    model="qwen3-vl:4b",
    base_url="http://localhost:11434",
)
messages=[
    SystemMessage(content="你是一个专业的英语翻译"),
    HumanMessage(content="把你好不好翻译成英文")
]

# stream返回迭代器，要用for循环遍历chunk
# for chunk in model.stream([HumanMessage("deepseek怎么样？")]):
      # print(chunk.content, end="", flush=True)
res=model.invoke(input=messages)
print(res)
print('-----------------')
print(res.content)
