import chatollama
from langchain_classic.chains.summarize.map_reduce_prompt import prompt_template
from langchain_community.llms import ollama
from langchain_core.messages import HumanMessage
from langchain_core.prompts import PromptTemplate
from langchain_ollama import ChatOllama
from ollama import chat

prompt_template=PromptTemplate.from_template(
    "我的邻居{lastname}，刚生了个{gender}，你帮我起个名字，简单回答"
)

prompt_txt=prompt_template.format(lastname="张三",gender="男")

model=ChatOllama(
    model="qwen3-vl:4b",
    base_url="http://localhost:11434",
)
message=HumanMessage(content=prompt_txt)

# res=model.invoke([HumanMessage(content=prompt_txt)])
# print(prompt_txt)
res=model.invoke((prompt_txt))


print(res.content)
print("-----------------")