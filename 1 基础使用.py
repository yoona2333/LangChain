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
    n=1
)
print(response.choices[0].message.content)
# print(response.choices[0])
print('-'*50)
# print(response.choices[1])
# print('-'*50)
# print(response.choices[2])
