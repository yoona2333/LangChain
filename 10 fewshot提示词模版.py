from sys import prefix

import chatollama
from langchain_classic.chains.constitutional_ai.prompts import examples
from langchain_classic.prompts import few_shot
from langchain_community.chat_models.openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate,FewShotPromptTemplate
from langchain_ollama import ChatOllama

example_template=PromptTemplate.from_template("单词：{word}，反义词：{antonym}")

examples_data=[
    {"word":"好","antonym":"坏"},
    {"word":"大","antonym":"小"},
    {"word":"快","antonym":"慢"},
]


few_shot_template=FewShotPromptTemplate(
    example_prompt=example_template,   # 示例的提示词模版
    examples=examples_data,         # 示例的数据
    prefix="告诉我单词的反义词，我提供如下的示例：",           # 提示词的前缀
    suffix="基于前面示例告诉我，{input_word}的反义词是：",           # 提示词的后缀
    input_variables=["input_word"],           # 提示词中使用的输入变量
)

prompt_text=few_shot_template.invoke({"input_word":"高"}).to_string()
print(prompt_text)

model=ChatOllama(
    model="qwen3-vl:4b",
    base_url="http://localhost:11434",
)

# res=model.invoke(prompt_text)
# # print(res)
# print(res.content)
for chunk in model.stream(prompt_text): # 流式输出 边生成边返回一小段文本（chunk）
    if chunk.content:
        print(chunk.content,end="",flush=True)  # 实时打印模型的输出

