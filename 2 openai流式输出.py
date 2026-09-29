import os
from random import choices

from openai import OpenAI


client = OpenAI(
    api_key="qw",
    base_url="http://localhost:11434/v1"
)

messages = [
    {"role":"system","content":"You are a helpful assistant"},
    {"role": "assistant", "content": "我是千问的助手"},
    {"role":"user","content":"你是什么模型?你能做什么?"}
]
response=client.chat.completions.create(
    model="qwen3-vl:4b",
    messages=messages,
    n=1,
    stream=True
)
# print(response.choices[0].message.content)
# print(response.choices[0])
print('-'*100)
for chunk in response:
    print(
        chunk.choices[0].delta.content, # 打印流式输出的内容
        end="", # 每段之间以空格分隔，不换行
        flush=True # 实时打印 ，不缓存 立刻刷新缓冲区
    )


